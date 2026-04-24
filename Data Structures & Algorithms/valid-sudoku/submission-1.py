class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        assert len(board) == 9
        for line in board:
            assert len(line) == 9

        for i in range(9):
            line = board[i]
            if not self.isValidLineColumnOrSquare(line):
                return False

            column = [line[i] for line in board]
            if not self.isValidLineColumnOrSquare(column):
                return False

            sq_l = (i // 3) * 3
            sq_c = (i % 3) * 3
            square = [
                element
                for line in board[sq_l : sq_l + 3]
                for element in line[sq_c : sq_c + 3]
            ]
            if not self.isValidLineColumnOrSquare(square):
                return False

        return True

    def isValidLineColumnOrSquare(self, values: list[str]) -> bool:
        empty_count = values.count(".")
        values_set = set(values)
        values_set.remove(".")

        return len(values_set) == len(values) - empty_count


if __name__ == "__main__":
    board = [
        ["1", "2", ".", ".", "3", ".", ".", ".", "."],
        ["4", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", ".", "3"],
        ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
        [".", ".", ".", "8", ".", "3", ".", ".", "5"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", ".", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "8"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert Solution().isValidSudoku(board)

    board = [
        ["1", "2", ".", ".", "3", ".", ".", ".", "."],
        ["4", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", "9", "1", ".", ".", ".", ".", ".", "3"],
        ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
        [".", ".", ".", "8", ".", "3", ".", ".", "5"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", ".", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "8"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert not Solution().isValidSudoku(board)
