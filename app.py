from flask import Flask, render_template
from flask_restx import Api

from configs.config import Config
from configs.setup_db import db

from views.auth import auth_ns
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns
from views.users import user_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)

    with app.app_context():
        db.create_all()


app = create_app(Config())
app.debug = True


if __name__ == '__main__':
    # create_app().run()
    app.run(host="localhost", port=5000, debug=True)

