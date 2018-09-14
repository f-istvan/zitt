from typing import Dict, Any, List


class Path:

    def __init__(self, path: str, method: Dict[str, Any]) -> None:
        self.path: str = path
        self.method = method
