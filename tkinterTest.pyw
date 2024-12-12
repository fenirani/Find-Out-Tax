import tkinter as tk

#.pyw extension so that the command line doesn't start too
window = tk.Tk()

prompt  = tk.Label( text= " Enter amount: $ ")
prompt.pack()

userEntry = tk.Entry()
userEntry.pack()


window.mainloop()
