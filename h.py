import math
x,y = map(int,input().split())
n = int(input())
a =[]
for i in range(n):
    arr = []
    x1, y1 = input().split()
    arr.append(math.sqrt((int(x1)-x)**2 + (int(y1)-y)**2))
    arr.append(x1)
    arr.append(y1)
    a.append(arr)
l = sorted(a)
for i in range(len(l)):
    print(l[i][1] , l[i][2])