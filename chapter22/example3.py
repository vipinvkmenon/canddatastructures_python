#Chapter 22.3
# BREADTH-FIRST TRAVERSAL

MAX = 10

class node:
    def __init__(self):
        self.data = 0
        self.link = None

# function to build adjacency matrix
def buildadjm(adj, n):
    for i in range(n):
        for j in range(n):
            print("Enter 1 if there is an edge from " + str(i) + " to " + str(j)),
            print(" otherwise enter 0 "),
            adj[i][j] = int(raw_input())
    return adj

#  A function to insert a new node in queue
def addqueue(p, val):
    if(p == None):
        p = node()
        if(p == None):
            print("Cannot Allocate")
            exit()
        p.data = val
    else:
        temp = p
        while(temp.link != None):
            temp = temp.link
        temp.link = node()
        temp = temp.link
        if(temp == None):
            print("Cannot Allocate")
            exit()
        temp.data = val
    return(p)

def deleteq(p, val):
    if(p == None):
        print("Cannot Allocate")
        exit()
    val = p.data
    temp = p
    p = p.link
    return(p, val)

def bfs(adj, x, visited, n, p):
    y = 1
    p = addqueue(p, x)
    p , y= deleteq(p, y)
    if(visited[y] == 0):
        print("node visited = " + str(y))
        visited[y] = 1
        for j  in range(n):
            if((adj[y][j] == 1) and (visited[j] == 0)):
                p = addqueue(p, j)
        while(p != None):
            p , y= deleteq(p, y)
            if(visited[y] == 0):
                print("node visited = " + str(y))
                visited[y] = 1
                for j  in range(n):
                    if((adj[y][j] == 1) and (visited[j] == 0)):
                        p = addqueue(p, j)

def main():
    adj = [[0 for i in range(MAX)] for j in range(MAX)]
    visited = [0 for i in range(MAX)]
    start = None
    print("Enter the number of nodes in graph maximum = " +str(MAX))
    n = int(raw_input())
    adj = buildadjm(adj, n)
    for i in range(n):
        visited[i] = 0
    for i in range(n):
        if(visited[i] == 0):
            bfs(adj, i, visited, n, start)

main()