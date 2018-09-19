from utils.file_utils import read_file
from utils.server_utils import build_server, run_server
from typing import Dict, Any

from models.Swagger import Swagger


def main() -> None:
    file_path: str = 'resources/petstore.swagger.yml'
    swagger_src: Dict[str, Any] = read_file(file_path)

    swagger: Swagger = Swagger(swagger_src)
    server = build_server(swagger)
    # run_server(server)


# execute only as a program
# do not execute when the module is imported
if __name__ == "__main__":
    main()
