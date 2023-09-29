from math import inf
import heapq
vertices, edges = map(int, input().split())
edge_data = [tuple(map(int, input().split())) for i in range(edges)]

class dijkstrasGraph(): # data needs to be formated for this to work properly
    def __init__(self, vertices):
        self.v = [set() for i in range(vertices)]
    
    def add_edge(self, a, b, dis):
        self.v[a].add((b, dis))
        self.v[b].add((a, dis))
    
    def dijkstra(self, src):
        pq = []

        heapq.heappush(pq, (0, src))
        dist = [inf for i in range(len(self.v))]
        dist[src] = 0

        while pq:
            d, u = heapq.heappop(pq)

            for v, weight in self.v[u]:
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))
        return dist[-1]

graph = dijkstrasGraph(vertices)
for a, b, weight in edge_data:
    graph.add_edge(a - 1, b - 1, weight)
print(graph.dijkstra(0))