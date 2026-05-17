class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adj = defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        state = set()
        def dfs(curr, prev):
            if curr in state:
                return True
            state.add(curr)
            for c in adj[curr]:
                if c == prev:
                    continue
                if dfs(c, curr):
                    return True
            return False
        dfs(0, -1)
        return len(state) == n