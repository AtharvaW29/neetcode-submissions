class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = { c:set() for w in words for c in w }
        visited = {}
        result = []
        for j in range(len(words)- 1):
            w1, w2 = words[j], words[j+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[: minLen] == w2[: minLen]: return ""
            
            for i in range(minLen):
                if w1[i] != w2[i]:
                    adj[w1[i]].add(w2[i])
                    break
        
        def dfs(c):
            if c in visited:
                return visited[c]
            
            visited[c] = True
            for neig in adj[c]:
                if dfs(neig):
                    return True
            visited[c] = False
            result.append(c)

        for c in adj:
            if dfs(c):
                return ""
        
        result.reverse()
        return "".join(result)