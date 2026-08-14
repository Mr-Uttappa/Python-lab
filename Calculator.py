# import tkinter as tk

# root = tk.Tk()
# root.title("Python Calculator")

# # Entry widget for display
# entry = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=5, relief="ridge")
# entry.grid(row=0, column=0, columnspan=4)

# # Functions
# def click_button(value):
#     current = entry.get()
#     entry.delete(0, tk.END)
#     entry.insert(0, current + str(value))

# def clear_button():
#     entry.delete(0, tk.END)

# def calculate():
#     try:
#         result = eval(entry.get())
#         entry.delete(0, tk.END)
#         entry.insert(0, str(result))
#     except:
#         entry.delete(0, tk.END)
#         entry.insert(0, "Error")

# # Button layout (fixed to include '+')
# buttons = [
#     ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
#     ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
#     ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
#     ('0',4,0), ('.',4,1), ('C',4,2), ('+',4,3),
#     ('=',5,0)
# ]

# for (text, row, col) in buttons:
#     if text == '=':
#         tk.Button(root, text=text, width=20, height=2, command=calculate).grid(row=row, column=col, columnspan=4)
#     elif text == 'C':
#         tk.Button(root, text=text, width=5, height=2, command=clear_button).grid(row=row, column=col)
#     else:
#         tk.Button(root, text=text, width=5, height=2, command=lambda t=text: click_button(t)).grid(row=row, column=col)

# root.mainloop()






# 🎨 Colorful Tkinter Calculator



import tkinter as tk

root = tk.Tk()
root.title("iPhone Style Calculator")
root.configure(bg="black")

# Entry display
entry = tk.Entry(root, width=15, font=("Arial", 24, "bold"),
                 borderwidth=0, relief="flat", bg="black", fg="white", justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10)

def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear_button():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Helper function
def make_button(text, row, col, bg, fg="white", colspan=1, command=None):
    tk.Button(root, text=text, width=5, height=2, bg=bg, fg=fg,
              font=("Arial", 18, "bold"), command=command).grid(row=row, column=col, columnspan=colspan, padx=2, pady=2)

# Buttons
make_button("C",1,0,"lightgray","black", command=clear_button)
make_button("/",1,3,"orange", command=lambda: click_button("/"))

make_button("7",2,0,"dimgray", command=lambda: click_button("7"))
make_button("8",2,1,"dimgray", command=lambda: click_button("8"))
make_button("9",2,2,"dimgray", command=lambda: click_button("9"))
make_button("*",2,3,"orange", command=lambda: click_button("*"))

make_button("4",3,0,"dimgray", command=lambda: click_button("4"))
make_button("5",3,1,"dimgray", command=lambda: click_button("5"))
make_button("6",3,2,"dimgray", command=lambda: click_button("6"))
make_button("-",3,3,"orange", command=lambda: click_button("-"))

make_button("1",4,0,"dimgray", command=lambda: click_button("1"))
make_button("2",4,1,"dimgray", command=lambda: click_button("2"))
make_button("3",4,2,"dimgray", command=lambda: click_button("3"))
make_button("+",4,3,"orange", command=lambda: click_button("+"))

make_button("0",5,0,"dimgray", colspan=2, command=lambda: click_button("0"))
make_button(".",5,2,"dimgray", command=lambda: click_button("."))
make_button("=",5,3,"orange", command=calculate)

root.mainloop()
