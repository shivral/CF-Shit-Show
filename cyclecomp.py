    #i know brute
    #  if you win, you live. you cannot win unless you fight.
    from sys import stdin,setrecursionlimit
    input=stdin.readline
    import heapq
    rd=lambda: map(lambda s: int(s), input().strip().split())
    rdone=lambda: map(lambda s: int(s)-1, input().strip().split())
    ri=lambda: int(input())
    rs=lambda :input().strip()
    from collections import defaultdict as unsafedict,deque,Counter as unsafecounter
    from bisect import bisect_left as bl, bisect_right as br
    from random import randint
    from math import gcd, floor,log2,factorial,radians,sin,cos,ceil
    setrecursionlimit(10**6)
     
    import threading
     
    cycleend=0
    cyclestart=0
    st=set()
     
    def dfs(node,vis,par,g,pp):
        # print(par)
        global st
        vis[node]=2
        for i in g[node]:
            if i==pp:
                continue
            if vis[i]==2:
                par.append(i)
                st=set(par)
                par=[]
            elif vis[i]==0:
                par.append(i)
                dfs(i,vis,par,g,node)
                par.pop()
        vis[node]=1
    def main():
        global cycleend,cyclestart,st
        n=ri()
        d=unsafedict(list)
     
        for i in range(n):
            x,y=rdone()
            d[x].append(y)
            d[y].append(x)
        vis=[0]*(n+1)
        par=[0]*(n+1)
        ans=0
        for i in range(1,n+1):
            if vis[i]==0:
                par=[]
                dfs(i,vis,par,d,-1)
        # print(st)
        vis2=[-1]*n
        q=deque()
        for i in st:
            q.append((i,i))
            vis2[i]=i
        while q:
            t,par=q.popleft()
            for i in d[t]:
                if i not in st:
                    if vis2[i]==-1:
                        vis2[i]=par
                        q.append((i,par))
        # print(vis2)
        q=ri()
        for i in range(q):
            x,y=rdone()
            if vis2[x]==vis2[y]:
                print("Yes")
            else:
                print("No")
    threading.stack_size(10 ** 8)
    t = threading.Thread(target=main)
    t.start()
    t.join()
