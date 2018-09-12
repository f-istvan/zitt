from utils.file_utils import read_file
from typing import Dict, Any

from models.Swagger import Swagger


def main() -> None:
    file_path: str = 'resources/petstore.swagger.yml'
    swagger_src: Dict[str, Any] = read_file(file_path)

    swagger: Swagger = Swagger(swagger_src)


# execute only as a program
# do not execute when the module is imported
if __name__ == "__main__":
    main()
