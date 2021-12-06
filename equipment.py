#

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import numpy as np
from keras.models import load_model
from keras.preprocessing import image

physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)

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
    
    def predict_equip(self):
        self.pred_equip = ML_Model(self.image).predict_image()
        #print(self.pred_equip)
        return self.pred_equip
    
    def map_equip(self, pred_equip):
    # '''
    # dict { name : 'threadmill' , related info: { image: 'dffsdfs' , 
    #                                             video_link :'sdadasdas', 
    #                                             muscle group :'dfdfda',
    #                                             additional_info : ''}} 
    #  # name and maps the info in the predefined list (dictionary)
    #  output.enterinfo(pred_dict)
    # '''
        pass
    
    def get_equip(self):
        pass


class ML_Model:
    
    no_of_classes = ''
    classes = []
    model = ''
    image_path = ''
    
    def __init__(self,image_path):
        # I started here by loading my saved model
        # self.model = load_model('data/model.h5')  # set this to your own directory.
        self.model = load_model('data/model_better.h5') 
        self.image_path = image_path
    
    def load_classes(self):
        # get number of classes available
        for directories in os.listdir("data/Image_data/train"):
            self.classes.append(directories)
           
        self.no_of_classes = len(self.classes)
        
    def predict_image(self):
        
        self.load_classes()
        test_image = image.load_img(self.image_path, target_size=(200, 200))
        test_image = np.expand_dims(test_image, axis=0)
        result = self.model.predict(test_image)
        
        for i in range(self.no_of_classes):
            if result[0][i] == 1:
                return self.classes[i]
