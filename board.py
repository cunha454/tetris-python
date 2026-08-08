class Board:
    def __init__(self):
        self.board =[[0] * 10 for _ in range(20)]

    def occupy(self, line, column):
        self.board[line][column] = 1

    def is_occupied(self, line, column):
        return self.board[line][column] == 1 # x = 1 => True / x = 0 => False

    def count_cells_in_line(self, line):
        line_score = 0

        for cell in self.board[line]:
            if cell == 1:
                line_score += 1

        return line_score

    def is_line_complete(self, line):
        return self.count_cells_in_line(line) == 10 # x = 10 => True

    def remove_line(self, line):
        self.board.pop(line) # "pop" remove a linha

    def add_empty_line(self):
        self.board.insert(0, [0] * 10) # adiciona uma lista no início da lista

    def clear_lines(self):
        complete_lines = []

        for line in range(19, -1, -1):
            if self.is_line_complete(line):
                complete_lines.append(line)

        for line in complete_lines:
            self.remove_line(line)

        for _ in complete_lines:
            self.add_empty_line()


board = Board()

for column in range(10):
    board.occupy(19, column)

print(board.is_line_complete(19))

board.clear_lines()

print(board.is_line_complete(19))
