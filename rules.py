from tkinter import *
from PIL import ImageTk, Image

class Rules():
    def __init__(self, newWindow):
        self.newWindow = newWindow
        self.canvas = Canvas(self.newWindow, width=1000, height=1000)
    def display(self):
        self.img = ImageTk.PhotoImage(Image.open("rules1.jpg"))

        self.canvas.create_image(0, 0, anchor=NW, image=self.img)
        self.canvas.image = self.img
        self.canvas.pack()