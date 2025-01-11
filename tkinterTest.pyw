import tkinter as tk


def submit ():
    print("Button clicked")

#.pyw extension so that the command line doesn't open as well as the app.
window = tk.Tk()
window.geometry("400x400")

prompt  = tk.Label( text= " Enter amount: $ ")
prompt.pack(pady=50)

userEntry = tk.Entry()
userEntry.pack(pady=20)

button_submit = tk.Button( text= "Submit", command=submit, background= "blue", foreground="white")
button_submit.pack()
''' TO DO
Retrieve information from user, calculate, and return information as a tkinter widget
'''

window.mainloop()
