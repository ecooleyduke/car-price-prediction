import yaml

def load_config(path="config.yaml"):
    return yaml.safe_load(open(path))