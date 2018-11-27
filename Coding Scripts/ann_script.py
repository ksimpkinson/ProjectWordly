"""""""""""""""""""""""""""""""""
Libraries
"""""""""""""""""""""""""""""""""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import KFold, cross_val_score
from keras.models import Sequential
from keras.layers import Dense



"""""""""""""""""""""""""""""""""
Importing Data
"""""""""""""""""""""""""""""""""

dataset = pd.read_csv("Blake/Fall 2018/ProjectWordly/words_separated_clean.csv")

"""""""""""""""""""""""""""""""""
Formating Data
"""""""""""""""""""""""""""""""""

# Storing Target Value Names
# target_names = np.unique(dataset.iloc[])

# Label Encoding Data
label_encoder = LabelEncoder()
# dataset.iloc[] = label_encoder.fit_transform(dataset.iloc[])

# Separating Data into X and y vectors
# X = dataset.iloc[]
# y = dataset.iloc[]

# Setting up K-fold Cross Validation
k_fold = KFold(n_splits=10, random_state=7, shuffle=True)

"""""""""""""""""""""""""""""""""
Setting Up Neural Network
"""""""""""""""""""""""""""""""""

def make_ann():
    
    # Inital Variables
    input_layer_size = np.shape(X)[1]
    
    # Initialising the ANN
    model = Sequential()   

    # Adding the input layer and the first hidden layer
    model.add(Dense(input_dim = input_layer_size, units = 16, 
                    kernel_initializer = 'uniform', activation = 'relu'))

    # Adding the second hidden layer
    model.add(Dense(units = 16, kernel_initializer = 'uniform', 
                    activation = 'relu'))
    
    # Adding the output layer
    model.add(Dense(units = 1, kernel_initializer = 'uniform'))

    # Compiling the ANN
    model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

    return model

"""""""""""""""""""""""""""""""""
Retrieving the Results
"""""""""""""""""""""""""""""""""
y_pred = cross_val_predict(make_ann, X, y, cv=k_fold, n_jobs=-1) #Change n_jobs to 1 if giving you greif

"""""""""""""""""""""""""""""""""
Classifier Performance Report
"""""""""""""""""""""""""""""""""

accuracy_score = cross_val_score(make_ann, X, y, cv=k_fold, n_jobs=1).mean()
f1 = np.average(f1_score(y, y_pred, average=None))