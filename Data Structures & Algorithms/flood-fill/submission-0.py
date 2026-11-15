class Solution:
    def isInside(self, image, row, column): 
        n = len(image)
        m = len(image[0])

        return(0 <= row < n and 0 <= column < m)

    def dfs(self, image, row, column, original, color): 
        image[row][column] = color
        
        dr = [1, 0, 0, -1]
        dc = [0, 1, -1, 0]

        for k in range(4):
            nr = row + dr[k]
            nc = column + dc[k]   

            if self.isInside(image, nr, nc) and image[nr][nc] == original:
                self.dfs(image, nr, nc, original, color)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        original = image[sr][sc]
        self.dfs(image, sr, sc, original, color)

        return image

        