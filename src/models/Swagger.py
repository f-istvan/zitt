from typing import Dict, Any


class Swagger:

    def __init__(self, swagger_src: Dict[str, Any]) -> None:
        # create class paths
        self.paths: Dict[str, Dict] = swagger_src['paths']
