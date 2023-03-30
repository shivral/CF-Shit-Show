class dsu(): #ta
	def __init__(self,n):
		self.parent=[0]*(n)
		self.sz=[0]*(n)

	def make_set(self,v):
		self.parent[v]=v
		self.sz[v]=1

	def find_set(self,v):
		if v==self.parent[v]:
			return v
		self.parent[v]=self.find_set(self.parent[v])
		return self.parent[v]

	def union(self,a,b):
		a=self.find_set(a)
		b=self.find_set(b)
		if a==b:
			return
		if self.sz[a]<self.sz[b]:
			a,b=b,a
		self.parent[b]=a
		self.sz[a]+=self.sz[b]

	def getsize(self,v):
		return self.sz[self.find_set(v)]
