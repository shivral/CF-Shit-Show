def Z(s,B):
	n=len(s)
	x=0;y=0
	z=[0]*(n)
	for i in range(1,n):
		z[i]=max(0,min(z[i-x],y-i+1))
		while i+z[i]<n and s[z[i]]==s[i+z[i]]:
			x=i
			y=i+z[i]
			z[i]+=1
	return z.count(B)

a=input()
b=input()
B=len(b)
s=b+"#"+a
print(Z(s,B))
