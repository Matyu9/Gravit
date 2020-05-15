import tkinter as tk
import tkinter.font as tkFont

class BodyFrame(tk.LabelFrame):
	def __init__(self, root, body=None):
		super().__init__(root, text="Bodies")
		self.coming_soon_label = tk.Label(self, text="COMING SOON...\nJust push \"Start the simulation\" button.",
										  font=tkFont.Font(size=30),
										  anchor=tk.N
										  )
		self.coming_soon_label.grid()