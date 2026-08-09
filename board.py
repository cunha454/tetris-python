class Board:
    def __init__(self):
        self.board = [[0] * 10 for _ in range(20)]

    def occupy(self, line, column):
        self.board[line][column] = 1

    def is_occupied(self, line, column):
        return self.board[line][column] == 1

    def is_inside(self, line, column):
        return 0 <= line < 20 and 0 <= column < 10

    def count_cells_in_line(self, line):
        line_score = 0

        for cell in self.board[line]:
            if cell == 1:
                line_score += 1

        return line_score

    def is_line_complete(self, line):
        return self.count_cells_in_line(line) == 10

    def remove_line(self, line):
        self.board.pop(line)

    def add_empty_line(self):
        self.board.insert(0, [0] * 10)

    def clear_lines(self):
        complete_lines = []

        for line in range(19, -1, -1):
            if self.is_line_complete(line):
                complete_lines.append(line)

        for line in complete_lines:
            self.remove_line(line)

        for _ in complete_lines:
            self.add_empty_line()

    def is_position_valid(self, line, column):
        return self.is_inside(line, column) and not self.is_occupied(line, column)

    def is_piece_position_valid(self, shape, upper_corner_piece_line, upper_corner_piece_column):
        for position_relative_shape_line in range(len(shape)):
            for position_relative_shape_column in range(len(shape[position_relative_shape_line])):
                if shape[position_relative_shape_line][position_relative_shape_column] == 1:

                    board_line = upper_corner_piece_line + position_relative_shape_line
                    board_column = upper_corner_piece_column + position_relative_shape_column

                    if not self.is_position_valid(board_line, board_column):
                        return False

        return True


board = Board()

shape = [
    [0, 1, 0],
    [1, 1, 1]
]

print(board.is_piece_position_valid(shape, 5, 3))

print(board.is_piece_position_valid(shape, 5, 8))

board.occupy(6, 5)

print(board.is_piece_position_valid(shape, 5, 3))