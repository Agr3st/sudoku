EMPTY_SPACE = '.'

class InvalidMoveError(Exception):
    pass

class Sudoku:
    def __init__(self):
        self.board = self.generate_board()

    @staticmethod
    def generate_board():
        # return [[EMPTY_SPACE for _ in range(9)] for _ in range(9)]
        return [
            [3, EMPTY_SPACE, EMPTY_SPACE, 9, EMPTY_SPACE, EMPTY_SPACE, EMPTY_SPACE, 6, 2],
            [EMPTY_SPACE, 5, EMPTY_SPACE, 3, 6, EMPTY_SPACE, 7, EMPTY_SPACE ,9],
            [EMPTY_SPACE, EMPTY_SPACE, EMPTY_SPACE, EMPTY_SPACE, EMPTY_SPACE, EMPTY_SPACE, 5, 8, EMPTY_SPACE],
            [EMPTY_SPACE, 6, EMPTY_SPACE, 4, EMPTY_SPACE, 9, 8, EMPTY_SPACE, EMPTY_SPACE],
            [9, EMPTY_SPACE, 8, 5, 2, EMPTY_SPACE, 4, 1, 6],
            [5, 2, 4, 1, EMPTY_SPACE, 6, EMPTY_SPACE, EMPTY_SPACE, EMPTY_SPACE],
            [8, EMPTY_SPACE, EMPTY_SPACE, EMPTY_SPACE, EMPTY_SPACE, 1, 2, 7, EMPTY_SPACE],
            [EMPTY_SPACE, 9, EMPTY_SPACE, EMPTY_SPACE, EMPTY_SPACE, EMPTY_SPACE, EMPTY_SPACE, 5, EMPTY_SPACE],
            [7, 1, 6, 2, 4, 5, EMPTY_SPACE, 9, EMPTY_SPACE],
        ]

    def display(self):
        """
        prints board in terminal
        """
        print("   ", end="")
        for i in range(9):
            print(f" {i+1} ", end="")
            if (i+1) % 3 == 0:
                print(" ", end="")
        print()
        print("   ", end="")
        for i in range(9):
            print(f" _ ", end="")
            if (i + 1) % 3 == 0:
                print(" ", end="")
        print()
        for i in range(9):
            print(f"{i+1} | ", end="")
            for j in range(9):
                print(f" {self.board[i][j]} ", end="")
                if (j+1) % 3 == 0 and j != 8:
                    print("|", end="")
            if (i + 1) % 3 == 0 and i != 8:
                print("\n    ", end="")
                for _ in range(28):
                    print('-', end="")
            print()

    def validate_move(self, r, c, num, ignore_current=False):
        """
        Check if number isn't already in same row/column/square.
        :param r: row, 1 <= r <= 10
        :param c: column, 1 <= c <= 10
        :param num: number to be checked
        :param ignore_current: True if num already is placed at position (r, c)
        :return: True if there is no such number in row/col/square, else False.
        """
        # check if args are valid
        if not isinstance(num, int):
            return False
        if not all(1 <= val <= 10 for val in [r, c, num]):
            return False

        # check if num is already in row
        for col in range(9):
            if self.board[r-1][col] == num and (ignore_current is False or col != c-1):
                return False

        # check if num is already in col
        for row in range(9):
            if self.board[row][c-1] == num and (ignore_current is False or row != r-1):
                return False

        # defining indexes of left upper corner for the specific square
        # 0 <= sr, sc <= 9
        sr = r - (r + 2) % 3 - 1
        sc = c - (c + 2) % 3 - 1

        # check if num is already in square 3x3
        for x in range(sr, sr+3):
            for y in range(sc, sc+3):
                if self.board[x][y] == num and (ignore_current is False or (x != r-1 or y != c-1)):
                    return False

        return True

    def is_valid_board(self):
        """
        Check every row, column and square for repeated numbers.
        :return: True if there is no repetition, else False.
        """
        for r in range(9):
            for c in range(9):
                if self.board[r][c] != EMPTY_SPACE:
                    if not self.validate_move(r+1, c+1, self.board[r][c], ignore_current=True):
                        return False
        return True

    def add_number(self, r, c, num):
        if not self.validate_move(r, c, num):
            raise InvalidMoveError
        self.board[r-1][c-1] = num

    def is_empty_space(self):
        for row in self.board:
            if EMPTY_SPACE in row:
                return True
        return False

    def is_win(self):
        if not self.is_empty_space() and self.is_valid_board():
            return True
        return False

    def game(self):
        while True:
            self.display()
            print("Add number:")
            r = int(input("row = "))
            c = int(input("col = "))
            num = int(input("num = "))
            try:
                self.add_number(r, c, num)
            except InvalidMoveError:
                print("Invalid arguments, try again.")
            else:
                if self.is_win():
                    self.display()
                    print("Congratulations, you did it!")
                    break

