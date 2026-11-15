class Solution:
    def isInside(self, grid, row, column, visited):
        n = len(grid)
        m = len(grid[0])

        return (0 <= row < n and 0 <= column < m and grid[row][column] == '1' and not visited[row][column])

    def dfs(self, grid, row, column, visited):
        visited[row][column] = True

        dr = [-1, 0, 0, 1]
        dc = [0, -1, 1, 0]

        for k in range(4): 
            nr = row + dr[k]
            nc = column + dc[k]
            if self.isInside(grid, nr, nc, visited):
                self.dfs(grid, nr, nc, visited)

    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        visited = [[False for i in range(m)] for i in range(n)]

        islands = 0 

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and not visited[i][j]:
                    self.dfs(grid, i, j, visited)
                    islands += 1 

        return islands