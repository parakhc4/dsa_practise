class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        time = 0
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        nxt = []
        queue = collections.deque()
        count = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    queue.append([i,j])
                elif grid[i][j] == 1:
                    count += 1
        if count == 0:
            return 0
        while len(queue) > 0:
            curr_x, curr_y = queue.popleft()
            for x, y in dirs:
                next_x, next_y = curr_x + x, curr_y + y
                if (0 <= next_x < M) and (0 <= next_y < N) and grid[next_x][next_y] == 1:
                    count -= 1
                    grid[next_x][next_y] = 2
                    nxt.append([next_x, next_y])

            if len(queue) == 0:
                if count == 0:        
                    time += 1
                    break
                queue.extend(nxt)
                nxt = []
                time += 1

        return time if count == 0 else -1