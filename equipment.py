#

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import numpy as np
import math
import ast
from keras.models import load_model
from keras.preprocessing import image

gpu_devices = tf.config.experimental.list_physical_devices('GPU')
for device in gpu_devices: tf.config.experimental.set_memory_growth(device, True)

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


class Equipment:
    
    dict_file = 'equipment_info.txt'

    
    
    def __init__(self, image):
        self.image = image
        self.dictionary = self.get_dict()

    def get_dict(self):
        """ The dictionary file is read and returned as a python dictionary type"""
        with open(self.dict_file, 'r') as f:
            s = f.read()
            read_dict = ast.literal_eval(s)
            return read_dict
    
    def get_predicted_equip(self):
        print(self.image)
        
        self.pred_equip = ML_Model(self.image).predict_image()
        print(self.pred_equip)
        return self.pred_equip
    
    def get_predcited_equip_info(self): 
        """ This function gets the key value pairs from what has been predicted"""  
           
        dictionary = self.get_dict()
        pred_equip = self.get_predicted_equip()     
        for item in dictionary:
            print ("Item : ", item)
            if item == pred_equip:
                print ("pred_equip : ", pred_equip)
                return dictionary[item]
    

class ML_Model:
    
    no_of_classes = ''
    classes = []
    model = ''
    image_path = ''
    
    def __init__(self, image_path):
        # I started here by loading my saved model
        self.model = load_model('data/model_better.h5')  # set this to your own directory.
        self.image_path = image_path
    
    def load_classes(self):
        # get number of classes available
        for directories in os.listdir("data/Image_data/train"):
            self.classes.append(directories)
           
        self.no_of_classes = len(self.classes)
        
    def check_distribution(self, prediction):
        checker = [probability for probability in prediction[0] if math.isclose(1, probability, abs_tol=1e-12) ]
        for probability in prediction[0]:
            if len(checker) > 0:
                return True
            else:
                return False
        
    def predict_image(self):
        
        self.load_classes()
        test_image = image.load_img(self.image_path, target_size=(512, 288))
        test_image = np.expand_dims(test_image, axis=0)
        test_image = test_image.astype('float64') 
        test_image /= 255
        result = self.model.predict(test_image)
        
        if self.check_distribution(result):
            for i in range(self.no_of_classes):
                if result[0][i] == np.max(result):
                    return self.classes[i]
        else:
            return {'error': "Please, choose an image from the gym dataset"}

