#!/usr/bin/python3
from sys import argv

"""
This modules finds all solutions for N queens problem
"""


class NQueensSolver:
    """
    Class to solve the N-Queens problem.
    """

    def __init__(self, n):
        """
        Initialize the N-Queens solver.

        Args:
            n (int): The size of the chessboard and the number of queens.
        """
        self.n = n
        self.board = [-1] * n

    def is_safe(self, row, col):
        """
        Check if it's safe to place a queen at a given position.

        Args:
            row (int): The row of the chessboard.
            col (int): The column of the chessboard.

        Returns:
            bool: True if it's safe to place a queen, False otherwise.
        """
        for i in range(row):
            if self.board[i] == col or \
               self.board[i] - i == col - row or \
               self.board[i] + i == col + row:
                return False
        return True

    def solve_util(self, row):
        """
        Recursive function to find solutions to the N-Queens problem.

        Args:
            row (int): The current row being considered.

        Returns:
            None
        """
        if row == self.n:
            self.print_solution()
            return

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row] = col
                self.solve_util(row + 1)

    def solve(self):
        """
        Public method to initiate the solving process.

        Returns:
            None
        """
        self.solve_util(0)

    def print_solution(self):
        """
        Print the current solution.

        Returns:
            None
        """
        solution = [[i, self.board[i]] for i in range(self.n)]
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 101-nqueens.py N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solver = NQueensSolver(N)
    solver.solve()
    
