
from tkinter import*

calc = Tk()
#naming the project
calc.title("Calculator")
calc.iconbitmap("calculator1.ico")
calc.config(bg="#666666")

expression = ""

# Create functions
def add(value):
    global expression
    expression += value
    display.config(text=expression)
    
def clear():
    global expression
    expression = ""
    display.config(text=expression)
    
def calculate():
    global expression
    result = ""
    if expression != "":
        try:
            result = eval(expression)
        except:
            result = "error"
            expression = ""
    display.config(text=result)
            
# Creating GUI
display = Label(calc, text="", width=43, borderwidth=5, bg="black", fg="white")
display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#adding buttons
button_7 = Button(calc, text="7", padx=43, pady=20,bg="#4d4d4d", fg="white",command=lambda: add("7"))
button_7.grid(row=3, column=0)

button_8 = Button(calc, text="8",padx=43, pady=20,bg="#4d4d4d",fg="white", command=lambda: add("8"))
button_8.grid(row=3, column=1)

button_9 =Button(calc, text="9",padx=43, pady=20,bg="#4d4d4d",fg="white", command=lambda: add("9"))
button_9.grid(row=3, column=2)

button_4 = Button(calc, text="4", padx=43, pady=20,bg="#4d4d4d",fg="white",command=lambda: add("4"))
button_4.grid(row=4, column=0)

button_5 = Button(calc, text="5", padx=43, pady=20,bg="#4d4d4d",fg="white",command=lambda: add("5"))
button_5.grid(row=4, column=1)

button_6 = Button(calc, text="6",padx=43, pady=20,bg="#4d4d4d",fg="white", command=lambda: add("6"))
button_6.grid(row=4, column=2)

button_1 = Button(calc, text="1",padx=43, pady=20,bg="#4d4d4d",fg="white", command=lambda: add("1"))
button_1.grid(row=5, column=0)

button_2 = Button(calc, text="2",padx=43, pady=20, bg="#4d4d4d",fg="white",command=lambda: add("2"))
button_2.grid(row=5, column=1)

button_3 = Button(calc, text="3", padx=43, pady=20,bg="#4d4d4d",fg="white",command=lambda: add("3"))
button_3.grid(row=5, column=2)

button_0 = Button(calc, text="0",padx=43, pady=20,bg="#4d4d4d",fg="white", command=lambda: add("0"))
button_0.grid(row=6, column=1)

button_dot = Button(calc, text=".",padx=43, pady=20,bg="#4d4d4d",fg="white", command=lambda: add("."))
button_dot.grid(row=6, column=0)

button_divide = Button(calc, text="/",padx=43, pady=20,bg="DarkGoldenRod1",fg="white", command=lambda: add("/"))
button_divide.grid(row=2, column=0)

button_add = Button(calc, text="+", padx=43, pady=20,height="6" ,bg="DarkGoldenRod1",fg="white",command=lambda: add("+"))
button_add.grid(row=1, column=2, rowspan=2)

button_equals = Button(calc, text="=", padx=43, pady=20, bg="#ff9980", fg="white",command=lambda: calculate())
button_equals.grid(row=6, column=2)

button_clear = Button(calc, text="C", padx=43, pady=20,bg="gray67",fg="white",command=lambda: clear())
button_clear.grid(row=1, column=0)

button_subtract = Button(calc, text="-",padx=43, pady=20,bg="DarkGoldenRod1",fg="white", command=lambda: add("-"))
button_subtract.grid(row=1, column=1)

button_multiply = Button(calc, text="*", padx=43, pady=20,bg="DarkGoldenRod1",fg="white",command=lambda: add("*"))
button_multiply.grid(row=2, column=1)

calc.mainloop() 