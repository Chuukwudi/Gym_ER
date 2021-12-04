import os

from flask import Flask
from flask import render_template
import logging



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

####################################################################
# Routing details - URL routing seen on client browser
####################################################################

@app.route("/")
def index():
    return render_template("input.html")

@app.route("/result", methods=['POST', 'GET'])
def result():
    return render_template("result.html")

##############################################################################
# Main Application: Execution of FreedomOfSearch Application starts from here. 
##############################################################################


if(__name__ == "__main__"):
    
    # defining the log and application configurations 
    logging.basicConfig(filename='Logs/app.log', level=logging.INFO)
    logging.info('info_app -- executing main()')
    logging.info('info_app -- invoking server 127.0.0.1, port = 5000')
    app.run(debug=DEBUG)
    #app.run(HOST,PORT)
    

