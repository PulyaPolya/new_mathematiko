import tkinter as tk
from tkinter import *
import game_function as gf
from settings import Settings
from matrix import  Matrix
from PIL import ImageTk, Image
global img
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

root = tk.Tk()
g_settings = Settings(root)
arr_buttons = []
welcome_label = Label(root, text = "Welcome to mathematiko!", fg = '#ffffff', bg=g_settings.bg_color)
welcome_label.config(font =("Courier", 20))
welcome_label.place(x = g_settings.welcome_label_x , y = g_settings.welcome_label_y)
game = gf.init_game(g_settings, root,arr_buttons)
img_start = ImageTk.PhotoImage(Image.open("play.png"))
play = tk.Button(root, image=img_start,borderwidth = 0,
                                 command=lambda:gf.start(game, play,welcome_label ))
play.place(x=g_settings.play_button_x, y=g_settings.play_button_y)

matrix = Matrix(g_settings)

root.geometry(g_settings.size)
root.config(bg=g_settings.bg_color)
positions = gf.get_square_positions()

root.mainloop()
