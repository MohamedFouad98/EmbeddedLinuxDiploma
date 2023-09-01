from tkinter import *

root = Tk()
root.geometry('400x150')

def action():
    word = entryWord.get()
    # initialise the reversed word 
    reversed_word = ""
    for x in word:
        reversed_word = x + reversed_word
    lblResult['text'] = reversed_word
        

# Create label and entry word
lblWord = Label(root , text ='Enter a word : ')
lblWord.place( x = 20 , y = 20 )
entryWord = Entry(root )
entryWord.place( x = 150 , y = 20 , width = 225 , height = 25)

# create a label to display result
lblResult = Label(root , text = "result .......")
lblResult.place( x = 150 , y = 60)

# Create a button to perform action
btnAction = Button(root , text = "Validate" , command = action)
btnAction.place( x = 150 , y = 100 , width = 225 , height = 30 )

root.mainloop()