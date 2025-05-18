import heapq
from collections import defaultdict

def dijkstra(start, n, graph):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        cost, node = heapq.heappop(heap)
        if cost > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))
    return dist

def solution(n, s, a, b, fares):
    graph = defaultdict(list)
    for u, v, cost in fares:
        graph[u].append((v, cost))
        graph[v].append((u, cost))

    dist_s = dijkstra(s, n, graph)
    dist_a = dijkstra(a, n, graph)
    dist_b = dijkstra(b, n, graph)

    min_cost = float('inf')
    for k in range(1, n + 1):
        total = dist_s[k] + dist_a[k] + dist_b[k]
        min_cost = min(min_cost, total)

    return min_cost