from tkinter import *
import random

# Create window object
app = Tk()

app.title('Hydra Virus')
app.geometry('500x500')

# Draw Hydra


# Get number of new heads
def getHeads():
    return random.randint(2, 5)

# Start program
app.mainloop