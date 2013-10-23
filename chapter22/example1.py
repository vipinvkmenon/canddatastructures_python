#Chapter 22.1
# INDEGREE AND OUTDEGREE OF A NODE OF A GRAPH

MAX = 10

# function to build adjacency matrix
def buildadjm(adj, n):
    for i in range(n):
        for j in range(n):
            print("Enter 1 if there is an edge from " + str(i) + " to " + str(j)),
            print(" otherwise enter 0 "),
            adj[i][j] = int(raw_input())
    return adj


#function to compute outdegree
def outdegree(adj, x, n):
    count = 0
    for i in range(n):
        if(adj[x][i] == 1):
            count = count + 1
    return count


# function to computer in degree
def indegree(adj, x, n):
    count = 0
    for i in range(n):
        if(adj[i][x] == 1):
            count = count + 1
    return count

def main():
    adj = [[0 for i in range(MAX)] for j in range(MAX)]
    print("Enter the number of nodes in graph maximum = " +str(MAX))
    n = int(raw_input())
    adj = buildadjm(adj, n)
    for i in range(n):
        print("The indegree of the node " + str(i) + " is " + str(indegree(adj, i, n)))
        print("The outdegree of the node " + str(i) + " is " + str(outdegree(adj, i, n)))

main()




