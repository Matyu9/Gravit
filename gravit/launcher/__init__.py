import tkinter as tk
import webbrowser as wb

from .menubar import MenuBar
from .bodyframe import BodyFrame

class Launcher(tk.Tk):
    #show an "coming soon" window'
    def soon(self):
        #tk.messagebox.showwarning("Sorry...", "This feature will coming soon ! :(", parent=self.master)
        pass

    def askplay(self):
    	#if tk.messagebox.askyesno("Start Simulation", "Do you want to start the Gravit simulation ?"):
        self.simulation.start()

    def ghpage():
    	wb.new("https://github.com/anat3000/Gravit")

    def __init__(self, sim_to_launch):
        #init of the super-class
        super().__init__()

        #some properties of the launcher
        self.geometry("960x720")

        #set the simulation which will launched (it's a launcher, no ?')
        self.simulation = sim_to_launch
        #menu bar
        self.menubar = MenuBar(self)
        self.config(menu=self.menubar)
        # play button
        self.play_button = tk.Button(self, text="Start the simulation", height=5, command=self.askplay)
        self.play_button.pack(side="bottom", fill="x")

