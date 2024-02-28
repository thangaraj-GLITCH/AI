graph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F','G'],
    'D' : [],
    'E' : [],
    'F' : [],
    'G' : [],
}

visited = []
queue = []

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)

    while queue:
         m = queue.pop(0)
         print(m, end = " ")

         for n in graph[m]:
             if n not in visited:
                 visited.append(n)
                 queue.append(n)
bfs(visited,graph,'B')
