def isCyclic(V, adj):
    white = set()
    gray = set()
    black = set()

    def dfs(curr):

        # once we enter DFS we remove from the white set and add to gray set

        white.remove(curr)
        gray.add(curr)

        for neighbour in adj[curr]:

            if neighbour in black:
                continue

            if neighbour in gray:
                return True

            if dfs(neighbour):
                return True

        black.add(curr)
        gray.remove(curr)
        return False

    for x in range(V):
        white.add(x)

    for current in range(len(white)):
        if current in white and dfs(current):
            return True

    return False


'''
3 3
0 1
1 2 
'''
#
print(isCyclic(4, [[1], [3, 0], [0], [1]]))

print(isCyclic(4, [[3], [], [1], [2]]))

print(isCyclic(2, [[1,0], [0,1]]))