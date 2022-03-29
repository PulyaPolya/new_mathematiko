import random
import tkinter as tk


class Random:
    def __init__(self, root,g_settings):
        self.dict = {}
        for i in range(1, 14):
            self.dict[i] = 0
        self.number = self.get_random_number()
        self.root = root
        self.text = tk.StringVar()
        self.text.set(self.number)
        self.label = tk.Label(self.root, textvariable=self.text, height=g_settings.random_label_h,
                              width=g_settings.random_label_w).place(x=g_settings.random_label_x, y=g_settings.random_label_y)
        #self.label.config(height = 3, width=5)
        #self.label.pack()
    def get_random_number(self):
        number = random.randint(1, 13)
        while self.dict[number] >= 4:
            number = random.randint(1, 13)
        self.dict[number] += 1
        self.number = number
        return number

    def change_number(self):
        self.get_random_number()
        self.text.set(self.number)
    def reset(self):
        self.dict = {}
        for i in range(1, 14):
            self.dict[i] = 0