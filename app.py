import os

from flask import Flask


def create_app(testing=False):
    app = Flask(__name__)

    ## Initialize Config
    app.config.from_pyfile("config.py")
    os.environ["TESTING"] = str(testing)

    from api.routes.rates import rates_api

    app.register_blueprint(rates_api, url_prefix="/rates")

    return app


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument(
        "-p", "--port", default=5000, type=int, help="port to listen on"
    )
    args = parser.parse_args()
    port = args.port

    app = create_app()
    app.run(host="0.0.0.0", port=port)
