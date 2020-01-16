import tkinter as tk
# nb: bien mettre le tkinter.messagebox, il n'est PAS importé par défaut !
import tkinter.messagebox

class MenuBar(tk.Menu):
    def __init__(self, root):
    	#init of the super-class
        super().__init__(root)


        ## File Menu
        self.simulation_menu = tk.Menu(self, tearoff=0)

        self.simulation_menu.add_command(label="New simulation", command=self.master.soon)
        self.simulation_menu.add_command(label="Play simulation", command=self.master.play_sim)
        self.simulation_menu.add_command(label="Pause simulation", command=self.master.pause_sim)
        self.simulation_menu.add_command(label="Stop simulation", command=self.master.stop_sim)
        self.simulation_menu.add_separator()
        self.simulation_menu.add_command(label="Quit launcher", command=self.master.destroy)

        self.add_cascade(label="Fichier", menu=self.simulation_menu)

        self.body_menu = tk.Menu(self, tearoff=0)

        self.body_menu.add_command(label="New body", command=self.master.soon)
        self.body_menu.add_command(label="Modify body", command=self.master.soon)
        self.body_menu.add_command(label="Rename body", command=self.master.soon)
        self.body_menu.add_command(label="Delete body", command=self.master.soon)

        self.add_cascade(label="Body", menu=self.body_menu)

        self.add_command(label="Advanced Options", command=self.master.soon)

        self.help_menu = tk.Menu(self, tearoff=0)

        self.help_menu.add_command(label="About", command=self.about)
        self.add_cascade(label="Help", menu=self.help_menu)

    def about(self):
        tk.messagebox.showinfo("About Gravit", "Gravit v0.1\nGravit is a simulator based on the Newton's gravity.")
