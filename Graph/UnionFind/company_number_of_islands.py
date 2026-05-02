# Example grid containing 3 blobs (labels are for ease of reading only)
#
# grid = [
#     "00010", # | | | |A| |
#     "01101", # | |B|B| |B|
#     "00111", # | | |B|B|B|
#     "11010", # |C|C| |B| |
#     "11000"  # |C|C| | | |
# ]

def solution(grid, minimumSize):
    n = 0

    visits = set()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # print(f"grid[{i}][{j}]: {grid[i][j]}")
            if grid[i][j] == '1' and (i,j) not in visits:
                # print(f"visits[{i}][{j}]: {visits}")
                size = 0
                f(grid, i, j, visits, size)
                if size >= minimumSize:
                    n += 1
                
    return n

def f(grid, i, j, visits, size):
    
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or (i,j) in visits:
        return

    visits.add((i,j))

    if grid[i][j] == '1':
        size += 1
        f(grid, i - 1, j,     visits, size)
        f(grid, i + 1, j,     visits, size)
        f(grid, i,     j - 1, visits, size)
        f(grid, i,     j + 1, visits, size)
    
    return

    
