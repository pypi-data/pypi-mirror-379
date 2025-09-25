from functools import lru_cache


def load_yaml(name: str) -> dict:
    """Load YAML file

    :param name: File name
    :return: Dictionary of config data
    """
    import yaml

    with open(file=name) as f:
        config = yaml.safe_load(f)

    return config


@lru_cache
def default_config() -> dict:
    """Load default SonusAI config

    :return: Dictionary of default config data
    """
    from .constants import DEFAULT_CONFIG

    try:
        return load_yaml(DEFAULT_CONFIG)
    except Exception as e:
        raise OSError(f"Error loading default config: {e}") from e


def _update_config_from_file(filename: str, given_config: dict) -> dict:
    """Update the given config with the config in the specified YAML file

    :param filename: File name
    :param given_config: Config dictionary to update
    :return: Updated config dictionary
    """
    from copy import deepcopy

    updated_config = deepcopy(given_config)

    try:
        file_config = load_yaml(filename)
    except Exception as e:
        raise OSError(f"Error loading config from {filename}: {e}") from e

    # Use default config as base and overwrite with given config keys as found
    if file_config:
        updated_config.update(file_config)

    return updated_config


def load_config(name: str) -> dict:
    """Load the SonusAI default config and update with the given location (performing SonusAI variable substitution)

    :param name: Directory containing mixture database
    :return: Dictionary of config data
    """
    from os.path import join

    from sonusai.config.asr import validate_asr_configs
    from sonusai.config.source import update_sources
    from sonusai.config.truth import validate_truth_configs

    config = _update_config_from_file(filename=join(name, "config.yml"), given_config=default_config())
    config = update_sources(config)
    validate_asr_configs(config)
    validate_truth_configs(config)
    return config
