def islandPerimeter(grid):
    rows = len(grid)
    cols = len(grid[0])

    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4

                if row > 0 and grid[row-1][col] == 1:
                    perimeter -= 2

                if col > 0 and grid[row][col-1] == 1:
                    perimeter -= 2

    return perimeter

if __name__ == "__main__":
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    result = islandPerimeter(grid)
    print(result)