from tkinter import *
from tkinter import ttk

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

tv.insert(parent='', index=0, iid=0, values=("A", "B", "C", "D"))
tv.insert(parent='', index=1, iid=1, values=("A", "B", "C", "D"))
tv.insert(parent='', index=2, iid=2, values=("A", "B", "C", "D"))
tv.insert(parent='', index=3, iid=3, values=("A", "B", "C", "D"))
tv.insert(parent='', index=4, iid=4, values=("A", "B", "C", "D"))
tv.insert(parent='', index=5, iid=5, values=("A", "B", "C", "D"))
tv.insert(parent='', index=6, iid=6, values=("A", "B", "C", "D"))
tv.insert(parent='', index=7, iid=7, values=("A", "B", "C", "D"))
tv.insert(parent='', index=8, iid=8, values=("A", "B", "C", "D"))
tv.insert(parent='', index=9, iid=9, values=("A", "B", "C", "D"))
tv.insert(parent='', index=10, iid=10, values=("A", "B", "C", "D"))
tv.insert(parent='', index=11, iid=11, values=("A", "B", "C", "D"))
tv.insert(parent='', index=12, iid=12, values=("A", "B", "C", "D"))
tv.insert(parent='', index=13, iid=13, values=("A", "B", "C", "D"))
tv.insert(parent='', index=14, iid=14, values=("A", "B", "C", "D"))
tv.insert(parent='', index=15, iid=15, values=("A", "B", "C", "D"))
tv.insert(parent='', index=16, iid=16, values=("A", "B", "C", "D"))
tv.insert(parent='', index=17, iid=17, values=("A", "B", "C", "D"))
tv.insert(parent='', index=18, iid=18, values=("A", "B", "C", "D"))
tv.insert(parent='', index=19, iid=19, values=("A", "B", "C", "D"))
tv.insert(parent='', index=20, iid=20, values=("A", "B", "C", "D"))

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