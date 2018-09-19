from typing import Dict, Any, List

from models.Method import Method


class Swagger:

    def __init__(self, swagger_src: Dict[str, Any]) -> None:
        self.methods: List[Method] = []
        for path, method in swagger_src['paths'].items():
            for method_name in method:
                method_config: Dict[str, Any] = method[method_name]
                method_to_add: Method = Method(path, method_name, method_config)
                self.methods.append(method_to_add)