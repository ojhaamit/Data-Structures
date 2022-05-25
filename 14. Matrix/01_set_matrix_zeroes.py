def setMatrixZeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    rows_idx, cols_idx = set(), set()

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                rows_idx.add(i)
                cols_idx.add(j)

    for i in range(rows):
        for j in range(cols):
            if i in rows_idx or j in cols_idx:
                matrix[i][j] = 0

    return matrix

if __name__ == "__main__":
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    result = setMatrixZeroes(matrix)
    print(result)