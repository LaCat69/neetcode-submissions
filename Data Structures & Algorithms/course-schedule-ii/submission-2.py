class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {n: [] for n in range(numCourses)}
        for k, v in prerequisites:
            graph[k].append(v)

        def dfs(k, active_path) -> bool:
            if k in path:
                return True
            if k in seen:
                return False

            active_path.add(k)
            for v in graph[k]:
                if dfs(v, active_path):
                    return True

            seen.add(k)
            res.append(k)
            active_path.remove(k)
            return False

        seen, res = set(), list()
        for k in graph.keys():
            path = set()
            if dfs(k, path):
                return []

        return res