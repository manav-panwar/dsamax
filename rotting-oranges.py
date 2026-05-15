from collections import deque

def worker(grid):
    time = -1
    fresh_or = 0
    rows = len(grid)
    cols = len(grid[0])
    q = deque()

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 2:
                q.append((row, col))
            elif grid[row][col] == 1:
                fresh_or += 1

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        for _ in range(len(q)):
            r, c = q.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_or -= 1
                    q.append((nr, nc))

        time += 1

    return time if fresh_or == 0 else -1