#  if you win, you live. you cannot win unless you fight.
import sys
from sys import stdin, setrecursionlimit
# fd=open("cses.txt")
# sys.stdin=fd
input = stdin.readline
import heapq
rd = lambda: map(lambda s: int(s), input().strip().split())
rdone = lambda: map(lambda s: int(s) - 1, input().strip().split())
ri = lambda: int(input())
rs = lambda: input().strip()
from collections import defaultdict as unsafedict, deque, Counter as unsafecounter
from bisect import bisect_left as bl, bisect_right as br
from random import randint
from math import gcd, floor, log2, factorial, radians, sin, cos, ceil,sqrt
from  sys import  setrecursionlimit

def manacher(s):
    n=len(s)
    s="$"+s+"^"
    p=[0]*(n+2)
    l,r=1,1
    for i in range(1,n+1):
        p[i]=max(0,min(r-i,p[l+(r-i)]))
        while s[i-p[i]]==s[i+p[i]]:
            p[i]+=1
        if(i+p[i]>r):
            l=i-p[i]
            r=i+p[i]
    return p[1:-2]

s=input()
x=manacher(s)
for i in x:
    print((2*i)-1,end=" ")
