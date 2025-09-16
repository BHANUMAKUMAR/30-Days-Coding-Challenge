def countComponents(n: int, edges: list[list[int]]) -> int:
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

    components = n
    for u, v in edges:
        if union(u, v):
            components -= 1

    return components
