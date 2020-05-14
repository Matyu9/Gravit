import tkinter as tk
import tkinter.messagebox
import webbrowser as wb

from .menubar import MenuBar
from .bodyframe import BodyFrame
from .. import simulation

class Launcher(tk.Tk):
    def soon(self):
        tk.messagebox.showwarning("Sorry...", "This feature will coming soon ! :(")

    def sim_is_alive(self):
        try:
            return self.simulation.is_alive()
        except AttributeError:
            return False

    def askplay(self):
        if tk.messagebox.askyesno("Start Simulation", "Do you want to start the Gravit simulation ?") and (not self.sim_is_alive()):
            self.simulation = simulation.Simulation()
            self.simulation.start()


    def play_sim(self):
        if self.sim_is_alive():
            self.simulation.do_play()

    def pause_sim(self):
        if self.sim_is_alive():
            self.simulation.do_pause()

    def stop_sim(self):
        if self.sim_is_alive():
            self.simulation.do_stop()
            

    def ghpage(self):
        wb.new("https://github.com/anatom3000/Gravit")

    def __init__(self):
        #init of the super-class
        super().__init__()

        #some properties of the launcher
        self.geometry("960x720")
        self.title("Gravit Launcher")


        #menu bar
        self.menubar = MenuBar(self)
        self.config(menu=self.menubar)
        # play button
        self.play_button = tk.Button(self, text="Start the simulation", height=5, command=self.askplay)
        self.play_button.pack(side="bottom", fill="x")

