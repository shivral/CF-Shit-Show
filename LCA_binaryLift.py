from collections import defaultdict
from sys import setrecursionlimit

setrecursionlimit(10 ** 5)
import threading

LOG = 14


def dfs(a, child, up, depth):
	global LOG
	for b in child[a]:
		depth[b] = depth[a] + 1
		up[b][0] = a  # parent
		for j in range(1, LOG):
			up[b][j] = up[up[b][j - 1]][j - 1]  # baap ka baap
		dfs(b, child, up, depth)


def get_lca(a, b, depth, up):
	global LOG
	if depth[a] < depth[b]:
		a, b = b, a  # we assume A is always the deeper one
	k = depth[a] - depth[b]
	for j in range(LOG - 1, -1, -1):  # start from the highest power
		if k & (1 << j):
			a = up[a][j]
	if a == b:
		return a

	for j in range(LOG - 1, -1, -1):  # start from the highest power
		if up[a][j] != up[b][j]:  # if father not same
			a = up[a][j]  # u go up
			b = up[b][j]

	return up[a][0]


def main():
	global LOG
	child = defaultdict(list)
	n = int(input())
	for i in range(n):
		ch = list(map(int, input().strip().split()))
		ch = ch[1:]
		child[i] += ch
	up = [[0] * LOG for i in range(10 ** 5)]
	depth = [0] * (10 ** 5)
	dfs(0, child, up, depth)
	q = []
	for j in range(int(input())):
		a, b = map(int, input().strip().split())
		print(get_lca(a, b, depth, up))


threading.stack_size(10 ** 8)
t = threading.Thread(target=main)
t.start()
t.join()
