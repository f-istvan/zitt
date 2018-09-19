from typing import Dict, Any


class Method:

    def __init__(self, path: str, method_name: str, method_config: Dict[str, Any]) -> None:
        self.path = path
        self.method_name: str = method_name
        self.method_config = method_config
