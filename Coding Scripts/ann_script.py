"""""""""""""""""""""""""""""""""
Libraries
"""""""""""""""""""""""""""""""""
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
#from ann_visualizer.visualize import ann_viz # Run this to visualize ann

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
model.fit(X_train, y_train, batch_size = 100, epochs = 250)


"""""""""""""""""""""""""""""""""
Data Visualization
"""""""""""""""""""""""""""""""""
#ann_viz(model, view=True, title="Project Wordly Neural Network") # Run this to get a visual of the image

"""""""""""""""""""""""""""""""""
GUI Code
"""""""""""""""""""""""""""""""""
from tkinter import *
from tkinter import Tk, scrolledtext, Menu, filedialog, END, messagebox, simpledialog, INSERT, Text
import tempfile

# create root object
root = Tk(className=" Project Wordly")

# create text area within window
textArea = Text(root, width=50, height=20)

# create temporary file for current text memory storage
temp = tempfile.TemporaryFile(mode='w+t')


######################################################
# MENU BAR FUNCTIONS
######################################################

def openFile():
    file = filedialog.askopenfile(parent=root, mode='rb', title="Select a File",
                                  filetype=(("Text File", "*.txt"), ("All files", "*.")))

    if file != None:
        contents = file.read()
        textArea.insert('1.0', contents)
        file.close()


def saveFile():
    file = filedialog.asksaveasfile(mode='w')

    if file != None:
        # reads data and slices off extra return at the end
        text = textArea.get('1.0', END + '-lc')

        file.write(text)
        file.close()


def newFile():
    if len(self.textArea.get('1.0', END + '-lc')) > 0:
        if messagebox.askyesno("Save", "Do you want to save this file?"):
            saveFile()
        else:
            textArea.delete('1.0', END)


def findInFile():
    findString = simpledialog.askstring("Find", "Enter the text you want to find.")
    text = textArea.get('1.0', END)

    if findString.upper() in text.upper():
        print("TRUE")


def exitRoot():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()


def about():
    messagebox.showinfo("About", "Project Wordly is a student led project " +
                        "designed to use a neural network to do next word " +
                        "prediction. Other features will be forthcoming.")


############################################################
# MENU BAR SETUP
############################################################

# makes menu
menu = Menu(root)

# configures menu
root.config(menu=menu)

# creates file menu item and its drop down options
fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New", command=newFile)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_command(label="Find", command=findInFile)
fileMenu.add_command(label="Print")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exitRoot)

# creates help menu item and its drop down options
helpMenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="Help")
helpMenu.add_command(label="About", command=about)

########################################################
# TEXT PREDICTION AREA
########################################################

textPrediction = Text(root, height=10, width=50, background='#EADDDB')

textPrediction.insert(INSERT, textArea.get("1.0", "end-1c"))

textPrediction.pack(side=BOTTOM)


########################################################
# AREA FOR ALGORITHM CALCS
########################################################

def typed_backspace(event):
    return


def typed_space(event):
    # detect cursor position
    pos = textArea.index(INSERT)
    curr_pos = int(pos.split('.', 1)[1])

    # get text that has already been typed
    string = textArea.get("1.0", END)

    # split text into seperate words
    words = string.split(' ')

    # delete everything in GUI, happens at the beginning of every loop
    textPrediction.delete('1.0', END)

    try:
        # Formatting Sentence
        example_sentence = [words[-5], words[-4], words[-3], words[-2]]
        words = pd.Series(example_sentence).values
        words = pd.DataFrame(words.reshape(1, 4))
        sentence = pd.DataFrame().append(words)

        # Imputing Sentence
        for column in range(words.shape[1]):
            try:
                sentence.iloc[:, column] = label_encoder.transform(sentence.iloc[:, column])
            except:
                sentence.iloc[:, column] = 0  # 0 maps to ''

        y_pred = model.predict(sentence).round()
        y_pred = pd.DataFrame(y_pred).astype(int)

        # Translation of numerical word predictions to string words
        word_predictions = pd.DataFrame()

        y_pred_length = y_pred.shape[0]

        try:
            word = target_names.iloc[y_pred.iloc[0, 0], 0]
        except:
            word = "(None)"
        word = pd.Series(word)
        word_predictions = word_predictions.append(word, ignore_index=True)

        textPrediction.insert(INSERT, word.iloc[0])

    except:
        pass


# detects if a backspace is typed
root.bind("<BackSpace>", typed_backspace)

root.bind("<space>", typed_space)

# don't know exactly what this does but program won't run without it :)
textArea.pack()

# keeps window open
root.mainloop()




    


