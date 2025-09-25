import os
import json

CONFIG_DIR = os.path.join(os.path.expanduser("~"), ".dvpy")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")


def save_config(conf_path: str = None, folder_id: str = None):
    """Save service account path and/or folder ID into config file."""
    os.makedirs(CONFIG_DIR, exist_ok=True)

    # Load existing config if it exists
    config = {}
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE) as f:
                config = json.load(f)
        except json.JSONDecodeError:
            config = {}

    # Update values if provided
    if conf_path:
        config["conf_path"] = conf_path
    if folder_id:
        config["folder_id"] = folder_id

    # Save back
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)

def load_conf_path(value) -> str | None:
    """Load the saved service account JSON path."""
    if not os.path.exists(CONFIG_FILE):
        return None
    try:
        with open(CONFIG_FILE) as f:
            data = json.load(f)
        if value == "conf_path":
            return data.get("conf_path")
        elif value == "folder_id":
            return data.get("folder_id")
    except (json.JSONDecodeError, KeyError):
        return None


