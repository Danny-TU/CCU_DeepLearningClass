import pandas as pd
import numpy as np
import os
import shutil

train_csv_file = 'dataset/Dataset_for_AQI_Classification/train_data.csv'
val_csv_file = 'dataset/Dataset_for_AQI_Classification/val_data.csv'
test_csv_file = 'dataset/Dataset_for_AQI_Classification/testing_data.csv'

train_df = pd.read_csv(train_csv_file)
val_df = pd.read_csv(val_csv_file)
test_df = pd.read_csv(test_csv_file)

root_dir = 'dataset/IND_and_NEP/'

data_split = ['train', 'valid', 'test']

for part in data_split:
    if not os.path.isdir(part):
    	os.mkdir(part)
    if part == 'train':
        dataframe = train_df
    elif part == 'valid':
        dataframe = val_df
    elif part == 'test':
        dataframe = test_df
    print(f'{part} data len : {len(dataframe)}')
    for i in range(len(dataframe)):
        file_name = dataframe.iloc[i]['Filename']
        class_name =  dataframe.iloc[i]['AQI_Class']
        if not os.path.isdir(part + '/' + class_name):
    	    os.mkdir(part + '/' + class_name)
        #print(root_dir + class_name + file_name)
        shutil.copyfile(root_dir + class_name + '/' + file_name, part + '/' + class_name + '/' + file_name)
