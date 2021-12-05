import os

from flask import Flask
from flask import render_template, request
import logging
import urllib

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
IMAGE_UPLOAD_PATH = app.config["IMAGE_UPLOAD_PATH"]

####################################################################
# Routing details - URL routing seen on client browser
####################################################################


@app.route("/")
def index():
    logging.info('Gym_ER -- routed to index page')
    return render_template("input.html")


@app.route("/result", methods=['POST', 'GET'])
def result():
    
    logging.info('Gym_ER -- routing to result page')
    # image file uploaded by the user
    image = request.files['image']
    image.save(IMAGE_UPLOAD_PATH)
    #image = request.form['image'] 
    # print(image)
    logging.info('Image Uploaded - ',IMAGE_UPLOAD_PATH)
    
    
    
    import equipment
    # equip_info is a dict 
    # equip_info = equipment.Equipment(image).get_equip()
    equip_info = equipment.Equipment(IMAGE_UPLOAD_PATH).predict_equip()
    return render_template("result.html" , equip_info = equip_info)



##############################################################################
# Main Application: Execution of FreedomOfSearch Application starts from here. 
##############################################################################


if(__name__ == "__main__"):
    
    # defining the log and application configurations 
    logging.basicConfig(filename='logs/app.log', level=logging.INFO)
    logging.info('Gym_ER -- executing main()')
    logging.info('Gym_ER -- invoking server 127.0.0.1, port = 5000')
    app.run(debug=DEBUG)
    # app.run(HOST,PORT)

