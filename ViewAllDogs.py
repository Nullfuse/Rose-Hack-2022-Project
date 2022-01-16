from tkinter import *
from tkinter import ttk
import DogData

doglist = []
DogData.readList(doglist)

ws = Tk()
ws.attributes('-zoomed', True)
ws.title('Dog Adoption Center - View all Dogs')
ws['bg']='white'

frame = Frame(ws)
frame.pack(padx=20, pady=20)

f = ("Times bold", 14)

tv = ttk.Treeview(frame, columns=(1, 2, 3, 4), show='headings', height=15)
tv.pack(side=LEFT)

tv.heading(1, text="Dog Name")
tv.heading(2, text="Dog Breed")
tv.heading(3, text="Dog Age")
tv.heading(4, text="Dog Gender")

sb = Scrollbar(frame, orient=VERTICAL)
sb.pack(side=RIGHT, fill=Y)

tv.config(yscrollcommand=sb.set)
sb.config(command=tv.yview)

def home():
    ws.destroy()
    import main

for i in range(len(doglist)):
  tv.insert(parent='', index=i, iid=i, values=(doglist[i].name, doglist[i].breed,doglist[i].age, doglist[i].gender))

Button(
    ws, 
    text="Home", 
    font=f,
    command=home
    ).pack(fill=X, expand=TRUE, side=LEFT)

style = ttk.Style()
style.theme_use("default")
style.map("Treeview")

ws.mainloop()