import yaml
from pathlib import Path

def load_yaml_data(filepath):
    with open(Path(filepath), encoding='utf-8') as file:
        return yaml.safe_load(file)
