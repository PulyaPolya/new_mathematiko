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