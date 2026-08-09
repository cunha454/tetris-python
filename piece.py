class Piece:
    def __init__(self, shape, line, column):
        self.shape = shape
        self.line = line
        self.column = column

    def move_right(self):
        self.column += 1

    def move_left(self):
        self.column -= 1

    def move_down(self):
        self.line += 1

# len(shape)     → quantidade de linhas
# len(shape[0])  → quantidade de colunas

    def preview_rotation_right(self):
        new_shape = [[0] * len(self.shape) for _ in range(len(self.shape[0]))]

        for line in range(len(self.shape)):
            for column in range(len(self.shape[line])):
                new_shape[column][len(self.shape[0]) - 1 - line] = self.shape[line][column]

        return new_shape

    def rotate_right(self, new_shape):
        self.shape = new_shape