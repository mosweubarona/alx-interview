#!/usr/bin/python3
import sys


def is_valid(board, row, col, n):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve(board, row, n, results):
    if row == n:
        result = []
        for i in range(n):
            result.append([i, board[i]])
        results.append(result)
        return
    for col in range(n):
        if is_valid(board, row, col, n):
            board[row] = col
            solve(board, row + 1, n, results)


def nqueens(n):
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [-1] * n
    results = []
    solve(board, 0, n, results)
    return results


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    results = nqueens(n)
    for result in results:
        print(result)
