#Chapter 22.2
# DEPTH-FIRST TRAVERSAL

MAX = 10

# function to build adjacency matrix
def buildadjm(adj, n):
    for i in range(n):
        for j in range(n):
            print("Enter 1 if there is an edge from " + str(i) + " to " + str(j)),
            print(" otherwise enter 0 "),
            adj[i][j] = int(raw_input())
    return adj

# a function to visit the nodes in a depth-first order

def dfs(x, visited, adj, n):
    visited[x] = 1
    print("The nodes visited id " + str(x))
    for j in range(n):
        if((adj[x][j] == 1) and (visited[j] == 0)):
            dfs(j,visited,adj,n)

def main():
    adj = [[0 for i in range(MAX)] for j in range(MAX)]
    visited = [0 for i in range(MAX)]
    print("Enter the number of nodes in graph maximum = " +str(MAX))
    n = int(raw_input())
    adj = buildadjm(adj, n)
    for i in range(n):
        visited[i] = 0
    for i in range(n):
        if(visited[i] == 0):
            dfs(i, visited, adj, n)


main()