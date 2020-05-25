# encoding: utf-8

import os
from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    from app.blueprints import company_bp

    app.register_blueprint(company_bp, url_prefix="/company")

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
