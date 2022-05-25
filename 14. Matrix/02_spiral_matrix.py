def spiralOrder(matrix):
    result = []
    rows = len(matrix)
    cols = len(matrix[0])

    min_row, min_col = 0, 0
    max_row, max_col = len(matrix) - 1, len(matrix[0]) - 1

    while min_row <= max_row and min_col <= max_col:
        #top row
        for col in range(min_col, max_col + 1):
            result.append(matrix[min_row][col])

        #right col
        for row in range(min_row + 1, max_row + 1):
            result.append(matrix[row][max_col])

        #bottom row
        for col in range(max_col - 1, min_col - 1, - 1):
            if min_row == max_row:
                break
            result.append(matrix[max_row][col])

        #left col
        for row in range(max_row - 1, min_row, -1):
            if min_col == max_col:
                break
            result.append(matrix[row][min_col])

        min_row += 1
        max_row -= 1
        min_col += 1
        max_col -= 1

    # print(result)
    return result

if __name__ == "__main__":
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    result = spiralOrder(matrix)
    print(result)  