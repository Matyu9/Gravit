import tkinter as tk
import tkinter.messagebox as tkmsb

class MenuBar(tk.Menu):
    def __init__(self, root):
        super().__init__(root)

        self.file_menu = tk.Menu(self, tearoff=0)
        self.file_menu.add_command(label="New simulation", command=self.soon)
        self.file_menu.add_command(label="Open simulation", command=self.soon)
        self.file_menu.add_command(label="Save simulation", command=self.soon)
        self.file_menu.add_command(label="Save as...", command=self.soon)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Quit", command=self.soon)
        self.add_cascade(label="Fichier", menu=self.file_menu)

        self.body_menu = tk.Menu(self, tearoff=0)
        self.body_menu.add_command(label="New body", command=self.soon)
        self.body_menu.add_command(label="Modify body", command=self.soon)
        self.body_menu.add_command(label="Rename body", command=self.soon)
        self.body_menu.add_command(label="Delete body", command=self.soon)
        self.add_cascade(label="Body", menu=self.body_menu)

        self.help_menu = tk.Menu(self, tearoff=0)
        self.help_menu.add_command(label="About", command=self.about)
        self.add_cascade(label="Help", menu=self.help_menu)

    def soon(self):
        print("Hello !")

    def about(self):
        tkmsb.showinfo("About Gravit", "Gravit v0.1\nGravit is a simulator based on the Newton's gravity.")

class Launcher(tk.Tk):
    def __init__(self):
        super().__init__()

        self.menubar = MenuBar(self)
        self.config(menu=self.menubar)

l = Launcher()

l.mainloop()
