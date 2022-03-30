import tkinter as tk
from tkinter import *
from rules import Rules
from matrix import  Matrix
from PIL import ImageTk, Image
from game import Game
from random_number import Random
from result_window import ResultWindow
def get_square_positions():
    arr = []
    x = 0
    y = 0
    for j in range(5):
        for i in range(5):
            position = []
            position.append(y)
            position.append(x)
            arr.append(position)
            x += 1
        x = 0
        y += 1
    return arr
print(get_square_positions())

def show_rules(root):
    newWindow = Toplevel(root)
    newWindow.title("New Window")
    newWindow.geometry("450x350")
    rules = Rules(newWindow)
    rules.display()

def restart(arr_buttons,g_settings):
    new_matrix = Matrix(g_settings)
    for button in arr_buttons:
        button.reset()
        button.matrix = new_matrix
        button.result.hide_label()
        button.random.reset()

def start(game, button, welcome_label):
   game.show_squares()
   game.show_butt_restart()
   game.show_butt_rules()
   button.place_forget()
   welcome_label.place_forget()
   game.random.show_random_label()

def init_game(g_settings, root, arr_buttons):
    matrix = Matrix(g_settings)
    random = Random(root, g_settings)
    result = ResultWindow(root)
    game = Game(root, g_settings, matrix, random, result, arr_buttons)
    return game
