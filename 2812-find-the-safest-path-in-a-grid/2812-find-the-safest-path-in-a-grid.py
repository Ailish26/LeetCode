class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        from collections import deque
import heapq
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[float('inf')] * n for _ in range(n)]
        q = deque()

        # Multi-source BFS
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == float('inf'):
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        # Max-heap search
        heap = [(-dist[0][0], 0, 0)]
        seen = [[False]*n for _ in range(n)]
        seen[0][0] = True

        while heap:
            safe, r, c = heapq.heappop(heap)
            safe = -safe
            if (r, c) == (n-1, n-1):
                return safe
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < n and 0 <= nc < n and not seen[nr][nc]:
                    seen[nr][nc] = True
                    heapq.heappush(heap, (-min(safe, dist[nr][nc]), nr, nc))
        return 0
