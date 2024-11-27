class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def _shortest_path():
            q = deque()
            q.append((0, 0))  # node, length
            visit = set()

            while q:
                cur, length = q.popleft()
                if cur == n - 1:
                    return length
                for nei in adj[cur]:
                    if nei not in visit:
                        q.append((nei, length + 1))
                        visit.add(nei)

        adj = [[i + 1] for i in range(n)]
        res = []

        for src, dst in queries:
            adj[src].append(dst)
            res.append(_shortest_path())

        return res
