import numpy as np
import pandas as pd

dataset = pd.read_csv("../Data/review_data_tidy.csv")

# Used to determing the range for the column and row random selection
dataset_row_size = np.shape(dataset)[0]
dataset_column_size = np.shape(dataset)[1]

# Creating the dataframe
dataframe = pd.DataFrame(columns=['word_minus_3', 'word_minus_2', 'word_minus_1', 'word', 'next_word'])

for row in range(5000):
    
    # We don't want "Word" column to have an NA
    real_word = False
    while (real_word is False):
        # Random row and column selection
        random_row = np.random.randint(low=0, high=dataset_row_size)
        random_column =  np.random.randint(low=0, high=dataset_column_size)
        # Word for "Word" column
        word = dataset.iloc[random_row, random_column]
        if not pd.isna(word):
            real_word = True
            
    # The words surrounding the word        
    word_minus_1 = dataset.iloc[random_row, random_column - 1]
    word_minus_2 = dataset.iloc[random_row, random_column - 2]
    word_minus_3 = dataset.iloc[random_row, random_column - 3]
    next_word = dataset.iloc[random_row, random_column + 1]

    # Turning the words into an array
    array = pd.DataFrame([[word_minus_3, word_minus_2, word_minus_1, word, next_word]],
                     columns=['word_minus_3', 'word_minus_2', 'word_minus_1', 'word', 'next_word'])
    
    # Appending the array
    dataframe = dataframe.append(array, ignore_index=True)
    
# Changing NA's to ''
dataframe = dataframe.replace(np.nan, '', regex=True)

# Exporting Dataframe
dataframe.to_csv("../Data/formatted_dataset.csv")