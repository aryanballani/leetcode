class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh_oranges = 0
        minutes = 0
        neighbours = [(1, 0), (-1, 0), 
                            (0, 1), (0, -1)]

        for i in range(len(grid)):
            for j in range(len(grid[0])): 
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        
        if fresh_oranges == 0:
            return 0
        
        while queue and fresh_oranges > 0:
            minutes += 1

            for _ in range(len(queue)):
                r, c = queue.popleft()
                for x, y in neighbours:
                    row = r+x
                    col = c+y

                    if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1:
                        grid[row][col] = 2
                        queue.append((row, col))
                        fresh_oranges -= 1
                
        if fresh_oranges:
            return -1
        else:
            return minutes
        
        
