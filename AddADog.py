from tkinter import *
import DogData

doglist = []
DogData.readList(doglist)

ws = Tk()
ws.geometry('400x300')
ws.attributes('-zoomed', True)
ws.title('Dog Adoption Center - Add a Dog')
ws['bg']='#48C2D4'

# frames
frame = Frame(ws, padx=145, pady=50)
frame.pack(expand=True)

f = ("Times bold", 14)

# val is equal to the value of the currently selected radio button
# default is 0
val = IntVar()
val.set(0)

def nextPage():
    DogData.addDog(doglist, [p_name.get(), p_age.get(), DogData.dog_gender(val.get()), p_breed.get()])
    ws.destroy()
    import AddADog_Confirmation

def prevPage():
    ws.destroy()
    import main
    

# labels
Label(
    frame, 
    text="Add a Dog",
    font=("Times", "24", "bold")
    ).grid(row=0, columnspan=3, pady=10)

Label(
    frame, 
    text='Dog Name', 
    font=("Times", "14")
    ).grid(row=1, column=0, pady=5)

Label(
    frame, 
    text='Dog Breed', 
    font=("Times", "14")
    ).grid(row=2, column=0, pady=5)

Label(
    frame, 
    text='Dog Age', 
    font=("Times", "14")
    ).grid(row=3, column=0, pady=5)

Label(
    frame, 
    text='Dog Gender', 
    font=("Times", "14")
    ).grid(row=4, column=0, padx=20, pady=5)

# Entry
p_name = Entry(frame, width=30)
p_breed = Entry(frame, width=30)
p_age = Entry(frame, width=30)

p_name.grid(row=1, column=1)
p_breed.grid(row=2, column=1)
p_age.grid(row=3, column=1)

frame2 = Frame(
    frame
)
frame2.grid(row=4, column=1, pady=5)

undetermined_rb = Radiobutton(
    frame2,
    text = 'Undetermined',
    value = 0,
    variable = val
)
undetermined_rb.pack(side=LEFT)

male_rb = Radiobutton(
    frame2,
    text = 'Male',
    value = 1,
    variable = val
)
male_rb.pack(side=LEFT)

female_rb = Radiobutton(
    frame2,
    text = 'Female',
    value = 2,
    variable = val
)
female_rb.pack(side=LEFT)

Button(
    ws, 
    text="Previous Page", 
    font=f,
    command=prevPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws, 
    text="Submit", 
    font=f,
    command=nextPage
    ).pack(fill=X, expand=TRUE, side=RIGHT)

ws.mainloop()