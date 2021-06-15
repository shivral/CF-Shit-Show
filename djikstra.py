import heapq
from collections import defaultdict
g = defaultdict(list)
n, m = map(int, input().strip().split())
for i in range(m):
	x, y, w = map(int, input().strip().split())
	g[x].append((w, y))  # weight : dest for heapq shit
d = [float("inf")]*(n+1)
d[1]=0
q = [(0, 1)]
heapq.heapify(q)
while q:
	u = heapq.heappop(q)
	if d[u[1]]!=u[0]:
		continue

	for child in g[u[1]]:
		to = child[1]
		wt = child[0]
		if d[u[1]] + wt < d[to]:
			d[to] = d[u[1]] + wt
			heapq.heappush(q, (d[to], to))

print(*d[1:])
