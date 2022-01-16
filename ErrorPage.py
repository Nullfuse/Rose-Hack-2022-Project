from tkinter import *

ws = Tk()
ws.geometry('400x300')
ws.attributes('-zoomed', True)
ws.title('Dog Adoption Center - Error')
ws['bg']='#F04145'

f = ("Times bold", 14)

def home():
    ws.destroy()
    import main
    
Label(
    ws,
    text="Error - Please Try Again",
    font = f,
    padx=20,
    pady=20,
    bg='#bfff00'
).pack(expand=True, fill=BOTH)

Button(
    ws, 
    text="Home", 
    font=f,
    command=home
    ).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()