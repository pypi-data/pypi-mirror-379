from typing import Optional, Any
from .requestor import Requestor
from .study import Study
from .benchmark import Benchmark
from .drivers import Driver
from .version import __version__
from . import drivers


class Client(Requestor):

    """
    This class provides methods for creating new optimization studies. Example::

       client = Client("http://localhost:4554")
       design_space = [
          {'name': 'x1', 'type': 'continuous', 'domain': (-1.5,1.5)},
          {'name': 'x2', 'type': 'continuous', 'domain': (-1.5,1.5)},
       ]
       study = client.create_study(design_space=design_space, name='example')

    Args:
      host: The host name under which the optimization server can be contacted.
        For example, ``'http://localhost:4554'``
      verbose: If true, messages from the optimization server are printed out.
      check: If true, check if the optimization server can be contacted
        via the given host name.
    """

    def __init__(self, host: str, verbose: bool = True, check: bool = True) -> None:
        super(Client, self).__init__(host=host, verbose=verbose)
        if check:
            self.check_server()

    def check_server(self) -> None:
        """Checks if the optimization server is running and if it is compatible to the client.
        Example::

            >>> client.check_server()
            Polling server at http://localhost:4554
            Optimization server is running

        """
        self.inform(f"Polling server at {self.host}")
        answer = self.get("check server")
        optimizer_version = str(answer["version"])
        if optimizer_version != __version__:
            self.warn(
                f"Version mismatch between Python client ({__version__}) "
                f"and optimization server ({optimizer_version}). "
                "This can lead to undefined behavior. "
                "Consider upgrading the "
                f"{'client' if __version__ < optimizer_version else 'server'}."
            )

        self.inform(answer["message"])

    def shutdown_server(self, force: bool = False) -> None:
        """Shuts down the optimization server. Example::

           client.shutdown_server()

        Args:
          force: If true, the optimization server is closed even if a study
            is not yet finished.

        """
        self.post("shutdown server", "server", "shutdown", data={"force": force})
        self.inform(f"Server at {self.host} is shutting down.")

    def create_study(
        self,
        design_space: Optional[list[dict[str, Any]]] = None,
        environment: Optional[list[dict[str, Any]]] = None,
        constraints: Optional[list[dict[str, Any]]] = None,
        name: Optional[str] = None,
        study_id: Optional[str] = None,
        driver: str = "ActiveLearning",
        save_dir: Optional[str] = None,
        output_precision: float = 1e-10,
        dashboard: bool = True,
        open_browser: bool = True,
        **kwargs: Any,
    ) -> Study:
        """Creates a new :class:`~jcmoptimizer.Study` instance. Example::

            study = client.create_study(
                design_space=design_space,
                name='example',
                study_id="example_01"
            )

        Args:
          design_space: List of domain definitions for each parameter. A design space
            definition consists of a list of dictionary with the entries

            :name: Name of the parameter. E.g. ``'x1'``. The name should contain
                no spaces and must not be equal to function names or mathematical
                constants like ``'sin'``, ``'cos'``, ``'exp'``, ``'pi'`` etc.
            :type: Type of the parameter. Either ``'continuous'``, ``'discrete'``,
                or ``'categorial'``.
            :domain: The domain of the parameter. For continuous parameters this
                is a tuple (min, max). For discrete parameters this is a list
                of values, e.g. ``[1.0,2.5,3.0]``. For categorial inputs it is a list
                of strings, e.g. ``['cat1','cat2','cat3']``. Note, that categorial
                values are internally mapped to integer representations, which
                are allowed to have a correlation. The categorial values should
                therefore be ordered according to their similarity.
                For fixed parameters the domain is a single parameter value.

            Example::

                 design_space = [
                     {'name': 'x1', 'type': 'continuous', 'domain': (-2.0,2.0)},
                     {'name': 'x2', 'type': 'continuous', 'domain': (-2.0,2.0)},
                     {'name': 'x3', 'type': 'discrete', 'domain': [-1.0,0.0,1.0]},
                     {'name': 'x4', 'type': 'categorial', 'domain': ['a','b']}
                 ]

            If not specified, the design space configuration from the study history
            is used. If no historic information exists, an error is raised.

          environment: Environment parameters are those which influence the
            behaviour of the system, but are not design parameters.
            Examples are uncontrollable environment parameters (e.g. temperature, time)
            or parameters that are scanned in each evaluation (e.g. wavelength, angle)
            for each run of the system can be described by environment parameters.
            Alternatively, scans can be described by surrogates that are trained on multiple
            inputs (one for each scan value). The environment definition consists of a
            list of dictionary with the entries:

            :name: Name of the parameter. E.g. ``'x1'``. The name should contain
                no spaces and must not be equal to function names or mathematical
                constants like ``'sin'``, ``'cos'``, ``'exp'``, ``'pi'`` etc.
            :type: Type of the parameter. Either ``'variable'`` or ``'fixed'``.
                Fixed parameters can be used in the constraint functions or other
                expressions.
            :domain: The domain of the parameter. For fixed parameters, this is a
                single value, for variable parameters this can be a tuple
                (min, max).  If no bounds are specified
                for variable parameters, the environment is considered to be
                unconstrained. In this case the scale has to be set.
            :scale: The scale at which environment parameter
                changes affect the system. If the environment parameter
                describes unknown drifts and aging effects, the length scale
                is equal to the timescale at which the system behaviour
                changes due to drifts or aging.

            Example::

                environment = [
                    {'name': 'wavelength', 'type': 'continuous', 'domain': (300, 600)},
                    {'name': 'time', 'type': 'continuous', 'scale': 0.1},
                    {'name': 'radius', 'type': 'fixed', 'domain': 1.5}
                ]

            If not specified, the environment configuration from the study history
            is used. If no historic information exists, the environment is
            assumed to be empty (``environment = []``).

          constraints: List of constraints on the design space. Each list element is a
            dictionary with the entries

            :name: Name of the constraint.
            :constraint: A string defining an inequality constraint in the
                for `a <= b` or `a >= b`.
                The following operations and functions may be for example used:
                +,-,*,/,^,sqrt,sin,cos,tan,exp,log,log10,abs,round,sign,trunc.
                E.g. ``'x1^2 + x2^2 <= sin(x1+x2)'``.
                For a more complete list of supported functions,
                see the :ref:`expression variable reference
                <ActiveLearning.Expression.expression>`.

            Example::

                constraints = [
                    {'name': 'circle', 'expression': 'x1^2 + x2^2 <= radius^2'},
                    {'name': 'triangle', 'expression': 'x1 >= x2'},
                ]

            If not specified, the constraints configuration from the study history
            is used. If no historic information exists, the list of constraints is
            assumed to be empty (``constraints = []``).

          study_id: A unique identifier of the study. All relevant information on
            the study are saved in a file named study_id+'.jcmo'
            If the study already exists, the ``design_space``, ``environment``, and
            ``constraints`` do not need to be provided. If not set, the study_id is set to
            a random unique string.

          name: The name of the study that will be shown in the dashboard.

          save_dir: The path to a directory, where the study file (jcmo-file)
            is saved. Default is a directory in the system's temporary directory.

          driver: Driver used for the study. Default is 'ActiveLearning'.
            For a list of drivers, see the :ref:`driver reference <DriverReference>`.

          output_precision: Precision level for output of parameters.

            .. note:: Rounding the output can potentially lead to a slight
               breaking of constraints.

          dashboard: If true, a dashboard will be served for the study.

          open_browser: If true, a browser window with the dashboard is started.

        """

        if "domain" in kwargs:
            raise ValueError(
                "The 'domain' argument is deprecated. "
                "Please use the 'design_space' argument instead."
            )

        answer = self.post(
            "create study",
            "study",
            "create",
            data={
                "study_id": study_id,
                "name": name,
                "design_space": design_space,
                "environment": environment,
                "constraints": constraints,
                "driver": driver,
                "save_dir": save_dir,
                "output_precision": output_precision,
                "dashboard": dashboard,
                "open_browser": open_browser,
            },
        )

        driver_class: type[Driver] = getattr(drivers, driver)
        driver_instance = driver_class(
            study_id=answer["study_id"], host=self.host, session=self.session
        )

        study = Study(
            study_id=answer["study_id"],
            host=self.host,
            session=self.session,
            driver=driver_instance,
        )

        if answer["dashboard_path"]:
            self.inform(
                f"The dashboard is accessible via {self.host}/{answer['dashboard_path']}"
            )

        return study

    def create_benchmark(
        self,
        benchmark_id: Optional[str] = None,
        num_average: int = 6,
        remove_completed_studies: bool = False,
    ) -> Benchmark:
        """Creates a new :class:`~jcmoptimizer.Benchmark` object for benchmarking
        different optimization studies against each other. Example::

            benchmark = client.create_benchmark(num_average=6)

        Args:
          benchmark_id: A unique identifier of the benchmark.
          num_average: Number of study runs to determine average
            study performance
          remove_completed_studies: If true, studies that are completed
            (i.e. some stopping criterion was met) are removed from the server
            as long as no other client holds a handle to the study.
        """

        answer = self.post(
            "create benchmark",
            "benchmark",
            "create",
            data={
                "benchmark_id": benchmark_id,
                "num_average": num_average,
                "remove_completed_studies": remove_completed_studies,
            },
        )

        benchmark = Benchmark(
            benchmark_id=answer["benchmark_id"],
            num_average=num_average,
            host=self.host,
            session=self.session,
        )
        return benchmark

    def _get_drivers(self) -> tuple[dict[str, str], str]:
        out = self.post("get available drivers", "server", "get_drivers", data={})
        return out["drivers"]

    def _get_driver_config_rsts(
        self,
        driver_name: str,
        language: str,
    ) -> tuple[str, dict[str, str]]:
        out = self.post(
            "get driver rst info",
            "server",
            "get_driver_config_rsts",
            data={
                "driver_name": driver_name,
                "language": language,
            },
        )
        return out["config_rst"], out["submodule_config_rst_dict"]
