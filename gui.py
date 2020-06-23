from tkinter import *

root = Tk()
root.title("Calculator")

display = Entry(root)
display.grid(row=0, column=0, columnspan=4, padx=0, ipady=20, sticky="NSEW")

def onClick(number):
	display.insert(END, str(number))


def sum():
	

resetButton = Button(root, text="Reset", padx=20, pady=20).grid(row=1, column=0, sticky="NSEW")
divideButton = Button(root, text="/", padx=20, pady=20).grid(row=1, column=1, sticky="NSEW")
multiButton = Button(root, text="x", padx=20, pady=20).grid(row=1, column=2, sticky="NSEW")
subsButton = Button(root, text="-", padx=20, pady=20).grid(row=1, column=3, sticky="NSEW")
sumButton = Button(root, text="+").grid(row=2, column=3, rowspan=2, ipady=50, ipadx=20, sticky="NSEW")
resultButton = Button(root, text="=").grid(row=4, column=3, rowspan=2, ipady=50, ipadx=20, sticky="NSEW")

num7button = Button(root, text="7", padx=40, pady=20, command=lambda: onClick(7)).grid(row=2, column=0)
num8button = Button(root, text="8", padx=40, pady=20, command=lambda: onClick(8)).grid(row=2, column=1)
num9button = Button(root, text="9", padx=40, pady=20, command=lambda: onClick(9)).grid(row=2, column=2)

num4button = Button(root, text="4", padx=40, pady=20, command=lambda: onClick(4)).grid(row=3, column=0)
num5button = Button(root, text="5", padx=40, pady=20, command=lambda: onClick(5)).grid(row=3, column=1)
num6button = Button(root, text="6", padx=40, pady=20, command=lambda: onClick(6)).grid(row=3, column=2)

num1button = Button(root, text="1", padx=40, pady=20, command=lambda: onClick(1)).grid(row=4, column=0)
num2button = Button(root, text="2", padx=40, pady=20, command=lambda: onClick(2)).grid(row=4, column=1)
num3button = Button(root, text="3", padx=40, pady=20, command=lambda: onClick(3)).grid(row=4, column=2)

num0button = Button(root, text="0", command=lambda: onClick(0)).grid(row=5, column=0, columnspan=2, sticky="NSEW")
decimalButton = Button(root, text=".", padx=41, pady=20, command=lambda: onClick(".")).grid(row=5, column=2, sticky="NSEW")

root.mainloop()