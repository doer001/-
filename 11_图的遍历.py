import collections
class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

# *** 深度优先 *********************************************************
def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

# *** 广度优先 *********************************************************
def bfs(graph, startnode):
        seen, queue = set([startnode]), collections.deque([startnode])
        while queue:
            vertex = queue.popleft()
            marked(vertex)
            for node in graph[vertex]:
                if node not in seen:
                    seen.add(node)
                    queue.append(node)
def marked(n):
    print(n)

gdict = { "a" : set(["b","c"]),
          "b" : set(["a", "d"]),
          "c" : set(["a", "d"]),
          "d" : set(["e"]),
          "e" : set(["a"])
                }


dfs(gdict, 'a')
bfs(gdict, "a")
