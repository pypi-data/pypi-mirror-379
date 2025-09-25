## Dependencies:
import json
import webbrowser
import datetime
from copy import deepcopy
from typing import Any, Callable, Dict, List, NoReturn, Optional, Tuple, Union

import psutil
import ray

# typing
import ray.remote_function
import ray.runtime_context

# context aware progress bar
# detect jupyter notebook
from IPython.core.getipython import get_ipython

try:
    ipy_str = str(type(get_ipython()))
    if "zmqshell" in ipy_str:
        pass
    else:
        pass
except Exception as _:
    pass

## loal
from .scheduler import Scheduler
from .listener import Listener


# %% Multi Core Execution Main
class MultiCoreExecutionTool:
    RuntimeData: Dict[Any, Dict[Any, Any]]

    RuntimeResults: Dict[Any, Dict[str, Any]]
    RuntimeContext: ray.runtime_context.RuntimeContext
    RuntimeMetadata: Dict[str, Union[str, bool, int, float]]
    RuntimeArchive: Dict[str, Dict[Any, Dict[str, Any]]]
    DashboardURL: str

    AutoLaunchDashboard: bool
    silent: bool
    DEBUG: bool

    SingleShot: bool
    AutoContinue: bool
    AutoArchive: bool

    def __init__(
        self, RuntimeData: Dict[Any, Dict[Any, Any]] = {}, /, **kwargs
    ) -> NoReturn:
        """Constructor for the MultiCoreExecutionTool class.

        Args:
            RuntimeData (Dict[Any,Dict[Any,Any]], optional): Dictionary containing keyword arguments for the methods to run. Defaults to None.

        Returns:
            MultiCoreExecutionTool: MultiCoreExecutionTool object.
        """
        ## Default Verbosity
        self.AutoLaunchDashboard = False
        self.silent = False
        self.DEBUG = False

        ## Initialize attributes
        self.DashboardURL = None
        self.RuntimeContext = None
        self.RuntimeMetadata = {}
        self.RuntimeResults = {}
        self.RuntimeArchive = {}

        ## Set Behavior
        self.SingleShot = False
        self.AutoContinue = False
        self.AutoArchive = True

        ## Setattributes
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

        ## set the debug flag
        if "DEBUG" in kwargs.keys():
            self.DEBUG = kwargs["DEBUG"]
            if self.DEBUG:
                print("Debug mode is enabled. Using verbose mode.")
                self.silent = False

        if "SingleShot" in kwargs.keys():
            self.SingleShot = kwargs["SingleShot"]

            if self.SingleShot:
                self.AutoArchive = False
                self.AutoContinue = True
                print(
                    "SingleShot mode is enabled. Archive disabled. AutoContinue enabled."
                )

        self.__post_init__(RuntimeData, **kwargs)

    def __post_init__(
        self, RuntimeData: Dict[Any, Dict[Any, Any]], /, **kwargs
    ) -> NoReturn:
        """Post initialization method for the MultiCoreExecutionTool class. Handles routine initialization tasks.

        Args:
            RuntimeData (Dict[Any,Dict[Any,Any]]): Structured data to be processed by the methods.

        Returns:
            NoReturn: No Return
        """
        self.__initialize_metadata__(**kwargs)
        self.__initialize_ray_cluster__()
        self.__offload_on_init__(RuntimeData)

    # %% Class methods
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "MultiCoreExecutionTool":
        """Convenience method to create a MultiCoreExecutionTool object from a dictionary.

        Returns:
            MultiCoreExecutionTool: MultiCoreExecutionTool object.
        """
        return cls(**data)

    @classmethod
    def from_json(cls, path: str) -> "MultiCoreExecutionTool":
        """Convenience method to create a MultiCoreExecutionTool object from a JSON file.

        Args:
            path (str): Path to the JSON file.

        Returns:
            MultiCoreExecutionTool: MultiCoreExecutionTool object.
        """
        with open(path, "r") as file:
            data = json.load(file)
        return cls(**data)

    # %% Ray Wrapper
    def __setup_wrapper__(self) -> Callable:
        @ray.remote(**self.RuntimeMetadata["task_metadata"])
        def __method_wrapper__(
            method: Callable, input: Dict[Any, Any]
        ) -> ray.remote_function.RemoteFunction:
            """Ray wrapper for arbitrary function logic.

            Args:
                method (Callable): Arbitrary method that takes at least one input.
                input (Dict[Any,Any]): Method input that will be forwarded to the main logic.

            Returns:
                Callable: Returns a ray.remote callable object.
            """
            return method(**input)

        return __method_wrapper__

    # %% Main Backend
    def __run__(
        self, worker: Union[Callable, ray.remote_function.RemoteFunction]
    ) -> bool:
        """Main execution method for the MultiCoreExecutionTool class. Runs the provided worker on the provided data.

        Args:
            worker (Union[Callable, ray.remote_function.RemoteFunction]): Main worker or logic. Can be either ray.remote or a callable.

        Raises:
            Exception: Exception is raised if the core logic is not ray compatible.

        Returns:
            bool: Boolean flag that is True if the execution is successful.
        """

        # forwards the worker to the batch method
        return self.__batch__(worker, runIDs="all")

    def __batch__(
        self,
        worker: Union[Callable, ray.remote_function.RemoteFunction],
        *,
        runIDs: Union[int, List[Any], str] = "all",
    ) -> bool:
        """Batch execution method for the MultiCoreExecutionTool class. Runs the provided worker on the provided data.

        Args:
            worker (Union[Callable, ray.remote_function.RemoteFunction]): Main worker or logic. Can be either ray.remote or a callable.
            runIDs (Union[int, List[Any], str], optional): RunIDs to process. Defaults to 'all'.

        Raises:
            Exception: Exception is raised if the core logic is not ray compatible.

        Returns:
            bool: Boolean flag that is True if the execution
        """

        ## check if ray is initialized
        if not ray.is_initialized():
            raise Exception(
                "Ray is not initialized. Use object.initialize() to initialize Ray."
            )

        if not self.__is_ray_compatible__(worker):
            try:
                coreLogic = worker
                worker = self.__setup_wrapper__()
            except Exception as e:
                print(f"Error: {e}")
                return False

        ## prepare schedule
        schedule = self.__setup_schedule__()

        ## check for pending tasks
        if not self.__has_pending_results__():
            print("No pending tasks found. Exiting...")
            return True

        ## handle runIDs, skip if all
        if not runIDs == "all":
            ## check for runIDs
            if not self.__RunIDs_in_RuntimeData__(runIDs):
                print(
                    "Invalid RunIDs. Please provide a list of keys referring to the RuntimeData or a number of tasks to run that is <= the total amount of tasks."
                )
                return False

            ## select the runIDs
            if isinstance(runIDs, int):
                schedule = schedule[:runIDs]
            elif isinstance(runIDs, list):
                schedule = [k for k in schedule if k in runIDs]
            else:
                print(
                    "Invalid RunIDs. Please provide a list of keys referring to the RuntimeData or a number of tasks to run that is <= the total amount of tasks."
                )
                return False

            if self.DEBUG:
                print(f"Running {runIDs} tasks...")

        ## check for schedule
        if len(schedule) == 0:
            print("No pending tasks to run. Exiting...")
            return True

        ## workflow factory
        if self.silent:
            permision, states = self.__multicore_workflow__(
                worker=worker,
                schedule=schedule,
                listener=Listener(DEBUG=self.DEBUG).silent,
                scheduler=Scheduler(DEBUG=self.DEBUG).silent,
                coreLogic=coreLogic if "coreLogic" in locals() else None,
            )
        else:
            permision, states = self.__multicore_workflow__(
                worker=worker,
                schedule=schedule,
                listener=Listener(DEBUG=self.DEBUG).verbose,
                scheduler=Scheduler(DEBUG=self.DEBUG).verbose,
                coreLogic=coreLogic if "coreLogic" in locals() else None,
            )

        ## update the results
        if permision:
            if self.DEBUG:
                print("Writing result refs to RuntimeResults...")
            for k in schedule:
                self.RuntimeResults[k].update(
                    {"result": states[k], "status": "completed"}
                )

        return permision

    def __multicore_workflow__(
        self,
        worker: Union[Callable, ray.remote_function.RemoteFunction],
        schedule: List[Any],
        listener: Callable,
        scheduler: Callable,
        coreLogic: Optional[Callable],
    ) -> Tuple[bool, Dict[int, Any]]:
        """Workflow for the MultiCoreExecutionTool class. Handles the main execution logic.

        Args:
            worker (Union[Callable, ray.remote_function.RemoteFunction]): Remote callable object. See ray.remote for more information.
            schedule (List[Any]): List of keys referring to RuntimeData values to be processed using the provided method.
            listener (Callable): Chosen listener.
            scheduler (Callable): Chosen scheduler.
            coreLogic (Optional[Callable]): Core logic of local function that will be forwarded to ray.

        Returns:
            Tuple[bool, Dict[int,Any]]: Boolean flag signaling the success or the execution, Dictionary containing the results of the execution.
        """
        ## workflow and listening
        permission, finished_states = listener(
            scheduler(worker, self.RuntimeData_ref, schedule, coreLogic)
        )

        ## check completion
        if permission:
            self.RuntimeResults | {
                k: {"result": v, "status": "completed"}
                for k, v in finished_states.items()
            }

            ## Shutdown Ray
            if self.DEBUG:
                print("Multi Core Execution Complete...")
                print("Use 'shutdown_multi_core()' to shutdown the cluster.")

            return True, finished_states

        return False, None

    ##### API #####
    # %% Main Execution
    def run(
        self, worker: Union[Callable, ray.remote_function.RemoteFunction]
    ) -> Union[bool, Dict[Any, Dict[str, Any]]]:
        """Run API for the MultiCoreExecutionTool class. Main API for running the provided worker on the provided data.

        Args:
            worker (Union[Callable, ray.remote_function.RemoteFunction]): Main worker or logic. Can be either ray.remote or a callable.

        Returns:
            bool: Boolean flag that is True if the execution was successful.
        """
        try:
            permission: bool = self.__run__(worker)
            assert permission

            if self.DEBUG:
                print("Multi Core Execution Complete...")
                print('Use "get_results()" to get the results.')

        except Exception as e:
            print(f"Error: {e}")
            return False

        if self.SingleShot:
            assert self.next(), "Error: Could not move to next task."
            return self.get_results()

        if self.AutoContinue:
            return self.next()

    def batch(
        self,
        worker: Union[Callable, ray.remote_function.RemoteFunction],
        *,
        runIDs: Union[int, List[Any], str] = "all",
    ) -> Union[bool, Dict[Any, Dict[str, Any]]]:
        """Batch API for the MultiCoreExecutionTool class. Main API for running the provided worker on the provided data.

        Args:
            worker (Union[Callable, ray.remote_function.RemoteFunction]): Main worker or logic. Can be either ray.remote or a callable.
            runIDs (Union[int, List[Any], str], optional): RunIDs to process. Defaults to 'all'.

        Returns:
            bool: Boolean flag that is True if the execution was successful.
        """
        try:
            permission: bool = self.__batch__(worker, runIDs=runIDs)
            assert permission

            if self.DEBUG:
                print("Multi Core Execution Complete...")
                print('Use "get_results()" to get the results.')

        except Exception as e:
            print(f"Error: {e}")
            return False

        if self.SingleShot:
            assert self.next(), "Error: Could not move to next task."
            return self.get_results()

        if self.AutoContinue:
            return self.next()

    # %% Runtime Control
    def initialize(self) -> NoReturn:
        """Initialize the Ray cluster using the parameters found in sel.RuntimeMetadata['instance_metadata']".
           See https://docs.ray.io/en/latest/ray-core/api/doc/ray.init.html for more information.

        Returns:
            NoReturn: No Return.
        """
        try:
            assert self.__initialize_ray_cluster__()
        except Exception as e:
            print(f"Error: {e}")
            return None

    def shutdown(self) -> NoReturn:
        """Shutdown the Ray cluster.

        Returns:
            NoReturn: No Return.
        """
        self.__shutdown__()

    def reset(self) -> NoReturn:
        """Resets RuntimeData and RuntimeData reference. Restores RuntimeMetadata defaults.

        Returns:
            NoReturn: No Return.
        """
        self.__reset__()

    def reboot(self) -> NoReturn:
        """Reboot the MultiCoreExecutionTool object. Can be provided with new instance parameters. See instance attributes for more information.

        Returns:
            NoReturn: No Return.
        """
        self.__reboot__()

    def launch_dashboard(self) -> bool:
        """Launch ray dashboard in default browser.

        Returns:
            bool: Status of the operation.
        """
        return self.__launch_dashboard__()

    # %% Runtime Data Control
    def update_data(self, RuntimeData: Dict[Any, Dict[Any, Any]]) -> NoReturn:
        """Update the RuntimeData with the provided data.

        Args:
            RuntimeData (Dict[Any,Dict[Any,Any]]): Structured data to be processed by the methods.

        Returns:
            NoReturn: No Return.
        """
        self.__update_data__(RuntimeData)

    def update_metadata(self, **kwargs) -> NoReturn:
        self.RuntimeMetadata.update(kwargs)

        ## check if the metadata is valid
        ## we will only notify the user if the metadata is invalid or the DEBUG flag is set
        status = self.__ressource_requirements_met__()
        if not status:
            print("Please adjust the metadata.")
        elif status and self.DEBUG:
            print("Metadata updated.")

    # %% Runtime Handling Backend
    def __initialize_metadata__(self, **kwargs) -> NoReturn:
        """Initializes the metadata for the MultiCoreExecutionTool class. Contains default values and will overwrite with given values.

        Returns:
            NoReturn: No Return
        """
        ## Default Metadata
        self.RuntimeMetadata = {
            "instance_metadata": {
                "num_cpus": 1,
                "num_gpus": 0,
                "address": None,
                "ignore_reinit_error": True,
            },
            "task_metadata": {"num_cpus": 1, "num_gpus": 0, "num_returns": None},
        }
        # update metadata with given values
        self.RuntimeMetadata.update(kwargs)

        ## check if the metadata is valid
        ## we will only notify the user if the metadata is invalid or the DEBUG flag is set
        status = self.__ressource_requirements_met__()
        if not status:
            print("Please adjust the metadata.")
        elif status and self.DEBUG:
            print("Metadata updated.")

    def __offload_on_init__(self, RuntimeData: Dict[Any, Dict[Any, Any]]) -> NoReturn:
        """Offload RuntimeData items to ray cluster on initialization if RuntimeData is provided.

        Args:
            RuntimeData (Dict[Any,Dict[Any,Any]]): Structured data to be processed by the methods.

        Returns:
            NoReturn: No Return
        """
        ## This has to be called AFTER the ray is initialized
        # otherwise, a new ray object will be created and the object references will be unreachable from within the main ray object.

        if RuntimeData is None:
            print(
                'No Runtime Data provided. Use the "update_data()" method to update the Runtime Data prior to running methods.'
            )
            return None

        ## Set RuntimeData
        self.RuntimeData = RuntimeData if RuntimeData is not None else None
        self.RuntimeData_ref = (
            self.__offload_data__() if RuntimeData is not None else None
        )
        self.RuntimeResults = (
            self.__setup_RuntimeResults__() if RuntimeData is not None else None
        )
        self.RuntimeArchive = {} if RuntimeData is not None else None

    def __initialize_ray_cluster__(self) -> bool:
        """Initialize the Ray cluster using the parameters found in sel.RuntimeMetadata['instance_metadata']".
           See https://docs.ray.io/en/latest/ray-core/api/doc/ray.init.html for more information.

        Returns:
            NoReturn: No Return
        """

        if self.__is_initalized__():
            print('Ray is already initialized. Use "reboot()" to reboot the object.')
            return False

        if self.DEBUG:
            print("Setting up Ray...")

        # shutdown any stray ray instances
        ray.shutdown()

        # ray init
        RuntimeContext = ray.init(**self.RuntimeMetadata["instance_metadata"])
        self.DashboardURL = f"http://{RuntimeContext.dashboard_url}/"

        # dashboard
        if self.AutoLaunchDashboard:
            self.__launch_dashboard__()

        if self.DEBUG:
            print("Ray setup complete...")
            print(f"Ray Dashboard: {self.DashboardURL}")

        # set the runtime context
        self.RuntimeContext = RuntimeContext

        return True

    def __shutdown__(self) -> bool:
        """Shutdown the Ray cluster.

        Returns:
            bool: True if the shutdown was successful.
        """
        if self.DEBUG:
            print("Shutting down Ray...")
        try:
            ray.shutdown()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def __reset__(self) -> NoReturn:
        """Resets RuntimeData and RuntimeData reference. Restores RuntimeMetadata defaults.

        Returns:
            NoReturn: No Return
        """
        self.RuntimeData_ref = None
        self.RuntimeData = None
        self.__initialize_metadata__()

    def __reboot__(self) -> NoReturn:
        """Reboots the MultiCoreExecutionTool object. Can be provided with new instance parameters. See https://docs.ray.io/en/latest/ray-core/api/doc/ray.init.html for more information.

        Returns:
            NoReturn: _description_
        """
        try:
            self.__shutdown__()
            self.__initialize_ray_cluster__()
            self.__offload_data__()
        except Exception as e:
            print(f"Error: {e}")

    def __launch_dashboard__(self) -> bool:
        """Launch ray dashboard in default browser.

        Returns:
            bool: Status of the operation.
        """
        if self.DEBUG:
            print("Preparing to launch ray dashboard...")

        if not self.__is_initalized__():
            print('Ray is not initialized. Use "initialize()" to initialize Ray.')
            return False

        try:
            webbrowser.get("windows-default").open(
                self.DashboardURL, autoraise=True, new=2
            )
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    # %% Runtime Data Handling
    def __setup_schedule__(self) -> List[Any]:
        """Bundle the RuntimeData keys into a list for scheduling.

        Returns:
            List[Any]: List of keys referring to RuntimeData values to be processed using the provided method.
        """
        return [k for k, v in self.RuntimeResults.items() if v["status"] == "pending"]

    def __setup_RuntimeResults__(self) -> Dict[int, Dict[str, Any]]:
        """Setup the RuntimeResults dictionary.

        Returns:
            Dict[int,Dict[str,Any]]: Dictionary containing the results of the execution
        """
        return {
            k: {"result": None, "status": "pending"} for k in self.RuntimeData.keys()
        }

    def __offload_data__(self) -> Dict[int, ray.ObjectRef]:
        """Offload the RuntimeData to the ray cluster.

        Returns:
            Dict[int,ray.ObjectRef]: Dictionary of keys and ray object references.
        """
        if self.DEBUG:
            print("Offloading data to Ray...")
        return {k: ray.put(v) for k, v in self.RuntimeData.items()}

    def __move_results_to_archive__(self) -> NoReturn:
        """Move the RuntimeResults to the RuntimeArchive.

        Returns:
            NoReturn: No Return
        """
        if self.DEBUG:
            print("Moving results to RuntimeArchive...")

        # set status to archived
        for k, v in self.RuntimeResults.items():
            if v["status"] == "completed":
                v["status"] = "archived"
            if v["status"] == "retrieved":
                v["status"] = "archived"
            if v["status"] == "pending":
                v["status"] = "no result"

        # write to archive
        self.RuntimeArchive[datetime.datetime.now().isoformat(timespec="seconds")] = (
            deepcopy(self.RuntimeResults)
        )
        # reset results
        self.RuntimeResults = self.__setup_RuntimeResults__()

    def __update_data__(self, RuntimeData: Dict[Any, Dict[Any, Any]]) -> NoReturn:
        """Update the RuntimeData with the provided data and offload the data to the ray cluster.

        Args:
            RuntimeData (Dict[int,Dict[str,Any]]): Structured data to be processed by the methods.

        Returns:
            NoReturn: No Return
        """
        if self.DEBUG:
            print("Updating Runtime Data...")

        self.RuntimeData = RuntimeData
        self.RuntimeData_ref = self.__offload_data__()

        if (
            self.RuntimeResults is not None
            and self.AutoArchive
            and not self.__all_results_pending__()
        ):
            self.__move_results_to_archive__()
            print("Previous results detected and moved to RuntimArchive.")
        else:
            self.RuntimeResults = self.__setup_RuntimeResults__()

    # %% Helper
    def __cpus_available__(self) -> bool:
        """Check if the Ray cluster has enough CPUs.

        Args:
            num_cpus (int): Number of CPUs.

        Returns:
            bool: True if the Ray cluster has enough CPUs. False otherwise.
        """
        if self.DEBUG:
            print("Checking CPU availability...")
        try:
            assert (
                psutil.cpu_count()
                >= self.RuntimeMetadata["instance_metadata"]["num_cpus"]
            )
            return True
        except AssertionError:
            print("Error: Not enough CPUs available.")
            print(
                "Requested CPUs: ",
                self.RuntimeMetadata["instance_metadata"]["num_cpus"],
            )
            print("Available CPUs: ", psutil.cpu_count())
            return False

    def __tasks_meet_cpu_requirements__(self) -> bool:
        """Check if the tasks meet the CPU requirements.

        Args:
            num_cpus (int): Number of CPUs.

        Returns:
            bool: True if the tasks meet the CPU requirements. False otherwise.
        """
        if self.DEBUG:
            print("Checking CPU requirements...")
        try:
            assert (
                self.RuntimeMetadata["task_metadata"]["num_cpus"]
                <= self.RuntimeMetadata["instance_metadata"]["num_cpus"]
            )
            return True
        except AssertionError:
            print(
                "Error: Tasks are assigned too many CPUs. None will be able to execute on the Ray cluster."
            )
            print(
                "Requested CPUs per Task: ",
                self.RuntimeMetadata["task_metadata"]["num_cpus"],
            )
            print(
                "Available CPUs in Cluster: ",
                self.RuntimeMetadata["instance_metadata"]["num_cpus"],
            )
            print(
                "Please adjust the number of CPUs per task. Or increase the number of CPUs in the Ray cluster."
            )
            return False

    def __warn_gpu_is_used__(self) -> bool:
        """Check if the Ray cluster has enough GPUs.

        Args:
            num_gpus (int): Number of GPUs.

        Returns:
            bool: True if the Ray cluster has enough GPUs. False otherwise.
        """
        if self.DEBUG:
            print("Checking GPU ise used...")
        if self.RuntimeMetadata["instance_metadata"]["num_gpus"] > 0:
            print("Warning: GPU is used.")
            print("Please make sure that the Ray cluster has enough GPUs.")
            print("You may need to manually check the GPU availability.")
            print(
                "Alternatively, you can use torch.cuda.is_available() to check the GPU availability."
            )
        return True

    def __ressource_requirements_met__(self) -> bool:
        """Check if the ressource requirements are met.

        Args:
            num_cpus (int): Number of CPUs.
            num_gpus (int): Number of GPUs.

        Returns:
            bool: True if the ressource requirements are met. False otherwise.
        """
        if self.DEBUG:
            print("Checking ressource requirements...")
        return (
            self.__cpus_available__()
            and self.__warn_gpu_is_used__()
            and self.__tasks_meet_cpu_requirements__()
        )

    def __is_ray_compatible__(self, func: Callable) -> bool:
        """Check if the provided function is ray compatible.

        Args:
            func (Callable): Provided function.

        Returns:
            bool: True if the function is ray compatible. False otherwise.
        """
        if isinstance(func, ray.remote_function.RemoteFunction):
            return True
        return False

    def __is_initalized__(self) -> bool:
        """Check of the Ray cluster is initialized.

        Returns:
            bool: True if the Ray cluster is initialized. False otherwise.
        """
        if self.DEBUG:
            print("Checking Ray Status...")
        return ray.is_initialized()

    def __has_pending_results__(self) -> bool:
        """Check if there are pending results.

        Returns:
            bool: True if there are pending results. False otherwise.
        """
        if self.DEBUG:
            print("Checking for pending results...")
        return any([v["status"] == "pending" for k, v in self.RuntimeResults.items()])

    def __all_results_pending__(self) -> bool:
        """Check if all results are pending.

        Returns:
            bool: True if all results are pending. False otherwise.
        """
        if self.DEBUG:
            print("Checking if all results are pending...")
        return all([v["status"] == "pending" for k, v in self.RuntimeResults.items()])

    def __has_completed_results__(self) -> bool:
        """Check if there are completed results.

        Returns:
            bool: True if there are completed results. False otherwise.
        """
        if self.DEBUG:
            print("Checking for completed results...")
        return any([v["status"] == "completed" for k, v in self.RuntimeResults.items()])

    def __all_results_retrieved__(self) -> bool:
        """Check if all results are retrieved.

        Returns:
            bool: True if all results are retrieved. False otherwise.
        """
        if self.DEBUG:
            print("Checking if all results are retrieved...")
        return all([v["status"] == "retrieved" for k, v in self.RuntimeResults.items()])

    def __RunIDs_in_RuntimeData__(self, RunIDs: Union[int, List[Any]]) -> bool:
        """Check if the provided RunIDs are in the RuntimeData.

        Args:
            RunIDs (Union[int, List[Any]]): RunIDs to check.

        Returns:
            bool: True if the RunIDs are in the RuntimeData. False otherwise.
        """
        if self.DEBUG:
            print("Checking if RunIDs are in RuntimeData...")
        if isinstance(RunIDs, int):
            return RunIDs <= len(self.RuntimeData)
        return all([k in self.RuntimeData.keys() for k in RunIDs])

    def retreive_data(self) -> bool:
        """Retreive the RuntimeData.

        Returns:
            Dict[Any,Dict[Any,Any]]: Structured data to be processed by the methods.
        """
        if self.DEBUG:
            print("Retreiving Data...")

        if self.RuntimeResults is None:
            print('No results found. Use the "run()" method to get results.')
            return False

        try:
            for refKey, objRef in self.RuntimeResults.items():
                if objRef["status"] == "completed":
                    self.RuntimeResults[refKey].update(
                        {"result": ray.get(objRef["result"])}
                    )
                    self.RuntimeResults[refKey].update({"status": "retrieved"})
        except Exception as e:
            print(f"Error: {e}")
            return False

        return True

    def get_results(self) -> Dict[Any, Dict[str, Any]]:
        """Returns RuntimeResults.

        Returns:
            Dict[Any,Dict[Any,Any]]: Structured data containing the results of the execution.
        """
        if self.DEBUG:
            print("Fetching Results...")

        if self.RuntimeResults is None:
            print('No results found. Use the "run()" method to get results.')
            return None

        if self.__has_pending_results__():
            print('Pending results found. Use the "run()" method to get results.')

        if self.__all_results_retrieved__():
            return deepcopy(self.RuntimeResults)

        elif self.__has_completed_results__():
            self.retreive_data()
            return deepcopy(self.RuntimeResults)

        else:
            print('No results found. Use the "run()" method to get results.')
            return None

    def get_archive(self) -> Dict[str, Dict[Any, Dict[str, Any]]]:
        """Returns RuntimeArchive.

        Returns:
            Dict[str,Dict[Any,Dict[str,Any]]]: Structured data containing the archived results.
        """
        if self.DEBUG:
            print("Fetching Archive...")
        return deepcopy(self.RuntimeArchive)

    def get_archive_keys(self) -> List[str]:
        """Returns the keys of the RuntimeArchive.

        Returns:
            List[str]: List of keys referring to the RuntimeArchive values.
        """
        if self.DEBUG:
            print("Fetching Archive Keys...")
        return list(self.RuntimeArchive.keys())

    def get_all_results(
        self,
    ) -> Tuple[Dict[Any, Dict[str, Any]], Dict[str, Dict[Any, Dict[str, Any]]]]:
        """Returns RuntimeResults and RuntimeArchive.

        Returns:
            Tuple[Dict[Any,Dict[str,Any]],Dict[str,Dict[Any,Dict[str,Any]]]: Structured data containing the results of the execution and the archived results.
        """
        if self.DEBUG:
            print("Fetching All Results...")
        return self.get_results(), self.get_archive()

    def archive_results(self) -> bool:
        """Move the RuntimeResults to the RuntimeArchive.

        Returns:
            NoReturn: No Return.
        """
        if self.DEBUG:
            print("Archiving Results...")
        try:
            self.__move_results_to_archive__()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def next(self) -> bool:
        if self.DEBUG:
            print("Moving to next task...")

        if self.__has_pending_results__():
            print("Pending results found. Continuing to next task.")

        try:
            if self.AutoArchive:
                self.__move_results_to_archive__()
            self.RuntimeResults = self.__setup_RuntimeResults__()

        except Exception as e:
            print(f"Error: {e}")
            return False
        return True
