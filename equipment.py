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
    
    EQUIP = {
        'name':"" ,
        'image': "",
        'video_link': "",
        'muscle_group': "",
        'additional_info': ""}
    image = ''
    pred_equip = ''
    

    
    def __init__(self, image):
        self.image = image
        self.dict_file = 'equipment_info.txt'

        
    
   

    def read_dict(self, dict_file):
        """ The dictionary file is read and returned as a python dictionary type"""
        with open(dict_file, 'r') as f:
            s = f.read()
            self.read_dict = ast.literal_eval(s)
            return self.read_dict
    
    
    
    
    def predict_equip(self):
        self.pred_equip = ML_Model(self.image).predict_image()
        return self.pred_equip
    
    def map_equip(self, pred_equip):
        
        """ This function gets the key value pairs from what has been predicted"""
        
        dictionary = self.read_dict(self.dict_file)
        for item in dictionary:
            if item == pred_equip:
                return dictionary[item]
            
    
    def get_equip(self):
        pass


class ML_Model:
    
    no_of_classes = ''
    classes = []
    model = ''
    image_path = ''
    
    def __init__(self,image_path):
        # I started here by loading my saved model
        self.model = load_model('data/model.h5')  # set this to your own directory.
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
            return "Please, choose an image from the gym dataset"
        

# Testing the functions I have just written
equippy = Equipment('data/Image_data/train/Ab trainer/image12.jpg')
pred_equip = equippy.predict_equip()
equip_info = equippy.map_equip(pred_equip)

print(equip_info)





