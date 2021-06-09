from math import  floor,log2
# sparse table
from sys import stdin
input=stdin.readline
class SparseTable():
	def __init__(self, n, data):
		self.n = n
		self.k = floor(log2(n))
		self.table = [[0] * (self.k + 1) for i in range(n)]
		self.data = data
		self.log=[0]*(self.n+100)


	def RMQ_build(self):
		for i in range(0, self.n):
			self.table[i][0] = self.data[i]
		for j in range(1, self.k + 1):
			i = 0
			while i + (1 << j) <= self.n:
				self.table[i][j] = min(self.table[i][j - 1], self.table[i + (1 << (j - 1))][j - 1])
				i += 1
		for i in range(2,self.n+100):
			self.log[i]=self.log[i//2]+1

	def RMQ_Q(self, l, r):  # 0 indexing l r please [l,r]
		j = self.log[r-l+1]
		return min(self.table[l][j], self.table[r - (1 << j) + 1][j])


n, m = map(int, input().strip().split())
lst = list(map(int, input().strip().split()))
st=SparseTable(n,lst)
st.RMQ_build()
for i in range(m):
	l, r = map(int, input().strip().split())

	print(st.RMQ_Q(l - 1, r-1))

