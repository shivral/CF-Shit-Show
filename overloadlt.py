class String():
	def __init__(self,s):
		self.res=s
	def __lt__(self, other):
		return self.res+other.res<other.res+self.res

q=[]
for i in range(int(input())):
	q.append(String(input()))
q=sorted(q)
ans=""
for i in q:
	ans+=i.res
print(ans)
