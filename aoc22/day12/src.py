import sys
f = open(sys.argv[1],'r')

letters = [[ord(c) for c in s.rstrip()] for s in f]
letters[0][0] = ord('a')


N,M = len(letters), len(letters[0])
V = N*M
starts = [0]

for i in range(len(letters)):
    for j in range(len(letters[0])):
            if letters[i][j] == ord('E'):
                letters[i][j] = ord('z')
                endCoord = (i*M +j)
            elif letters[i][j] == ord('a'):
                starts.append(i*M+j)


E = [[0 for _ in range(V)] for _ in range(V)]

for i in range(N):
    for j in range(M):
        val = letters[i][j]
        if i<N-1:
            if letters[i+1][j] < val + 2:
                E[M*i+j][M*(i+1)+j] = 1
        if i>0 and letters[i-1][j] < val + 2:
            E[M*i+j][M*(i-1)+j] = 1
        if j<M-1 and letters[i][j+1] < val + 2:
            E[M*i+j][M*i+j+1] = 1
        if j>0 and letters[i][j-1] < val + 2:
            E[M*i+j][M*i+j-1] = 1

def dijkstra(graph, start):
    # Number of vertices in the graph
    num_vertices = len(graph)
    
    # Shortest distance from the start to each node
    distances = [sys.maxsize] * num_vertices
    for  s in start:
        distances[s] = 0
    
    # Boolean array to track vertices for which the shortest distance is already found
    visited = [False] * num_vertices
    
    for _ in range(num_vertices):
        # Select the vertex with the minimum distance from the unvisited set
        min_distance = sys.maxsize
        min_vertex = -1
        
        for v in range(num_vertices):
            if not visited[v] and distances[v] < min_distance:
                min_distance = distances[v]
                min_vertex = v
        
        # Mark the selected vertex as visited
        visited[min_vertex] = True
        
        # Update the distances of the adjacent vertices of the selected vertex
        for v in range(num_vertices):
            if graph[min_vertex][v] > 0 and not visited[v]:
                new_distance = distances[min_vertex] + graph[min_vertex][v]
                if new_distance < distances[v]:
                    distances[v] = new_distance

    return distances

sp = dijkstra(E,starts)
print(sp[endCoord])
