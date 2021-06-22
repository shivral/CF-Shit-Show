from sys import  stdin
input=stdin.readline
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.count=0
class Trie():
    def __init__(self):
        self.root=Node(0)

    def insert(self,preXor):
        self.temp=self.root
        for i in range(31,-1,-1):
            val=preXor&(1<<i)
            if val:
                if not self.temp.right:
                    self.temp.right=Node(0)
                self.temp=self.temp.right
                self.temp.count+=1
            else:
                if not  self.temp.left:
                    self.temp.left=Node(0)
                self.temp=self.temp.left
                self.temp.count+=1
        self.temp.data=preXor

    def query(self,val):
        self.temp=self.root
        for i in range(31,-1,-1):
            active=val&(1<<i)
            if active:
                if self.temp.right and self.temp.right.count>0:
                    self.temp=self.temp.right
                elif self.temp.left:
                    self.temp=self.temp.left
            else:
                if self.temp.left and self.temp.left.count>0:
                    self.temp=self.temp.left
                elif self.temp.right:
                    self.temp=self.temp.right
            self.temp.count-=1
        return val^(self.temp.data)


n=input()
l1=list(map(int,input().strip().split()))
l2=list(map(int,input().strip().split()))
trie=Trie()
for i in l2:
    trie.insert(i)
for i in l1:
    print(trie.query(i),end=" ")
