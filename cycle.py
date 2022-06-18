#https://atcoder.jp/contests/abc256/submissions/32565921
import string
from sys import stdin

input = stdin.readline
read = lambda: map(lambda s: int(s), input().strip().split())
readi = lambda: int(input())
from collections import defaultdict
from bisect import bisect_left as bl, bisect_right as br
from random import randint
from math import gcd, ceil, floor
import threading
from  sys import setrecursionlimit
setrecursionlimit(10**6)
RANDOM = randint(1, 10 ** 9)

cycleend=0
cyclestart=0
class Wrapper(int):
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM

def dfs(node,vis,par,g):
    global cycleend,cyclestart
    vis[node]=1
    for i,wt in g[node]:
        if vis[i]==0:
            par[i]=(node,wt)
            vis[i]=True
            # st.append(wt)
            if dfs(i,vis,par,g):
                return True
        elif vis[i]==1:
            par[i]=(node,wt)
            cycleend=node
            cyclestart=i
            return True
    vis[node]=2
    return False
def main():
    global cycleend,cyclestart
    n=readi()
    x=list(read())
    c=list(read())
    d=defaultdict(list)

    for i in range(n):
        d[i+1].append((x[i],c[i]))
    vis=[0]*(n+1)
    par=[(0,0)]*(n+1)
    ans=0
    for i in range(1,n+1):
        if vis[i]==0:
            cyclestart=-1
            cycleend=-1
            dfs(i,vis,par,d)
            if cyclestart!=-1:
                v=cycleend
                c=[]
                c.append(par[v][1])
                # print(v,par[v])
                while v!=cyclestart and v:
                   v=par[v][0]

                   c.append(par[v][1])
                   # print(i,v,par[v])

                ans+=min(c)
    print(ans)

threading.stack_size(10 ** 8)
t = threading.Thread(target=main)
t.start()
t.join()
