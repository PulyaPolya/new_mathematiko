import tkinter as tk

class Button:
    def __init__(self, root, x, y, random, matrix,result, g_settings):
        self.root = root
        self.random = random
        self.x = x
        self.y = y
        self.matrix = matrix
        self.text = tk.StringVar()
        self.result = result

        self.button = tk.Button(self.root, textvariable=self.text,  height = 4, width = 10,
                                 command=lambda:self.changeText(self.random))
        self.button.place(x=self.x*100, y=self.y*100)
        self.pressed = 0


    def changeText(self, random):
        self.state = 1
        if self.pressed == 0:
            self.text.set(random.number)
            self.pressed = 1
            self.matrix.matrix[self.y][self.x] = random.number
            self.matrix.counter += 1
            if self.matrix.counter == 25:
                self.result.score = self.matrix.count_points()
                self.result.show_label()

            random.change_number()


    def reset(self):
        self.pressed = 0
        self.text.set('')






