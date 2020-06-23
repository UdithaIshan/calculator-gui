from tkinter import *

value = 0
operator = ""

def onClick(number):
	display.insert(END, str(number))

def reset():
	display.delete(0, END)

def sum():
	global value
	global operator
	value = display.get()
	operator = "+"
	display.delete(0, END)


def subs():
	global value
	global operator
	value = display.get()
	operator = "-"
	display.delete(0, END)

def div():
	global value
	global operator
	value = display.get()
	operator = "/"
	display.delete(0, END)

def mult():
	global value
	global operator
	value = display.get()
	operator = "x"
	display.delete(0, END)


def result():
	global value
	global operator
	val = float(display.get())
	display.delete(0, END)

	if operator == "+":
		res = (val + float(value))
		display.insert(0, str(res))

	elif operator == "-":
		res = (float(value) - val)
		display.insert(0, str(res))

	elif operator == "/":
		if val != 0:
			res = (float(value) / val)
			display.insert(0, str(res))
		else:
			display.insert(0, "Error")

	elif operator == "x":
		res = (float(value) * val)
		display.insert(0, str(res))


root = Tk()
root.title("Calculator")

display = Entry(root)
display.grid(row=0, column=0, columnspan=4, padx=0, ipady=20, sticky="NSEW")

resetButton = Button(root, text="Reset", padx=20, pady=20, bg="cyan", command=reset).grid(row=1, column=0, sticky="NSEW")
divideButton = Button(root, text="/", padx=20, pady=20,command=div).grid(row=1, column=1, sticky="NSEW")
multiButton = Button(root, text="x", padx=20, pady=20, command=mult).grid(row=1, column=2, sticky="NSEW")
subsButton = Button(root, text="-", padx=20, pady=20, command=subs).grid(row=1, column=3, sticky="NSEW")
sumButton = Button(root, text="+", command=sum)
resultButton = Button(root, text="=", command=result)

num7button = Button(root, text="7", padx=40, pady=20, command=lambda: onClick(7))
num8button = Button(root, text="8", padx=40, pady=20, command=lambda: onClick(8))
num9button = Button(root, text="9", padx=40, pady=20, command=lambda: onClick(9))

num4button = Button(root, text="4", padx=40, pady=20, command=lambda: onClick(4))
num5button = Button(root, text="5", padx=40, pady=20, command=lambda: onClick(5))
num6button = Button(root, text="6", padx=40, pady=20, command=lambda: onClick(6))

num1button = Button(root, text="1", padx=40, pady=20, command=lambda: onClick(1))
num2button = Button(root, text="2", padx=40, pady=20, command=lambda: onClick(2))
num3button = Button(root, text="3", padx=40, pady=20, command=lambda: onClick(3))

num0button = Button(root, text="0", command=lambda: onClick(0))
decimalButton = Button(root, text=".", padx=41, pady=20, command=lambda: onClick(".")).grid(row=5, column=2, sticky="NSEW")

num7button.grid(row=2, column=0)
num8button.grid(row=2, column=1)
num9button.grid(row=2, column=2)
num4button.grid(row=3, column=0)
num5button.grid(row=3, column=1)
num6button.grid(row=3, column=2)
num1button.grid(row=4, column=0)
num2button.grid(row=4, column=1)
num3button.grid(row=4, column=2)
num0button.grid(row=5, column=0, columnspan=2, sticky="NSEW")

sumButton.grid(row=2, column=3, rowspan=2, ipady=50, ipadx=20, sticky="NSEW")
resultButton.grid(row=4, column=3, rowspan=2, ipady=50, ipadx=20, sticky="NSEW")

root.mainloop()