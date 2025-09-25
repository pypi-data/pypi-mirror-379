"""LangGraph tools for MLflow interactions."""
import json
import logging
import sys
from datetime import datetime

import mlflow
from langchain_core.tools import tool
from mlflow_assistant.core.connection import MLflowConnection
from mlflow_assistant.engine.definitions import MLFLOW_MAX_RESULTS, NA, TIME_FORMAT
from mlflow_assistant.utils.config import get_mlflow_uri

logger = logging.getLogger("mlflow_assistant.enngine.tools")


class MLflowTools:
    """Collection of helper utilities for MLflow interactions."""

    @staticmethod
    def format_timestamp(timestamp_ms: int) -> str:
        """Convert a millisecond timestamp to a human-readable string."""
        if not timestamp_ms:
            return NA
        dt = datetime.fromtimestamp(timestamp_ms / 1000.0)
        return dt.strftime(TIME_FORMAT)


# Get MLflow client
mlflow_connection = MLflowConnection(tracking_uri=get_mlflow_uri())
mlflow_connection.connect()
client = mlflow_connection.get_client()


@tool
def list_models(name_contains: str = "", max_results: int = MLFLOW_MAX_RESULTS) -> str:
    """List all registered models in the MLflow model registry, with optional filtering.

    Args:
        name_contains: Optional filter to only include models whose names contain this string
        max_results: Maximum number of results to return (default: 100)

    Returns:
        A JSON string containing all registered models matching the criteria.

    """
    logger.debug(
        f"Fetching registered models (filter: '{name_contains}', max: {max_results})",
    )

    try:
        # Get all registered models
        registered_models = client.search_registered_models(max_results=max_results)

        # Filter by name if specified
        if name_contains:
            registered_models = [
                model
                for model in registered_models
                if name_contains.lower() in model.name.lower()
            ]

        # Create a list to hold model information
        models_info = []

        # Extract relevant information for each model
        for model in registered_models:
            model_info = {
                "name": model.name,
                "creation_timestamp": MLflowTools.format_timestamp(
                    model.creation_timestamp,
                ),
                "last_updated_timestamp": MLflowTools.format_timestamp(
                    model.last_updated_timestamp,
                ),
                "description": model.description or "",
                "tags": {tag.key: tag.value for tag in model.tags}
                if hasattr(model, "tags")
                else {},
                "latest_versions": [],
            }

            # Add the latest versions if available
            if model.latest_versions and len(model.latest_versions) > 0:
                for version in model.latest_versions:
                    version_info = {
                        "version": version.version,
                        "status": version.status,
                        "stage": version.current_stage,
                        "creation_timestamp": MLflowTools.format_timestamp(
                            version.creation_timestamp,
                        ),
                        "run_id": version.run_id,
                    }
                    model_info["latest_versions"].append(version_info)

            models_info.append(model_info)

        result = {"total_models": len(models_info), "models": models_info}

        return json.dumps(result, indent=2)

    except Exception as e:
        error_msg = f"Error listing models: {e!s}"
        logger.error(error_msg, exc_info=True)
        return json.dumps({"error": error_msg})


@tool
def list_experiments(
    name_contains: str = "", max_results: int = MLFLOW_MAX_RESULTS,
) -> str:
    """List all experiments in the MLflow tracking server, with optional filtering.

    Args:
        name_contains: Optional filter to only include experiments whose names contain this string
        max_results: Maximum number of results to return (default: 100)

    Returns:
        A JSON string containing all experiments matching the criteria.

    """
    logger.debug(f"Fetching experiments (filter: '{name_contains}', max: {max_results})")

    try:
        # Get all experiments
        experiments = client.search_experiments()

        # Filter by name if specified
        if name_contains:
            experiments = [
                exp for exp in experiments if name_contains.lower() in exp.name.lower()
            ]

        # Limit to max_results
        experiments = experiments[:max_results]

        # Create a list to hold experiment information
        experiments_info = []

        # Extract relevant information for each experiment
        for exp in experiments:
            exp_info = {
                "experiment_id": exp.experiment_id,
                "name": exp.name,
                "artifact_location": exp.artifact_location,
                "lifecycle_stage": exp.lifecycle_stage,
                "creation_time": MLflowTools.format_timestamp(exp.creation_time)
                if hasattr(exp, "creation_time")
                else None,
                "tags": {tag.key: tag.value for tag in exp.tags}
                if hasattr(exp, "tags")
                else {},
            }

            # Get the run count for this experiment
            try:
                runs = client.search_runs(
                    experiment_ids=[exp.experiment_id], max_results=1,
                )
                if runs:
                    # Just get the count of runs, not the actual runs
                    run_count = client.search_runs(
                        experiment_ids=[exp.experiment_id], max_results=1000,
                    )
                    exp_info["run_count"] = len(run_count)
                else:
                    exp_info["run_count"] = 0
            except Exception as e:
                logger.warning(
                    f"Error getting run count for experiment {exp.experiment_id}: {e!s}",
                )
                exp_info["run_count"] = "Error getting count"

            experiments_info.append(exp_info)

        result = {
            "total_experiments": len(experiments_info),
            "experiments": experiments_info,
        }

        return json.dumps(result, indent=2)

    except Exception as e:
        error_msg = f"Error listing experiments: {e!s}"
        logger.error(error_msg, exc_info=True)
        return json.dumps({"error": error_msg})


@tool
def get_model_details(model_name: str) -> str:
    """Get detailed information about a specific registered model.

    Args:
        model_name: The name of the registered model

    Returns:
        A JSON string containing detailed information about the model.

    """
    logger.debug(f"Fetching details for model: {model_name}")

    try:
        # Get the registered model
        model = client.get_registered_model(model_name)

        model_info = {
            "name": model.name,
            "creation_timestamp": MLflowTools.format_timestamp(
                model.creation_timestamp,
            ),
            "last_updated_timestamp": MLflowTools.format_timestamp(
                model.last_updated_timestamp,
            ),
            "description": model.description or "",
            "tags": {tag.key: tag.value for tag in model.tags}
            if hasattr(model, "tags")
            else {},
            "versions": [],
        }

        # Get all versions for this model
        versions = client.search_model_versions(f"name='{model_name}'")

        for version in versions:
            version_info = {
                "version": version.version,
                "status": version.status,
                "stage": version.current_stage,
                "creation_timestamp": MLflowTools.format_timestamp(
                    version.creation_timestamp,
                ),
                "source": version.source,
                "run_id": version.run_id,
            }

            # Get additional information about the run if available
            if version.run_id:
                try:
                    run = client.get_run(version.run_id)
                    # Extract only essential run information to avoid serialization issues
                    run_metrics = {}
                    for k, v in run.data.metrics.items():
                        try:
                            run_metrics[k] = float(v)
                        except ValueError:
                            run_metrics[k] = str(v)

                    version_info["run"] = {
                        "status": run.info.status,
                        "start_time": MLflowTools.format_timestamp(
                            run.info.start_time,
                        ),
                        "end_time": MLflowTools.format_timestamp(run.info.end_time)
                        if run.info.end_time
                        else None,
                        "metrics": run_metrics,
                    }
                except Exception as e:
                    logger.warning(
                        f"Error getting run details for {version.run_id}: {e!s}",
                    )
                    version_info["run"] = "Error retrieving run details"

            model_info["versions"].append(version_info)

        return json.dumps(model_info, indent=2)

    except Exception as e:
        error_msg = f"Error getting model details: {e!s}"
        logger.error(error_msg, exc_info=True)
        return json.dumps({"error": error_msg})


@tool
def get_system_info() -> str:
    """Get information about the MLflow tracking server and system.

    Returns:
        A JSON string containing system information.

    """
    logger.debug("Getting MLflow system information")

    try:
        info = {
            "mlflow_version": mlflow.__version__,
            "tracking_uri": mlflow.get_tracking_uri(),
            "registry_uri": mlflow.get_registry_uri(),
            "artifact_uri": mlflow.get_artifact_uri(),
            "python_version": sys.version,
            "server_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        # Get experiment count
        try:
            experiments = client.search_experiments()
            info["experiment_count"] = len(experiments)
        except Exception as e:
            logger.warning(f"Error getting experiment count: {e!s}")
            info["experiment_count"] = "Error retrieving count"

        # Get model count
        try:
            models = client.search_registered_models()
            info["model_count"] = len(models)
        except Exception as e:
            logger.warning(f"Error getting model count: {e!s}")
            info["model_count"] = "Error retrieving count"

        # Get active run count
        try:
            active_runs = 0
            for exp in experiments:
                runs = client.search_runs(
                    experiment_ids=[exp.experiment_id],
                    filter_string="attributes.status = 'RUNNING'",
                    max_results=1000,
                )
                active_runs += len(runs)

            info["active_runs"] = active_runs
        except Exception as e:
            logger.warning(f"Error getting active run count: {e!s}")
            info["active_runs"] = "Error retrieving count"

        return json.dumps(info, indent=2)

    except Exception as e:
        error_msg = f"Error getting system info: {e!s}"
        logger.error(error_msg, exc_info=True)
        return json.dumps({"error": error_msg})
