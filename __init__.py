import os

from flask import Flask
import input



# Create and configure an instance of the Flask application
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.DevConfig')


# Defining Global Constants
HOST = app.config['HOST']
PORT = app.config['PORT']
FLASK_ENV = app.config['FLASK_ENV']
DEBUG = app.config['DEBUG']
TESTING = app.config['TESTING']
TEMPLATES_AUTO_RELOAD = app.config["TEMPLATES_AUTO_RELOAD"]


@app.route("/")
def index():
    return "Hello, Your Server is up and running!"

# apply the blueprints to the app
app.register_blueprint(input.bp)
app.add_url_rule("/", endpoint="index")

app.run(HOST,PORT)
