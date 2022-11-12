import yaml


def load_yaml(file_path, encoding='utf-8'):
    with open(file_path, "r", encoding=encoding) as file:
        configs = yaml.safe_load(file)

    return configs
