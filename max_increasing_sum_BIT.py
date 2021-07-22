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
    ind={}
    newind=0
    for i in sorted(list(set(a))):
        ind[i]=newind
        newind+=1
    maxs=0
    ft=BIT(newind+1)
    print(ind)
    for i in a:
        maxs=ft.sum(ind[i]-1)
        print(maxs,i)
        ft.update(ind[i],i+maxs)
        print(ft.tree)

    print(ft.sum(newind))

print(f([4, 2, 3, 1, 5, 8 ]))
