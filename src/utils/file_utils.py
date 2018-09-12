import yaml
from typing import Dict, Any


def read_file(path: str) -> Dict[Any, str]:
    result: Dict[Any, str] = {}
    with open(path, 'r') as stream:
        try:
            result = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return result
