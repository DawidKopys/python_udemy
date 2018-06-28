from tkinter import *

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

window = Tk()
window.title('Feet to Meters')

feet = StringVar()
meters = StringVar()

feet_entry = Entry(window, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

Label(window, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
Button(window, text='Calculate', command=calculate).grid(column=3, row=3, sticky=W)

Label(window, text='feet').grid(column=3, row=1, sticky=W)
Label(window, text='is equivalent to').grid(column=1, row=2, sticky=E)
Label(window, text='meters').grid(column=3, row=2, sticky=W)

for child in window.winfo_children():
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
window.bind('<Return>', calculate)

window.mainloop()
