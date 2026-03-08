import os

list_of_files = os.listdir('model')

if 'model_vgg16.h5' in list_of_files:
    print('File exists')

else:
    print('File does not exist')