#!/usr/bin/python3
def island_perimeter(grid):
    # initialize perimeter to 0
    perimeter = 0

    # loop over the rows and columns of the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # if the cell is land, add its perimeter to the overall perimeter
            if grid[i][j] == 1:
                # check left neighbor
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # check right neighbor
                if j == len(grid[0])-1 or grid[i][j+1] == 0:
                    perimeter += 1
                # check top neighbor
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # check bottom neighbor
                if i == len(grid)-1 or grid[i+1][j] == 0:
                    perimeter += 1

    # return the overall perimeter
    return perimeter
