from models.Swagger import Swagger

from flask import Flask


from jinja2.nativetypes import NativeEnvironment

def build_server(swagger: Swagger):

    app = Flask(__name__)

    func_template = """
@app.route('{{ path_name }}')
def func{{ func_postfix }}(): 
    {{ func_body }}
"""

    env = NativeEnvironment()

    func_body = 'return "ok"'

    paths = swagger.paths
    for i in range(len(paths)):
                    # 1 commit + push
                    # 2 rename this path
        p = paths[i].path
        result = env.from_string(func_template).render(path_name=p, func_postfix=i, func_body=func_body)
        print(result)
        exec(result)

    return app


def run_server(app):
    app.run()

