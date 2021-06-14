from collections import defaultdict
import heapq
from sys import stdin

input = stdin.readline

g = defaultdict(list)
n, m = map(int, input().strip().split())
for i in range(m):
	x, y, w = map(int, input().strip().split())
	g[x].append((w, y))  # weight : dest for heapq shit
d = [float("inf")]*(n+1)
d[1]=0
q = [(0, 1)]
p = [0] * (n + 1)
heapq.heapify(q)
while q:
	u = heapq.heappop(q)


	for child in g[u[1]]:
		to = child[1]
		wt = child[0]
		if d[u[1]] + wt < d[to]:
			d[to] = d[u[1]] + wt
			p[to] = u[1]
			heapq.heappush(q, (d[to], to))

print(d)
