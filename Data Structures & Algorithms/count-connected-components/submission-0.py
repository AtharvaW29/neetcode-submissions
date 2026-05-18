class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if len(edges) == 0:
            return n
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = [False] * n
        count = 0
        stack = []
        for i in range(n):
            if not visited[i]:
                count += 1
                visited[i] = True
                stack = [i]
                while stack:
                    a = stack.pop()
                    for c in adj[a]:
                        if not visited[c]:
                            visited[c] = True
                            stack.append(c)
        return count