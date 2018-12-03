"""""""""""""""""""""""""""""""""
Libraries
"""""""""""""""""""""""""""""""""
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
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
target_names = pd.DataFrame(target_names) 

# Label Encoding Data
label_encoder = LabelEncoder()
for column in range(5):
    dataset.iloc[:, column] = label_encoder.fit_transform(dataset.iloc[:, column])

# Separating Data into X and y vectors
X = dataset.iloc[:, 0:4].values
y = dataset.iloc[:, 4].values

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
model.add(Dense(input_dim = input_layer_size, units = 64, kernel_initializer = 'uniform', activation = 'relu'))

# Adding the second hidden layer
model.add(Dense(units = 64, kernel_initializer = 'uniform', activation = 'relu'))
    
# Adding the output layer
model.add(Dense(units = 1, kernel_initializer = 'uniform'))

# Compiling the ANN
model.compile(optimizer = 'adam', loss = 'mean_squared_error', metrics = ['accuracy'])

"""""""""""""""""""""""""""""""""
Training the Neural Network
"""""""""""""""""""""""""""""""""
# Fitting the ANN to the Training set
model.fit(X_train, y_train, batch_size = 100, epochs = 1000)

"""""""""""""""""""""""""""""""""
Retrieving the Results
"""""""""""""""""""""""""""""""""

# Formatting Sentence
example_sentence = ['What', 'are', 'you', 'talking']
words = pd.Series(example_sentence).values
words = pd.DataFrame(words.reshape(1,4))
sentence = pd.DataFrame().append(words)

# Imputing Sentence
for column in range(words.shape[1]):
    try:
        sentence.iloc[:, column] = label_encoder.transform(sentence.iloc[:, column])
    except:
        sentence.iloc[:, column] = 0 # 0 maps to ''

y_pred = model.predict(sentence).round()
y_pred = pd.DataFrame(y_pred).astype(int)

# Translation of numerical word predictions to string words
word_predictions = pd.DataFrame()

y_pred_length = y_pred.shape[0]

try:
    word = target_names.iloc[y_pred.iloc[0,0], 0]
except:
    word = "(None)"
word = pd.Series(word)
word_prediction = word_predictions.append(word, ignore_index=True)

print(word.iloc[0])
  
    


