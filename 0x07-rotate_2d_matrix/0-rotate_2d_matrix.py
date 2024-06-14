def rotate_2d_matrix(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        for i in range(layer, n - layer - 1):
            temp = matrix[layer][i]
            matrix[layer][i] = matrix[n - 1 - i][layer]
            matrix[n - 1 - i][layer] = matrix[n - 1 - layer][n - 1 - i]
            matrix[n - 1 - layer][n - 1 - i] = matrix[i][n - 1 - layer]
            matrix[i][n - 1 - layer] = temp
