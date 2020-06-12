# MY 1ST TKINTER APPLICATION
# CREATED JUNE 27TH, 2019
# DANIEL ALEXANDER BERRONES

import tkinter as tk
from tkinter import ttk

# ROOT IS THE MAIN WINDOW
root = tk.Tk()
root.title("My 1st Tkinter Application")

frame1 = tk.Frame(root, height=800, width=500, bg="Beige")
frame1.grid()

# LABELS DISPLAY TEXT INFO
label = tk.Label(frame1, text="Daniel's Reddit App", relief="raised",bg="Blue", fg="White", font=('Lucida Grande',40))
label.grid(column=0)

label2 = tk.Label(frame1, text="My 3rd Label", bg="Blue", fg="White", font=('Helvitica',25))
label2.grid() # THIS PUTS THE LABEL ON THE ROOT

# ENTRY 
entry = tk.Entry(frame1,font=('Sans serif',25))
entry.grid(column=1)

# BUTTON
button = tk.Button(frame1, command=root.destroy, text='Quit',font=('Gisha',22))
button.grid()

button1 = tk.Button(frame1, command=root.destroy, text='Quit',font=('Gisha',22))
button1.grid()

#STARTS THE PROGRAM
root.mainloop()