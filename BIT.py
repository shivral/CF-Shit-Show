from sys import stdin
input=stdin.readline
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


def isvowel(c):
	if c in "aeiou":
		return 1
	return 0


n = int(input())
bit = BIT(n)
s = list(input().strip())
for i in range(len(s)):
	bit.update(i, isvowel(s[i]))
for q in range(int(input())):
	typ, l, r = map(str, input().strip().split())
	if typ == "1":
		l = int(l) - 1
		r = int(r) - 1

		if l:
			left=bit.sum(l-1)
		else:
			left=0
		print(bit.sum(r)-left)
	if typ=="2":
		l=int(l)-1
		a=isvowel(s[l])
		b=isvowel(r)
		if a and b:
			continue
		elif  a==0 and b==0:
			continue
		else:
			if a:
				s[l]='b'
			else:
				s[l]='a'
			bit.update(l,b-a)
