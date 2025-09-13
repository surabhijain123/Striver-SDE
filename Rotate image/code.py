def rotate_matrix(mat):
    n = len(mat)

    for i in range((n//2)):
        for j in range(i, n - i - 1):
            mat[i][j], mat[j][n-1-i], mat[n-1-i][n-1-j], mat[n-1-j][i] = mat[n-1-j][i], mat[i][j], mat[j][n-1-i], mat[n-1-i][n-1-j]
    return mat