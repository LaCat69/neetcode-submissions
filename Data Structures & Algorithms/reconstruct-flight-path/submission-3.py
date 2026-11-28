class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for from_city, to_city in tickets:
            graph[from_city].append(to_city)
            graph[from_city].sort()

        res = []
        def dfs(node):
            while graph[node]:
                nei = graph[node].pop(0)
                dfs(nei)

            res.append(node)

        dfs("JFK")
        return res[::-1]