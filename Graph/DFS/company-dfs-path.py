def can_escape(maze):
    """
    Given a maze represented as a 2D list, where 1 represents a path and
    0 represents a wall, determine if there is a path from the top row to
    the bottom row. The user can move in four directions: up, down, left,
    and right. The user can only move through cells with a value of 1.
    The function returns True if there is a path from the top row to the
    bottom row, and False otherwise.
    """

    if len(maze) == 0:
        return False
    
    rows, cols = len(maze), len(maze[0])
    directions = [(0,1), (0,-1), (1,0), (-1, 0)]
    visited = set()

    def is_inbound(row, col):
        if row >= 0 and row < rows and col >= 0 and col < cols:
            return True
        return False


    def dfs(row, col):
        visited.add((row,col))
        if is_inbound(row, col) and maze[row][col] == 1:
            if row == rows-1:
                return True
            for dx, dy in directions:
                nextRow, nextCol = row + dx, col + dy
                if (nextRow, nextCol) not in visited and dfs(nextRow, nextCol):
                    return True
        return False

    row = 0
    for col in range(cols):
        visited.clear()
        visited.add((row,col))
        if maze[row][col] == 1:
            # print(f" begin with maze[{row}][{col}]:{maze[row][col]}")
            for dx, dy in directions:
                nextRow, nextCol = row + dx, col + dy
                if (nextRow, nextCol) not in visited and dfs(nextRow, nextCol):
                    return True
                
    return False


# Test cases
if __name__ == "__main__":
    maze1 = [
        [1, 0, 0, 0, 1],
        [0, 0, 0, 1, 1],
        [0, 1, 1, 1, 0],
        [1, 0, 1, 0, 0],
        [1, 0, 0, 0, 1],
    ]

    maze2 = [
        [1, 0, 0, 0, 1],
        [0, 0, 0, 1, 1],
        [0, 1, 1, 1, 0],
        [1, 0, 1, 0, 0],
        [1, 0, 1, 0, 1],
    ]

    assert can_escape(maze1) == False, "maze1 user cannot escape"
    assert can_escape(maze2) == True, "maze2 user can escape"

    print("All tests passed!")