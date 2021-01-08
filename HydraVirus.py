from tkinter import *
import random

# Create window object
app = Tk()
app.title('Hydra Virus')
app.geometry('500x500')
app.resizable(0, 0)

# Draw Hydra
hydraSerpant = Label(app, text='---------------------------------------------------------', font=('bold', 14), pady=20)
hydraSerpant.grid(row=0, column=0)

# Function to open a new window  
def openNewWindow(): 
    # Toplevel object which will be treated as a new window 
    newAPP = Tk() 
    newAPP.title("Hydra Virus") 
    newAPP.geometry("500x500")
    newAPP.resizable(0, 0)

    # Draw Head
    newHead = Label(newAPP, text='---------------------------------------------------------', font=('bold', 14), pady=20)
    newHead.grid(row=0, column=0)

# Get number of new heads
def getHeads():
    return random.randint(2, 5)

def closeWindow():
    for i in range(getHeads()):
        openNewWindow()
    
    app.destroy()

app.protocol("WM_DELETE_WINDOW", closeWindow)

# Start program
app.mainloop()