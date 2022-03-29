import tkinter as tk

class ResultWindow:
    def __init__(self, root):
        self.root = root
        self.score = 0
        self.label = tk.Label(self.root, text='your score is \n' + str(self.score),
                              height=4, width=10)
        self.label.place(x=600, y=300)
        self.label.place_forget()
        #self.label.pack_forget()
        #self.show_label = 0

    def show_label(self):
        self.label = tk.Label(self.root, text='your score is \n' + str(self.score),
                              height=4, width=10)
        self.label.place(x=600, y=300)
    def hide_label(self):
        self.label.place_forget()