import tkinter as tk


def submit ():
    print("Button clicked")

#.pyw extension so that the command line doesn't open as well as the app.
window = tk.Tk()

prompt  = tk.Label( text= " Enter amount: $ ")
prompt.pack()

userEntry = tk.Entry()
userEntry.pack()

button_submit = tk.Button( text= "Submit", command=submit)
button_submit.pack()
''' TO DO
Retrieve information from user, calculate, and return information as a tkinter widget
'''

window.mainloop()
