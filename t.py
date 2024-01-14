c,v,w,x=list(map(int,input().split()))
m=[['NW','N','NE'],
['W', 0,'E'],
['SW','S','SE']]
j=[-1,0,1]
b=w
n=x
while True:
 o=p=0
 if n<v:
  p=2
 elif n==v:
  p=1
 if b<c:
  o=2
 elif b==c:
  o=1
 b+=j[o]
 n+=j[p]
 print(m[p][o])
