import tkinter as tk
from PIL import ImageTk, Image
import game_function as gf
from button import Button

class Game:
    def __init__(self, root, g_settings, matrix, random, result, arr_buttons):
        self.root = root
        self.g_settings = g_settings
        self.matrix = matrix
        self.random = random
        self.arr_buttons = arr_buttons
        self.img_rules = ImageTk.PhotoImage(Image.open("rules_button.png"))
        self.img_restart = ImageTk.PhotoImage(Image.open("restart_button2.png"))
        self.result = result
        self.positions = gf.get_square_positions()
        '''
        self.img_start = ImageTk.PhotoImage(Image.open("play.png"))
        self.play = tk.Button(self.root, image=self.img_start, borderwidth=0,
                         command=lambda: gf.start(self.root, self.g_settings, self.arr_buttons))
        self.play.place(x=self.g_settings.restart_button_x, y=self.g_settings.restart_button_y)
        '''
    def show_squares(self):
        for pair in self.positions:
            b = Button(self.root, pair[0], pair[1], self.random, self.matrix, self.result, self.g_settings)
            button_number = str(str(pair[0]) + str(pair[1]))
            self.arr_buttons.append(b)

    def show_butt_rules(self):
        self.show_rules_button = tk.Button(self.root, image=self.img_rules, borderwidth=0,
                                           command=lambda: gf.show_rules(self.root))
        self.show_rules_button.place(x=self.g_settings.rules_button_x, y=self.g_settings.rules_button_y)


    def show_butt_restart(self):
        self.restart_button = tk.Button(self.root, image=self.img_restart, borderwidth=0,
                                        command=lambda: gf.restart(self.arr_buttons, self.g_settings))
        self.restart_button.place(x=self.g_settings.restart_button_x, y=self.g_settings.restart_button_y)
        
