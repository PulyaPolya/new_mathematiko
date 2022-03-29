import numpy as np

import win_combinations as w
class Matrix:
    def __init__(self, g_settings):
        self.g_setttings = g_settings
        self.size = 5
        self.matrix = self.fill_matrix_with_zero()
        self.counter = 0

    def fill_matrix_with_zero(self):
        matrix = []
        for j in range(5):
            row = []
            for i in range(self.size):
                row.append(0)
            matrix.append(row)
        return matrix

    def np_to_arr(self, col):
        array = []
        for elem in col:
            array.append(elem)
        return array

    def count_points(self):
        self.matrix = np.array(self.matrix)
        sum = 0
        for i in range(len(self.matrix)):
            arr = self.np_to_arr(self.matrix[i])
            d = w.count_row(arr)
            sum += d
        for j in range(len(self.matrix)):
            arr = self.np_to_arr(self.matrix[:, j])
            d = w.count_row(arr)
            sum += d

        diag_1 = []
        for i in range(len(self.matrix)):
            diag_1.append(self.matrix[i][i])
        sum += w.count_row(diag_1, 1)
        diag_2 = []
        for j in range(len(self.matrix) - 1, -1, -1):
            diag_2.append(self.matrix[j][len(self.matrix) - j - 1])
        sum += w.count_row(diag_2, 1)
        return sum