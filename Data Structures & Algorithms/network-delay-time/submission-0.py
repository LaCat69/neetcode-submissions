class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))

        heap = []
        heapq.heappush(heap, (0, k))

        dist = {k: 0}

        while heap:
            curr_cost, node = heapq.heappop(heap)
            if curr_cost > dist[node]:
                continue
            for nei, cost in graph.get(node, []):
                if cost + curr_cost < dist.get(nei, float("inf")):
                    dist[nei] = cost + curr_cost
                    heapq.heappush(heap, (dist[nei], nei))

        if len(dist) != n:
            return -1

        return max(dist.values())