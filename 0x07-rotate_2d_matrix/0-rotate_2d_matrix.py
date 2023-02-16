def rotate_2d_matrix(matrix):
    n = len(matrix)
    # Transpose the matrix (rows become columns, columns become rows)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row to rotate clockwise
    for i in range(n):
        matrix[i] = matrix[i][::-1]
