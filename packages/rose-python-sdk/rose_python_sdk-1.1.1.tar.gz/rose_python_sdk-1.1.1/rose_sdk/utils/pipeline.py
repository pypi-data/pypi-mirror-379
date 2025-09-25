"""
Pipeline builder utilities for the Rose Python SDK.
"""

from typing import Dict, Any, List, Set

# Datetime import removed


# Supported scenarios from the pipeline deployer
SUPPORTED_SCENARIOS: Dict[str, Dict[str, Any]] = {
    "realtime_leaderboard": {
        "dataset_keys": {"interaction", "metadata"},
        "description": "Realtime leaderboard pipeline for item ranking and user favorites",
    },
}


class PipelineBuilder:
    """
    Builder for creating pipeline configurations with intuitive API.

    The PipelineBuilder provides a fluent interface for creating recommendation
    pipelines. It handles the complexity of dataset mapping and ensures that
    all required datasets for a given scenario are properly configured.

    Args:
        pipeline_name: Name of the pipeline
        scenario: Pipeline scenario (e.g., 'realtime_leaderboard')
        account_id: The account ID for the pipeline (optional, will be derived from access token)

    Example:
        >>> builder = PipelineBuilder("recommendation-pipeline", "realtime_leaderboard")
        >>> pipeline_config = (builder
        ...     .add_dataset("interaction-log", "interaction_dataset_123")
        ...     .add_dataset("item-metadata", "metadata_dataset_456")
        ...     .set_custom_property("custom_param", "value")
        ...     .build())
        >>>
        >>> # Use with client
        >>> pipeline = client.pipelines.create(**pipeline_config)

    Note:
        - Each scenario requires specific dataset keys
        - Use get_supported_scenarios() to see available scenarios and their requirements
        - The builder validates that all required datasets are provided before building
    """

    def __init__(self, pipeline_name: str, scenario: str, account_id: str = ""):
        self.pipeline_name = pipeline_name

        if scenario not in SUPPORTED_SCENARIOS:
            raise ValueError(f"Unsupported scenario: {scenario}. Supported scenarios: {list(SUPPORTED_SCENARIOS.keys())}")

        self.scenario = scenario
        self.scenario_config = SUPPORTED_SCENARIOS[scenario]

        # Initialize with minimal required properties
        self.properties: Dict[str, Any] = {"datasets": {}, "scenario": scenario}

    def add_dataset(self, dataset_key: str, dataset_id: str) -> "PipelineBuilder":
        """
        Add a dataset mapping to the pipeline configuration.

        Maps a pipeline-defined dataset key to a user-created dataset ID.
        The dataset_key is defined by the pipeline scenario, while dataset_id
        is the actual ID of a dataset created by the user.

        Args:
            dataset_key: Pipeline-defined key (e.g., 'interaction', 'metadata')
            dataset_id: User-created dataset ID (e.g., 'AHgyJijrQ5GPnHZgKE_Hgg')

        Returns:
            Self for method chaining

        Example:
            >>> builder = PipelineBuilder("account", "pipeline", "realtime_leaderboard")
            >>> builder.add_dataset("interaction-log", "interaction_dataset_123")
            >>> builder.add_dataset("item-metadata", "metadata_dataset_456")

        Note:
            - Use get_supported_scenarios() to see required dataset keys for each scenario
            - The builder will validate that all required datasets are provided
        """
        if dataset_key not in self.scenario_config["dataset_keys"]:
            raise ValueError(
                f"Dataset key '{dataset_key}' not supported for scenario '{self.scenario}'. "
                f"Supported dataset keys: {self.scenario_config['dataset_keys']}"
            )

        datasets = self.properties["datasets"]
        if not isinstance(datasets, dict):
            datasets = {}
            self.properties["datasets"] = datasets
        datasets[dataset_key] = dataset_id
        return self

    def set_custom_property(self, key: str, value: Any) -> "PipelineBuilder":
        """Set a custom property (overrides default service properties)."""
        self.properties[key] = value
        return self

    def get_scenario_info(self) -> Dict[str, Any]:
        """Get information about the current scenario."""
        return {
            "scenario": self.scenario,
            "description": self.scenario_config["description"],
            "required_dataset_keys": list(self.scenario_config["dataset_keys"]),
        }

    def get_dataset_mapping(self) -> Dict[str, str]:
        """Get the current dataset mapping (dataset_key -> dataset_id)."""
        datasets = self.properties["datasets"]
        if isinstance(datasets, dict):
            return dict(datasets)
        return {}

    def is_dataset_mapping_complete(self) -> bool:
        """Check if all required dataset keys are mapped to dataset IDs."""
        required_keys: Set[str] = self.scenario_config["dataset_keys"]
        datasets = self.properties["datasets"]
        if isinstance(datasets, dict):
            mapped_keys = set(datasets.keys())
        else:
            mapped_keys = set()
        return required_keys.issubset(mapped_keys)

    def get_missing_dataset_keys(self) -> List[str]:
        """Get list of dataset keys that still need to be mapped."""
        required_keys: Set[str] = self.scenario_config["dataset_keys"]
        datasets = self.properties["datasets"]
        if isinstance(datasets, dict):
            mapped_keys = set(datasets.keys())
        else:
            mapped_keys = set()
        return list(required_keys - mapped_keys)

    def build(self) -> Dict[str, Any]:
        """Build the pipeline configuration."""
        return {"pipeline_name": self.pipeline_name, "properties": self.properties}


def create_realtime_leaderboard_pipeline(
    account_id: str, pipeline_name: str, interaction_dataset_id: str, metadata_dataset_id: str
) -> Dict[str, Any]:
    """
    Create a realtime leaderboard pipeline configuration.

    Args:
        account_id: The account ID
        pipeline_name: The pipeline name
        interaction_dataset_id: The interaction dataset ID
        metadata_dataset_id: The metadata dataset ID

    Returns:
        Pipeline configuration dictionary
    """
    return (
        PipelineBuilder(pipeline_name, scenario="realtime_leaderboard", account_id=account_id)
        .add_dataset("interaction", interaction_dataset_id)
        .add_dataset("metadata", metadata_dataset_id)
        .build()
    )


def create_pipeline(pipeline_name: str, scenario: str, dataset_mapping: Dict[str, str], **kwargs) -> Dict[str, Any]:
    """
    Create a pipeline configuration with minimal configuration.

    Args:
        pipeline_name: The pipeline name
        scenario: The pipeline scenario (realtime_leaderboard)
        dataset_mapping: Dictionary mapping dataset keys to dataset names
                        e.g., {"interaction": "user_dataset_123", "metadata": "user_dataset_456"}
        **kwargs: Additional configuration parameters (optional)

    Returns:
        Pipeline configuration dictionary
    """
    # Account ID will be derived from the access token when creating the pipeline
    builder = PipelineBuilder(pipeline_name, scenario)

    # Add datasets
    for dataset_key, dataset_name in dataset_mapping.items():
        builder.add_dataset(dataset_key, dataset_name)

    # Apply custom configurations if provided
    for key, value in kwargs.items():
        if hasattr(builder, key):
            getattr(builder, key)(value)
        else:
            builder.set_custom_property(key, value)

    return builder.build()


def create_custom_pipeline(pipeline_name: str, scenario: str, datasets: Dict[str, str], **kwargs) -> Dict[str, Any]:
    """
    Create a custom pipeline configuration (alias for create_pipeline).

    Args:
        pipeline_name: The pipeline name
        scenario: The pipeline scenario (realtime_leaderboard)
        datasets: Dictionary mapping dataset names to dataset IDs
        **kwargs: Additional configuration parameters

    Returns:
        Pipeline configuration dictionary
    """
    return create_pipeline(pipeline_name, scenario, datasets, **kwargs)


def get_supported_scenarios() -> Dict[str, Dict[str, Any]]:
    """
    Get information about all supported scenarios.

    Returns:
        Dictionary of scenario information
    """
    return SUPPORTED_SCENARIOS.copy()
