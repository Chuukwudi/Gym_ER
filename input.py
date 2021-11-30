import functools

from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import numpy as np
from keras.models import load_model
from keras.preprocessing import image


bp = Blueprint("input", __name__, url_prefix="/input")


@bp.route("/enterinfo", methods=("GET", "POST"))
def enterinfo():
    return render_template("input/enterinfo.html")



# I started here by loading my saved model
model = load_model('data/model.h5') # set this to your own directory.

# -------------------------------------------------------------------------
# get number of classes available
classes = []
for directories in os.listdir("data/Image_data/train"):
    classes.append(directories)

no_of_classes = len(classes)
# ------------------------------------------------------------------------


def predict_image(image_path):
    test_image = image.load_img(image_path, target_size=(200, 200))
    test_image = np.expand_dims(test_image, axis=0)
    result = model.predict(test_image)
    
    for i in range(no_of_classes):
        if result[0][i] == 1:
            return classes[i]
            
            
# test model by predicting a sample data from the test set.
prediction = predict_image("data/Image_data/val/Upright bike/image10.jpg")

# prediction = predict_image("data/1612991218-best-rowing-machines-1612991205.jpg")

print("Predicted Equipment : ",prediction)




