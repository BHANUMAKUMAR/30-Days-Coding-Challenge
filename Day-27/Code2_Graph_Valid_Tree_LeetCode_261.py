def validTree(n: int, edges: list[list[int]]) -> bool:
    if len(edges) != n - 1:
        return False
    
    parent = list(range(n))
    rank = [1] * n  
    
    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])  
        return parent[x]
    
    def union(x, y):
        rootX, rootY = find(x), find(y)
        if rootX == rootY:
            return False  
        if rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        elif rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        else:
            parent[rootY] = rootX
            rank[rootX] += 1
        return True
    
    for u, v in edges:
        if not union(u, v):
            return False
    
    return True
