from commonpower.control.logging_utils.loggers import *
from pathlib import Path
from commonpower.control.safety_layer.safety_layers import ActionProjectionSafetyLayer
from commonpower.core import System
from commonpower.models.components import *
from commonpower.models.buses import *
from commonpower.models.powerflow import *
from commonpower.data_forecasting import *
from commonpower.modeling.param_initialization import *
from commonpower.control.controllers import RLControllerMA, OptimalController
from commonpower.control.observation_handling import ObservationHandler
from commonpower.control.logging_utils.callbacks import *
from commonpower.control.wrappers import MultiAgentWrapper
from commonpower.control.runners import MAPPOTrainer, DeploymentRunner
from commonpower.control.configs.algorithms import *
from commonpower.control.safety_layer.penalties import *
from commonpower.modeling.history import ModelHistory
import unittest
import shutil


class TestControl(unittest.TestCase):
    def setUp(self):
        os.makedirs("./tests/artifacts/", exist_ok=True)

    def tearDown(self):
        shutil.rmtree("./tests/artifacts/")

    def test_marl_training(self):
        horizon = timedelta(hours=24)
        frequency = timedelta(minutes=60)

        data_path = Path(__file__).parent / "data" / "1-LV-rural2--1-sw"
        data_path = data_path.resolve()

        ds1 = CSVDataSource(
            data_path / "LoadProfile.csv",
            delimiter=";",
            datetime_format="%d.%m.%Y %H:%M",
            rename_dict={"time": "t", "H0-A_pload": "p", "H0-A_qload": "q"},
            auto_drop=True,
            resample=frequency,
        )

        ds2 = CSVDataSource(
            data_path / "LoadProfile.csv",
            delimiter=";",
            datetime_format="%d.%m.%Y %H:%M",
            rename_dict={"time": "t", "G1-B_pload": "psib", "G1-C_pload": "psis", "G2-A_pload": "psi"},
            auto_drop=True,
            resample=frequency,
        )

        ds3 = CSVDataSource(
            data_path / "RESProfile.csv",
            delimiter=";",
            datetime_format="%d.%m.%Y %H:%M",
            rename_dict={"time": "t", "PV3": "p"},
            auto_drop=True,
            resample=frequency,
        ).apply_to_column("p", lambda x: -x)

        dp1 = DataProvider(
            ds1, PerfectKnowledgeForecaster(frequency=frequency, horizon=horizon)
        )
        dp2 = DataProvider(
            ds2, PerfectKnowledgeForecaster(frequency=frequency, horizon=horizon)
        )
        dp3 = DataProvider(
            ds3, PerfectKnowledgeForecaster(frequency=frequency, horizon=horizon)
        )

        n1 = RTPricedBusLinear(
            "MultiFamilyHouse",
            {
                "p": [-50, 50],
                "q": [-50, 50],
                "v": [0.95, 1.05],
                "d": [-15, 15]
            }
        ).add_data_provider(dp2)

        n2 = RTPricedBusLinear(
            "MultiFamilyHouse_2",
            {
                "p": [-50, 50],
                "q": [-50, 50],
                "v": [0.95, 1.05],
                "d": [-15, 15]
            }
        ).add_data_provider(dp2)

        # components
        # energy storage sytem
        capacity = 3  # kWh
        e1 = ESSLinear(
            "ESS1",
            {
                "rho": 0.1,
                "p": [-1.5, 1.5],
                "q": [0, 0],
                "soc": [0.2 * capacity, 0.8 * capacity],
                "soc_init": RangeInitializer(0.2 * capacity, 0.8 * capacity),
            },
        )

        capacity_2 = 6
        e2 = ESSLinear(
            "ESS1",
            {
                "rho": 0.1,
                "p": [-3, 3],
                "q": [0, 0],
                "soc": [0.2 * capacity_2, 0.8 * capacity_2],
                "soc_init": RangeInitializer(0.2 * capacity_2, 0.8 * capacity_2),
            },
        )

        # photovoltaic with generation data
        r1 = RenewableGen("PV1").add_data_provider(dp3)

        # static load with data source
        d1 = Load("Load1").add_data_provider(dp1)
        d2 = Load("Load1").add_data_provider(dp1)

        # external grid
        n999 = ExternalGrid("ExternalGrid")

        # we first have to add the nodes to the system
        # and then add components to the node in order to obtain a tree-like structure
        sys = System(power_flow_model=PowerBalanceModel()).add_node(n1).add_node(n2).add_node(n999)

        # add components to nodes
        n1.add_node(d1).add_node(e1).add_node(r1)
        n2.add_node(d2).add_node(e2)

        # show system structure:
        sys.pprint()

        # algorithm configuration
        config = MAPPOBaseConfig(
            algorithm_name='mappo',
            seed=1,
            num_env_steps=1 * int(horizon.total_seconds() // 3600),
            episode_length=1 * int(horizon.total_seconds() // 3600),
            penalty_factor=2.0
        )

        # add controllers
        for i in range(len(sys.nodes) - 1):
            # will also add a controller to households which do not have inputs (e.g., households with only a Load component),
            # but these are disregarded when the system is initialized
            if i==0: 
                # first agent also gets the load of the second agent as obs (to test global obs functionality)
                _ = RLControllerMA(
                    name=str.join("agent", str(i)),
                    obs_handler=ObservationHandler(num_forecasts=4, num_past_observations=1, global_obs_elements=[(d2, ["p"])]),
                    safety_layer=ActionProjectionSafetyLayer(penalty=DistanceDependingPenalty(penalty_factor=10.0)),
                ).add_entity(sys.nodes[i])
            else:
                _ = RLControllerMA(
                    name=str.join("agent", str(i)),
                    obs_handler=ObservationHandler(num_forecasts=4, num_past_observations=1),
                    safety_layer=ActionProjectionSafetyLayer(penalty=DistanceDependingPenalty(penalty_factor=10.0)),
                ).add_entity(sys.nodes[i])

        # set up logger
        logger = MARLTensorboardLogger(log_dir="./tests/artifacts/test_run/", callback=MARLBaseCallback)
        # set up trainer
        runner = MAPPOTrainer(
            sys=sys,
            global_controller=OptimalController("global"),
            wrapper=MultiAgentWrapper,
            alg_config=config,
            seed=5,
            logger=logger,
        )
        # run training
        runner.run(fixed_start=datetime(2016, 11, 27))

        # deployment
        # load pre-trained policies
        load_path = "./saved_models/test_model"  # default location
        # first agent also gets the load of the second agent as obs (to test global obs functionality)
        trained_agent_1 = RLControllerMA(
            name="trained_mappo_agent_1",
            obs_handler=ObservationHandler(num_forecasts=4, num_past_observations=1, global_obs_elements=[(d2, ["p"])]),
            safety_layer=ActionProjectionSafetyLayer(penalty=DistanceDependingPenalty(penalty_factor=10.0)),
            pretrained_policy_path=load_path + "/agent0",
        ).add_entity(sys.nodes[0])
        # second agent only has local obs
        trained_agent_2 = RLControllerMA(
            name="trained_mappo_agent_2",
            obs_handler=ObservationHandler(num_forecasts=4, num_past_observations=1),
            safety_layer=ActionProjectionSafetyLayer(penalty=DistanceDependingPenalty(penalty_factor=10.0)),
            pretrained_policy_path=load_path + "/agent1",
        ).add_entity(sys.nodes[1])

        sys_history_mappo = ModelHistory([sys])

        runner = DeploymentRunner(
            sys=sys,
            global_controller=OptimalController("global"),
            alg_config=config,
            wrapper=MultiAgentWrapper,
            history=sys_history_mappo,
            seed=1,
        )
        runner.run(n_steps=2, fixed_start=datetime(2016, 11, 27))

        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
