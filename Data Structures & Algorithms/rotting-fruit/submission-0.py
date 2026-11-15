class Solution:
    def isSafe(self, i, j, n, m):
        return 0 <= i < n and 0 <= j < m

    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        queue = deque()

        time = 0 

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue: 
            size = len(queue)
            flag = False 

            for i in range(size):
                x, y = queue.popleft()

                for dx, dy in directions: 
                    nx, ny = x + dx, y + dy

                    if self.isSafe(nx, ny, n, m) and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        flag = True

            if flag: 
                time += 1 
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1: 
                    return -1 

        return time
        