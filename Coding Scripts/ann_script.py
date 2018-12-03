"""""""""""""""""""""""""""""""""
Libraries
"""""""""""""""""""""""""""""""""
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense


"""""""""""""""""""""""""""""""""
Importing Data
"""""""""""""""""""""""""""""""""

dataset = pd.read_csv("../Data/formatted_dataset.csv", index_col=0)
dataset = dataset.replace(np.nan, '', regex=True)

"""""""""""""""""""""""""""""""""
Formating Data
"""""""""""""""""""""""""""""""""

# Storing Target Value Names
target_names = np.unique(dataset.iloc[:, 4])

# Label Encoding Data
label_encoder = LabelEncoder()
for column in range(5):
    dataset.iloc[:, column] = label_encoder.fit_transform(dataset.iloc[:, column])

# Separating Data into X and y vectors
X = dataset.iloc[:, 0:4]
y = dataset.iloc[:, 4]

# One Hot Encoding
y = y.reshape(-1,1)
one_hot_encoder = OneHotEncoder(categorical_features = [0])
y = one_hot_encoder.fit_transform(y).toarray()

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

"""""""""""""""""""""""""""""""""
Setting Up Neural Network
"""""""""""""""""""""""""""""""""

# Inital Variables
input_layer_size = np.shape(X)[1]
    
# Initialising the ANN
model = Sequential()   

# Adding the input layer and the first hidden layer
model.add(Dense(input_dim = input_layer_size, units = 16, kernel_initializer = 'uniform', activation = 'relu'))

# Adding the second hidden layer
model.add(Dense(units = 16, kernel_initializer = 'uniform', activation = 'relu'))
    
# Adding the output layer
model.add(Dense(units = 1, kernel_initializer = 'uniform'))

# Compiling the ANN
model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

"""""""""""""""""""""""""""""""""
Training the Neural Network
"""""""""""""""""""""""""""""""""
# Fitting the ANN to the Training set
model.fit(X_train, y_train, batch_size = 20, epochs = 200)

"""""""""""""""""""""""""""""""""
Retrieving the Results
"""""""""""""""""""""""""""""""""
y_pred = model.predict(X_test)
