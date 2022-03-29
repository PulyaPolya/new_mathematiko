
import tkinter as tk
from tkinter import *
import game_function as gf
from random_number import Random
from button import Button
from settings import Settings
from matrix import  Matrix
from result_window import ResultWindow
from PIL import ImageTk, Image
from rules import Rules
global img
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)


g_settings = Settings()
matrix = Matrix(g_settings)
root = tk.Tk()
root.geometry(g_settings.size)
root.config(bg=g_settings.bg_color)
positions = gf.get_square_positions()
dict_buttons = {}
arr_buttons = []
random = Random(root, g_settings)
result = ResultWindow(root)
for pair in positions:
    b = Button(root, pair[0], pair[1], random, matrix, result, g_settings)
    button_number = str(str(pair[0]) + str(pair[1]))
    dict_buttons[button_number] = b
    arr_buttons.append(b)
img_rules = ImageTk.PhotoImage(Image.open("rules_button.png"))
show_rules_button = tk.Button(root, image=img_rules,borderwidth = 0,
                                 command=lambda:show_rules())
show_rules_button.place(x=g_settings.rules_button_x, y=g_settings.rules_button_y)
img_restart = ImageTk.PhotoImage(Image.open("restart_button2.png"))
restart_button = tk.Button(root, image=img_restart,borderwidth = 0,
                                 command=lambda:restart(arr_buttons,g_settings))
restart_button.place(x=g_settings.restart_button_x, y=g_settings.restart_button_y)
#print(matrix.counter)
def show_rules():
    newWindow = Toplevel(root)
    newWindow.title("New Window")
    newWindow.geometry("450x350")
    #newWindow.config(bg=g_settings.bg_color)
    rules = Rules(newWindow)
    rules.display()

def restart(arr_buttons,g_settings):
    new_matrix = Matrix(g_settings)
    for button in arr_buttons:
        button.reset()
        button.matrix = new_matrix
        button.result.hide_label()
        button.random.reset()

root.mainloop()
