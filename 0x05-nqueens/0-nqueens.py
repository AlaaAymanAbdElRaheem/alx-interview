#!/usr/bin/env python3
"""placing N non-attacking queens on an N×N chessboard"""

import sys


def is_valid(board: list, row: int, col: int) -> bool:
    """checks if a queen can be placed on board at row and col"""

    """if there is a queen on the left"""
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    """if there is a queen on the upper left diagonal"""
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    """if there is a queen on the lower left diagonal"""
    i, j = row + 1, col - 1
    while i < len(board) and j >= 0:
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1

    return True


def n_queens(borad: list, n: int, col: int, result: list) -> None:
    """prints every possible solution to the problem"""

    """best case scenario"""
    if col == n:
        print(result)
        return

    """recursive call to check for all possible solutions"""
    for i in range(n):
        if is_valid(board, i, col):
            board[i][col] = 'Q'
            result.append([i, col])
            n_queens(board, n, col + 1, result)
            board[i][col] = 0
            result.pop()


if __name__ == "__main__":
    """main function"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    elif int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    n = int(sys.argv[1])
    board = [[0 for i in range(n)] for j in range(n)]
    result = []
    n_queens(board, n, 0, result)
