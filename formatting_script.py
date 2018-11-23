import numpy as np
import pandas as pd

dataset = pd.read_csv("words_separated_clean.csv")

dataset_rows = np.shape(dataset)[0]

dataframe = pd.DataFrame(columns=['word_minus_3', 'word_minus_2', 'word_minus_1', 'word', 'next_word'])

for column in range(1000):
    
    real_word = False
    
    while (real_word is False):
        random_row = np.random.randint(low=0, high=dataset_rows)
        random_column =  np.random.randint(low=0, high=10)
        word = dataset.iloc[random_row, random_column]
        if not pd.isna(word):
            real_word = True
            
    word_minus_1 = dataset.iloc[random_row, random_column - 1]
    word_minus_2 = dataset.iloc[random_row, random_column - 2]
    word_minus_3 = dataset.iloc[random_row, random_column - 3]
    next_word = dataset.iloc[random_row, random_column + 1]

    array = pd.DataFrame([[word_minus_3, word_minus_2, word_minus_1, word, next_word]],
                     columns=['word_minus_3', 'word_minus_2', 'word_minus_1', 'word', 'next_word'])
    dataframe = dataframe.append(array)
    
#pd.isna(dataframe.iloc[:, 4])