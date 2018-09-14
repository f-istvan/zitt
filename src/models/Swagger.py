from typing import Dict, Any, List

from models.Path import Path


class Swagger:

    def __init__(self, swagger_src: Dict[str, Any]) -> None:
        self.paths: List[Path] = []
        for path, method in swagger_src['paths'].items():
            path_to_add = Path(path, method)
            self.paths.append(path_to_add)
