def worker(grid):

    rows = len(grid)
    cols = len(grid[0])
    stk = []
    islands = 0
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for row in range(rows):
        for col in range(cols):

            if grid[row][col] == '1':

                islands += 1
                grid[row][col] = '0'
                stk.append((row, col))

                while stk:
                    r, c = stk.pop()
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                            grid[nr][nc] = '0'
                            stk.append((nr, nc))
    
    return islands
