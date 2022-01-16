from tkinter import *
from PIL import Image,ImageTk

#---------------------------FRONTEND---------------------------
ws = Tk()
ws.geometry('400x300')
ws.attributes('-zoomed', True)
ws.title('Dog Adoption Center')
ws['bg']='#D3E4E4'

f = ("Times bold", 14)
t = ("Times bold", 35)


#Create a canvas
canvas= Canvas(ws, width= 275, height= 275, highlightthickness=0)
canvas.configure(bg='#D3E4E4')
canvas.pack()

#Load an image in the script
img= (Image.open("HomePageDog.png"))

#Resize the Image using resize method
resized_image= img.resize((250,250), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
canvas.create_image(10,10, anchor=NW, image=new_image)


def addDog():
    ws.destroy()
    import AddADog

def deleteDog():
    ws.destroy()
    import DeleteADog

def viewDogs():
    ws.destroy()
    import ViewAllDogs

Label(
    ws,
    text="Welcome",
    padx=10,
    pady=10,
    bg='#D3E4E4',
    font=t
).pack(expand=True, fill=BOTH)

Button(
    ws, 
    text="Add a Dog", 
    font=f,
    command=addDog
    ).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws, 
    text="View all Dogs", 
    font=f,
    command=viewDogs
    ).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws, 
    text="Delete a Dog", 
    font=f,
    command=deleteDog
    ).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()