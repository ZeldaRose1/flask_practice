#!/bin/bash

import os

from flask import Flask

def create_app(test_config=None):
    # Createand configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY='dev'  # This should be randomized on production run
            DATABASE=os.path.join(app.instance_path, 'main'),
        )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

        # Ensure the instance folder exists
        try:
            os.makedir(app.instance_path)
        except OSError:
            pass

        # A simple page that says hello
        @app.route('/hello')
        def hello():
            return "Hello, World!"

        return app

if __name__ == '__main__':
    print('hello')
