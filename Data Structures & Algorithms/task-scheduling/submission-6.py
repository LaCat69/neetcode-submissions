class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        heap = []

        for t in set(tasks):
            heapq.heappush_max(heap, (counter[t], t))

        time = 0
        cooldown = deque([])

        while cooldown or heap:
            time += 1
            while cooldown and cooldown[0][2] <= time:
                t, f, _ = cooldown.popleft()
                if f > 0:
                    heapq.heappush_max(heap, (f, t))
            if heap:
                f, t = heapq.heappop_max(heap)
                f -= 1
                if f > 0:
                    cooldown.append((t, f, time + n + 1))

        return time