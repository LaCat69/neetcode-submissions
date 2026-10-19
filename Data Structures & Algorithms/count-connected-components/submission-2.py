class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i :[] for i in range(n)}
        for k, v in edges:
            graph[k].append(v)
            graph[v].append(k)

        def dfs(node):
            if node in seen:
                return False

            seen.add(node)
            for nei in graph[node]:
                dfs(nei)

            return True
                
        seen = set()
        res = 0
        for k in graph.keys():
            if dfs(k):
                res += 1

        return res