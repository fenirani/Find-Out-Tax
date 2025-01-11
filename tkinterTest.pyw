import tkinter as tk


def calculate(amount):
    ''' Formula is amount / (1 + tax) '''
    tax = 0.06625             # 6.625 %
    beforeTax = round(amount / (1 + tax), 2 ) 
    return beforeTax

def submit():
    '''Calls calculate function and then uses its value to 'configure' a tKinter label widget ''' 
    beforeTax= calculate(float(user_Entry.get()))

    directions_Label.config(text = "ENTER THIS AMOUNT:")
    beforeTax_Label.config(text=beforeTax)


#.pyw extension so that the command line doesn't open as well as the app.
window = tk.Tk()
window.geometry("400x400")

prompt_Label  = tk.Label( text= " Enter amount: $ ")
prompt_Label.pack(pady=25)

user_Entry = tk.Entry()
user_Entry.pack(pady=10)

button_Submit = tk.Button( text= "Submit", command=submit, background= "blue", foreground="white")
button_Submit.pack(pady=20)

directions_Label = tk.Label()
directions_Label.pack()
beforeTax_Label = tk.Label ()
beforeTax_Label.pack()

window.mainloop()
