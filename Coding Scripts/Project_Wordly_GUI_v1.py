from tkinter import Tk, scrolledtext, Menu, filedialog, END, messagebox, simpledialog, INSERT
import tempfile

#create root object
root = Tk(className = " Project Wordly")

#create text area within window
textArea = scrolledtext.ScrolledText(root, width=50,height=20)

#create temporary file for current text memory storage
temp = tempfile.TemporaryFile(mode='w+t')

######################################################
# MENU BAR FUNCTIONS
######################################################


def openFile():
    file = filedialog.askopenfile(parent=root, mode='rb', title="Select a File", filetype=(("Text File","*.txt"),("All files","*.")))
    
    if file != None:
        contents = file.read()
        textArea.insert('1.0',contents)
        file.close()

def saveFile():
    file = filedialog.asksaveasfile(mode='w')
    
    if file != None:
        
        #reads data and slices off extra return at the end
        text = textArea.get('1.0', END+'-lc')
        
        file.write(text)
        file.close()
        
def newFile():
    if len(self.textArea.get('1.0', END+'-lc')) > 0:
        if messagebox.askyesno("Save","Do you want to save this file?"):
            saveFile()
        else:
            textArea.delete('1.0',END)
            
def findInFile():
    findString = simpledialog.askstring("Find","Enter the text you want to find.")
    text = textArea.get('1.0', END)
    
    if findString.upper() in text.upper():    
        print("TRUE")

def exitRoot():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()
        
def about():
    messagebox.showinfo("About","Project Wordly is a student led project designed to use a neural network to do next word prediction. Other features will be forthcoming.")


############################################################
# MENU BAR SETUP
############################################################

#makes menu
menu = Menu(root)

#configures menu
root.config(menu = menu)

#creates file menu item and its drop down options
fileMenu = Menu(menu)
menu.add_cascade(label = "File", menu = fileMenu)
fileMenu.add_command(label="New", command=newFile)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_command(label="Find", command=findInFile)
fileMenu.add_command(label="Print")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exitRoot)

#creates help menu item and its drop down options
helpMenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="Help")
helpMenu.add_command(label="About", command=about)


########################################################
# AREA FOR ALGORITHM CALCS
########################################################


#this method to be used to maybe insert output of next word prediction
#textArea.insert(INSERT, "hello")


#keystroke detection
def key(event):
    
    #assigns key to char
    kp = repr(event.char)
    
    #writes char to temp file
    temp.write(kp)
    
    #starts reading at char index 0
    temp.seek(0)
    print(temp.read())


#binds the keys type to the open root window
root.bind("<Key>", key)

#don't know exactly what this does but program won't run without it :)
textArea.pack()

#keeps window open
root.mainloop()




# TO DO'S
#need to parse behind cursor after every stroke to identify previous 3 words
#need to create secondary window to show most likely predictions