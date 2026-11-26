class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        dist = {(points[0][0], points[0][1]): 0}
        visited = set()
        heap = []
        heapq.heappush(heap, (0, points[0]))
        while len(visited) < len(points):
            weight, node = heapq.heappop(heap)
            x, y = node
            if (x, y) in visited:
                continue
            visited.add((x, y))
            res += weight
            if weight > dist[(x, y)]:
                continue
            for i in range(len(points)):
                x2, y2 = points[i]
                if (x2, y2) in visited:
                    continue
                manhetten = abs(x - x2) + abs(y - y2)
                if dist.get((x2, y2), float("inf")) > manhetten:
                    dist[(x2, y2)] = manhetten
                heapq.heappush(heap, (manhetten, (x2, y2)))
                

        return res