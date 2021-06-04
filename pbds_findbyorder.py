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
			ans += self.tree[i]
			i -= (i & (-i))
		return ans

	def update(self, i, value):
		i += 1
		while i <= self.n:
			self.tree[i] += value
			i += (i & (-i))


n, m = map(int, input().strip().split())
lst=list(map(int,input().strip().split()))
bit=BIT(n)
lst=sorted(lst)
for i in range(0,len(lst)):
	bit.update(i,1)         #u fill em all with ones and this shit works
print(bit.tree)
for i in range(0,len(lst)):
	print("query is ",bit.sum(i))
for q in range(m):
	k=int(input())
	l=0
	r=n-1
	val=n-1
	while l<=r: #this is bascially bin search for index mfkr
		mid=(l+r)//2 
		x=bit.sum(mid)
		if x>=k:
			print("x is ", x, k, mid)

			val=min(val,mid)
			r=mid-1
		else:
			l=mid+1
	print(lst[val],val)
	bit.update(val,-1)
	for i in range(0, len(lst)):
		print("query is ", bit.sum(i))
