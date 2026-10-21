class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = {i: i for i in range(1, n+1)}
        size = {i: 1 for i in range(1, n+1)}

        def find(leader):
            if leader == par[leader]:
                return leader

            par[leader] = find(par[leader])

            return par[leader]

        def union(n1, n2):
            if size[n1] > size[n2]:
                par[n2] = n1
                size[n1] += size[n2]
            else:
                par[n1] = n2
                size[n2] += size[n1]


        for v1, v2 in edges:
            leader1, leader2 = find(v1), find(v2)
            if leader1 == leader2:
                return [v1, v2]
            union(leader1, leader2)

        return []