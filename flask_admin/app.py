# -*- coding: utf-8 -*-
# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)

'''
flask db init
flask db migrate
flask db upgrade
'''


def create_app():
    from flask_admin.views.auth import auth_bp

    app.register_blueprint(auth_bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
