from embedl_hub.cli.init import _read_ctx
from embedl_hub.core.context import experiment_context
from embedl_hub.tracking import (
    RunType,
    log_metric,
    log_param,
    set_experiment,
    set_project,
)
from embedl_hub.tracking.client import BASE_URL_ENV_VAR_NAME

BASE_URL_ENV_VAR_NAME = "http://localhost:5173/"

ctx = _read_ctx()

with experiment_context(
    project_name=ctx["project_name"],
    experiment_name=ctx["experiment_name"],
    run_type=RunType.TUNE,
):

    print("hi from inside the experiment context")
