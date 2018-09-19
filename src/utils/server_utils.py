from models.Swagger import Swagger

from flask import Flask


from jinja2.nativetypes import NativeEnvironment

def build_server(swagger: Swagger):
    for method in swagger.methods:
        print(f'{method.path}, {method.method_name}')

        def flaskify_path_param(path) -> None:
            path = path.replace('{', '<')
            path = path.replace('}', '>')
            return path

        path = flaskify_path_param(method.path)

        endpoint = f'@app.route("{path}, methods=[\'{method.method_name.upper()}\']")'
        print(endpoint)
    return temp(swagger)

def run_server(app):
    print(app.url_map)
    app.run()


def temp(swagger):
    app = Flask(__name__)

    func_template = """
{{ endpoint }}
def func{{ func_postfix }}():
    {{ func_body }}
"""

    env = NativeEnvironment()

    func_body = 'return "ok"'

    i: int = 0
    for method in swagger.methods:
        i = i + 1
        endpoint = f'@app.route("{method.path}, methods=[\'{method.method_name.upper()}\']")'
        result = env.from_string(func_template).render(endpoint=endpoint, func_postfix=i, func_body=func_body)
        #print(result)
        exec(result)

    return app
