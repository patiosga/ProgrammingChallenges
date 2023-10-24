import numpy as np

# UnionFind-like implementation but with two opposite numbers for the same node if the variables are opposites


def unite_equals(var11, var22):
    cluster11 = graph[var11]
    cluster22 = graph[var22]
    graph[graph == cluster22] = cluster11  # Union equals of val1 with equals of val2
    graph[graph == (-1) * cluster22] = (-1) * cluster11  # Union opposites of val1 with opposites of val2


def unite_opposites(var11, var22):
    cluster11 = graph[var11]
    cluster22 = graph[var22]
    graph[graph == cluster22] = (-1) * cluster11  # Union equals of val1 with opposites of val2
    graph[graph == (-1) * cluster22] = cluster11  # Union opposites of val1 with equals of val2


n = int(input("Number of variables: "))
m = int(input("Number of equations: "))

graph = np.zeros(n + 1)  # index 0 is unused for simplicity
clusters = 0
for i in range(m):
    print(graph)
    equation = input()
    var1, var2 = [int(num) for num in equation.split()]

    cluster1 = graph[abs(var1)]
    cluster2 = graph[abs(var2)]
    if var1 == var2:
        print("E")
    elif var1 * var2 < 0:
        var1 = abs(var1)
        var2 = abs(var2)
        if cluster1 != 0 and cluster2 != 0:
            # Variables have been encountered
            if cluster1 == cluster2:  # Variables are in the same cluster and therefore are equal
                print("C")  # contradicting
                break
            elif abs(cluster1) == abs(cluster2):  # Variables are in opposing clusters and therefore are opposites
                print("E")  # existing information
            else:
                unite_opposites(var1, var2)
                print("N")
        else:  # new variables
            if cluster1 != 0:  # var1 already exists
                graph[var2] = (-1) * graph[var1]  # var1 and var2 are opposites
            elif cluster2 != 0:  # var2 already exists
                graph[var1] = (-1) * graph[var2]
            else:  # new cluster
                clusters += 1
                graph[var1] = clusters
                graph[var2] = (-1) * clusters  # var2 gets the same cluster code but opposite
            print("N")
    else:
        var1 = abs(var1)
        var2 = abs(var2)
        if cluster1 != 0 and cluster2 != 0:
            # Variables have been encountered
            if cluster1 == cluster2:  # Variables are in the same cluster and therefore are equal
                print("E")  # contradicting
            elif abs(cluster1) == abs(cluster2):  # Variables are in opposing clusters and therefore are opposites
                print("C")  # existing information
                break
            else:
                unite_equals(var1, var2)
                print("N")
        else:  # new variables
            if cluster1 != 0:  # var1 already exists
                graph[var2] = graph[var1]  # var1 and var2 are opposites
            elif cluster2 != 0:  # var2 already exists
                graph[var1] = graph[var2]
            else:  # new cluster
                clusters += 1
                graph[var1] = clusters
                graph[var2] = clusters  # var2 gets the same cluster code
            print("N")
