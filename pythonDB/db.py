# MY 1ST TKINTER APPLICATION
# CREATED JUNE 27TH, 2019
# COMPLETED AUGUST 2ND, 2019
# DANIEL ALEXANDER BERRONES

import tkinter as tk
from random import choice

class myApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(root)
        self.grid()

        root.title("DB's 1st Tkinter Application")
        root.geometry('395x510')
        root.configure(background='Light Cyan')

        self.__create_widgets()

    def __create_widgets(self):
        'creates main widgets for app'
        # WELCOME LABEL
        self.l = tk.Label(root, 
                text="INTRODUCE YOURSELF",
                bg='Blue',
                fg='White',
                font='Helvetica 22 bold',
                borderwidth=3,relief='sunken')
        self.l.grid(row=2)

        # ASKS USER FOR NAME
        self.l1 = tk.Label(root,
                text="What is your name?",
                bg="khaki1", fg="tomato2",
                font='Arial 25 bold',
                borderwidth=3, relief='groove')
        self.l1.grid(row=7)

        # ASKS USER FOR ORIGIN
        self.label1 = tk.Label(root,
                text="Where are you from?",
                bg="khaki1", fg="tomato2",
                font='Arial 25 bold',
                borderwidth=3,
                relief='groove')
        self.label1.grid(row=9)

        # ENTRY WIDGETS (GET DATA FROM THESE)
        self.str_variable = tk.StringVar()
        self.str_variable1 = tk.StringVar()

        self.user_name = tk.Entry(root, textvariable=self.str_variable,font=('Sans serif',25))
        self.user_name.grid(row=8)

        self.user_state = tk.Entry(root,textvariable=self.str_variable1,font=('Sans serif',25))
        self.user_state.grid(row=10)

        # ENTER BUTTON
        self.button1 = tk.Button(root, text='ENTER', command=self.display_data, font=('Arial',18))
        self.button1.grid(row=15, column=0)

        # CLEAR BUTTON
        self.clear = tk.Button(root, command=self.clear_text, text='CLEAR',font=('Arial',18))
        self.clear.grid(row=20)

        # QUIT BUTTON
        self.button = tk.Button(root, command=root.destroy,
                    highlightbackground='indian red',
                    text='QUIT',font=('Arial',20),
                    height="5", width="10")
        self.button.grid(row=21)

    def clear_text(self):
        'clears text so user can input new data'
        # CLEAR NAME AND STATE LABEL
        try:
            self.lab.grid_forget()
            self.lab1.grid_forget()
            self.user_name.delete(0,tk.END)
            self.user_state.delete(0,tk.END)
        except AttributeError:
            pass

    def display_data(self):
        'prints user name and state to root window'
        l = ['Hola, ','Bonjour, ','Hey, ','Hello, ', 'Hiya, ']
        c = choice(l)
        # DISPLAYS NAME
        stripped_text = self.str_variable.get()
        if len(stripped_text) <= 1:
            pass
        else:
            self.lab = tk.Label(root,text=c + stripped_text + "!",
                    font=('Verdana',24))
            self.lab.grid(row=25)

        st = ['Let\'s go to ','I wanna see ','Can\'t wait to see ','I\'d love to visit ']
        c1 = choice(st)

        # DISPLAYS STATE
        stripped_text1 = self.str_variable1.get()
        if len(stripped_text1) <= 1:
            pass
        else:
            self.lab1 = tk.Label(root,text=c1 + stripped_text1 + " soon!",
                    font=('Verdana',22))
            self.lab1.grid(row=27)

    
if __name__ == '__main__':
    root = tk.Tk()
    app = myApp(root)
    app.mainloop()