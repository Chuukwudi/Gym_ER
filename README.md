# Gym_ER

## 1. Motivation

I recently started going to the gym. I had to rely on more experienced trainers to watch and learn how an equipment is used. I sometimes googled the name written on the body of the equipment to read more details about each equipment, what muscles they trained and videos on how to use them. A thought came to me. Why not build an image recognition web app that recognises an equipment by its photo and outputs details about the equipment? I wrote to a gym owner who let me do the required work such as data gathering, labelling, etc. More details are in [Chukwudi_Ajoku_A0151658_Internship_Report.pdf](https://github.com/Chuukwudi/Gym_ER/blob/main/Chukwudi_Ajoku_A0151658_Internship_Report.pdf). The above resulted to this project.
          
## 2. How to Install and Run the Project
This project runs on the browser and requires python.
1. Clone the repo
2. Create a python environment that meets [requirements.txt](https://github.com/Chuukwudi/Gym_ER/blob/main/requirements.txt)
3. Run [__init__.py](https://github.com/Chuukwudi/Gym_ER/blob/main/__init__.py)
4. Go to your browser and open [127.0.0.1:5000/](http://127.0.0.1:5000/)
5. Select desired image and submit query. 


## 3. Folder/File Description
1. [Data](https://github.com/Chuukwudi/Gym_ER/tree/main/data) contains few samples from my train/validation/test sets.
2. [statis](https://github.com/Chuukwudi/Gym_ER/tree/main/static) contains the CSS file and cache for uploaded images.
3. [templates](https://github.com/Chuukwudi/Gym_ER/tree/main/templates) has the HTML templates.
4. [Chukwudi_Ajoku_A0151658_Internship_Report.pdf](https://github.com/Chuukwudi/Gym_ER/blob/main/Chukwudi_Ajoku_A0151658_Internship_Report.pdf) is the report.
5. [Image Classification.ipynb](https://github.com/Chuukwudi/Gym_ER/blob/main/Image%20Classification.ipynb) contains the Machine Learning pipeline. From data preparation, training to prediction.
          
## 4. Important Consideration
The pretrained model behaves differently when loaded into CPU or GPU. Using TensorFlow with GPU produces desired results as opposed to using TensorFlow on CPU. This is a TensorFlow specific issue and more details can be gotten [here](https://stackoverflow.com/questions/43221730/tensorflow-same-code-but-get-different-result-from-cpu-device-to-gpu-device).
