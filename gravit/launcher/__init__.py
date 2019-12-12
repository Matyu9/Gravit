import tkinter as tk
import tkinter.messagebox as tkmsb
import webbrowser as wb

class MenuBar(tk.Menu):
    def __init__(self, root):
    	#init of the super-class
        super().__init__(root)


		## File Menu
        self.file_menu = tk.Menu(self, tearoff=0)

        self.file_menu.add_command(label="New simulation", command=self.master.soon)
        self.file_menu.add_command(label="Open simulation...", command=self.master.soon)
        self.file_menu.add_command(label="Save simulation", command=self.master.soon)
        self.file_menu.add_command(label="Save as...", command=self.master.soon)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Quit", command=self.master.soon)

        self.add_cascade(label="Fichier", menu=self.file_menu)

        self.add_command(label="|")

        self.body_menu = tk.Menu(self, tearoff=0)

        self.body_menu.add_command(label="New body", command=self.master.soon)
        self.body_menu.add_command(label="Modify body", command=self.master.soon)
        self.body_menu.add_command(label="Rename body", command=self.master.soon)
        self.body_menu.add_command(label="Delete body", command=self.master.soon)

        self.add_cascade(label="Body", menu=self.body_menu)

        self.add_command(label="|")

        self.add_command(label="Advanced Options", command=self.master.soon)

        self.add_command(label="|")

        self.help_menu = tk.Menu(self, tearoff=0)

        self.help_menu.add_command(label="About", command=self.about)
        self.add_cascade(label="Help", menu=self.help_menu)

    def about(self):
        tkmsb.showinfo("About Gravit", "Gravit v0.1\nGravit is a simulator based on the Newton's gravity.")

class BodyFrame(tk.Frame):
	def __init__(self, root, body):
	     super().__init__(root)

class Launcher(tk.Tk):
    #show an "coming soon" window'
    def soon(self):
        tkmsb.showwarning("Sorry...", "This feature will coming soon ! :(", parent=self.master)

    def askplay(self):
    	if tkmsb.askyesno("Start Simulation", "Do you want to start the Gravit simulation ?"):
    	    pass

    def ghpage():
    	wb.new("https://github.com/anat3000/Gravit")

    def __init__(self, sim_to_launch=None):
        #init of the super-class
        super().__init__()

        #some properties of the launcher
        self.geometry("960x720")

        #set the simulation which will launched (it's a launcher, no ?')
        self.sim_to_launch = sim_to_launch
        #menu bar
        self.menubar = MenuBar(self)
        self.config(menu=self.menubar)
        # play button
        self.play_button = tk.Button(self, text="Start the simulation", height=5, command=self.askplay)
        self.play_button.pack(side="bottom", fill="x")


l = Launcher()

l.mainloop()
