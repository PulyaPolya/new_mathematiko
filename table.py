from matrix import Matrix

class Table:
    def __init__(self, g_settings):
        self.matrix = Matrix(g_settings).matrix
        self.counter = 0

