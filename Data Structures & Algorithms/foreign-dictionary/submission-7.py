class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        visited = {}
        result = []
        adj = {c: set() for w in words for c in w}
        n = len(words)
        l, r = 0, 1
        while r < n:
            w1 = words[l]
            w2 = words[r]
            minlen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[: minlen] == w2[: minlen]:
                return "" 
            
            for i in range(minlen):
                if w1[i] != w2[i]:
                    adj[str(w1[i])].add(str(w2[i]))
                    break
            l += 1
            r += 1
            
        def dfs(n):
            if n in visited:
                return visited[n]
            visited[n] = True
            for c in adj[n]:
                if dfs(c):
                    return True
            visited[n] = False
            result.append(n)
            
        for n in adj:
            if dfs(n):
                return ""
        result.reverse()
        return "".join(result)