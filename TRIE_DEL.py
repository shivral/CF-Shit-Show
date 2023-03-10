#  if you win, you live. you cannot win unless you fight.
import sys
from sys import stdin, setrecursionlimit
# fd=open("cses.txt")
# sys.stdin=fd

input = stdin.readline
rd = lambda: map(lambda s: int(s), input().strip().split())
rdone = lambda: map(lambda s: int(s) - 1, input().strip().split())
ri = lambda: int(input())
rs = lambda: input().strip()
from collections import defaultdict as unsafedict, deque, Counter as unsafecounter
from bisect import bisect_left as bl, bisect_right as br
from random import randint
from math import gcd, floor, log2, factorial, radians, sin, cos, ceil, sqrt


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.count = 0


class Trie():
    def __init__(self):
        self.root = Node(0)

    def insert(self, preXor):
        self.temp = self.root
        for i in range(31, -1, -1):
            val = preXor & (1 << i)
            if val:
                if not self.temp.right:
                    self.temp.right = Node(0)
                self.temp = self.temp.right
                self.temp.count += 1
            else:
                if not self.temp.left:
                    self.temp.left = Node(0)
                self.temp = self.temp.left
                self.temp.count += 1
        self.temp.data = preXor

    def delete(self, val):
        self.temp = self.root
        for i in range(31, -1, -1):
            active = val & (1 << i)
            if active:
                self.temp = self.temp.right
                self.temp.count -= 1
            else:
                self.temp = self.temp.left
                self.temp.count -= 1

    def query(self, val):
        self.temp = self.root
        for i in range(31, -1, -1):
            active = val[i]%2
            if active == 1:
                if self.temp.left and self.temp.left.count > 0:
                    self.temp = self.temp.left
                elif self.temp.right and self.temp.right.count>0:
                    self.temp=self.temp.right
            else:
                # print(self.temp.data)
                if self.temp.right and self.temp.right.count > 0:
                    self.temp = self.temp.right
                elif self.temp.left and self.temp.left.count > 0:
                    self.temp = self.temp.left
        return self.temp.data

n=ri()
vl=list(rd())
g=unsafedict(list)
for i in range(n-1):
    x,y=rdone()
    g[x].append(y)
    g[y].append(x)
q=deque([(0,0)])
d=unsafedict(list)
xr=unsafedict(int)
dep=[-1]*n
dep[0]=0

while q:
    di,t=q.popleft()
    d[di].append(vl[t])
    xr[di]^=vl[t]
    for i in g[t]:
        if dep[i]==-1:
            dep[i]=di+1
            q.append((dep[i],i))
tr=Trie()
for i in vl:
    tr.insert(i)
ans=unsafedict(int)
for i  in d:
    txr=xr[i]
    ans[i]=txr
    hmp=[0]*32
    for v in d[i]:
        for bt in range(31):
            if (v>>bt)&1:
                hmp[bt]+=1
        tr.delete(v)

    for v in d[i]:
        tans=txr^v
        hm2=hmp.copy()
        for bt in range(31):
            if (v>>bt)&1:
                hm2[bt]-=1
        qr=tr.query(hm2)
        ans[i]=max(ans[i],qr^tans)
    for v in d[i]:
        tr.insert(v)
res=[]
for i in sorted(ans.keys()):
    res.append(ans[i])
print(res)
