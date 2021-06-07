from  collections import defaultdict
from sys import setrecursionlimit
setrecursionlimit(10**5)
import threading

from sys import stdin
input=stdin.readline

def dfs(node,vis,g,ans):
	vis[node]=1
	for i in g[node]:
		if vis[i]==0:
			dfs(i,vis,g,ans)
	ans.append(node)
	return
def dfs2(node,vis,g,component):
	vis[node] = 1
	component.append(node)
	for i in g[node]:
		if vis[i] == 0:
			dfs2(i, vis, g,component)

def main():
	n,m=map(int,input().strip().split())
	g=defaultdict(list)
	graph_reversed=defaultdict(list)
	lst=list(map(int,input().strip().split()))

	for i in range(m):
		x,y=map(int,input().strip().split())
		g[x].append(y)
		graph_reversed[y].append(x)
	vis=[0]*(n+1)

	order=[]
	cost=0
	for ind in range(1,n+1):
		if vis[ind]==0:
			dfs(ind,vis,g,order)
	order=order[::-1]
	vis=[0]*(n+1)
	for ind in order:
		if vis[ind]==0:
			component=[]
			dfs2(ind,vis,graph_reversed,component)
			cost+=lst[min(component,key=lambda s:lst[s-1])-1]
	print(cost)

threading.stack_size(10 ** 8)
t = threading.Thread(target=main)
t.start()
t.join()
