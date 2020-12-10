## Simon Says written in tkinter
## Created by Daniel Berrones

import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, bg='blue')
        
        self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
        self.button1.pack()
        
        self.label1 = tk.Label(self.frame, text = "This is a label")
        self.label1.pack()
        
        self.frame.pack()
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = SimpleClass(self.newWindow)   

class SimpleClass:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        
        self.text1 = tk.Text(self.frame, height=20)
        self.text1.pack()
        
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
	main()