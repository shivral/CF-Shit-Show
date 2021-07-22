from sys import stdin

input = stdin.readline


class BIT():
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        ans = 0
        i += 1
        while i > 0:
            ans =max(ans, self.tree[i])
            i -= (i & (-i))
        return ans

    def update(self, i, value):
        i += 1
        while i <= self.n:
            self.tree[i] = max(value,self.tree[i])
            i += (i & (-i))
def f(a):
    newind=0
    maxs=0
    ans=0
    ft=BIT(2*(10**5)+5)
    for i in a:
        maxs=ft.sum(i-1)
        # print(maxs,i)
        ft.update(i,maxs+1)
        ans=max(ans,maxs+1)
        # print(ft.tree)

    return ans

a=input()
l=list(map(int,input().strip().split()))
print(f(l))
