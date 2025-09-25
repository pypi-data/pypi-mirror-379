import argparse

from alpss.alpss_watcher import Watcher
from alpss.alpss_main import alpss_main
import os
import json
import logging
import sys

def start_watcher():
    w = Watcher()
    w.run()

def load_json_config(config):
    """Load configuration from a JSON file or return directly if it's already a dictionary."""
    if isinstance(config, dict):
        return config  # If already a dictionary, return it

    if isinstance(config, str) and os.path.exists(config):
        with open(config, "r") as file:
            return json.load(file)  # Load JSON directly

    raise ValueError(
        "Invalid config input: Provide a dictionary or a valid JSON file path."
    )

def alpss_main_with_config(config=None):
    """
    Run ALPSS with a given JSON configuration.

    Args:
        config (str or dict, optional): JSON config file, either given as parsable argument through CLI or directly as a string, or a dictionary containing config parameters.
    """

    if config is None: 
        # If called from CLI, parse arguments
        parser = argparse.ArgumentParser(
            description="Run ALPSS using a JSON config file"
        )
        parser.add_argument(
            "config_path", type=str, help="Path to the JSON configuration file"
        )
        args = parser.parse_args()
        config = load_json_config(args.config_path)

    # Load the dictionary or YAML config
    else:
        config = load_json_config(config)

    # Run ALPSS with the loaded config
    return alpss_main(**config)

def alpss_cli():
    """
    Entry point for console_scripts.
    Always uses sys.argv so `alpss /path/to/config.json` works.
    """
    try:
        sys.exit(alpss_main_with_config())
    except Exception as e:
        print(f"[ALPSS ERROR] {e}", file=sys.stderr)
        sys.exit(1)