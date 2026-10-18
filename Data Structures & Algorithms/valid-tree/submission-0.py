class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph = defaultdict(list)
        for k, v in edges:
            graph[k].append(v)
            graph[v].append(k)

        def dfs(node):
            if node in seen:
                return
            
            seen.add(node)

            for neighbor in graph[node]:
                dfs(neighbor)

        seen = set()
        dfs(0)

        return len(seen) == n