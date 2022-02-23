n = int(input())
kosu = 0
a = [ [0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j]=i**2
        elif j == 0:
             a[i][j] = i
        elif i == 0:
            a[i][j] = j
for row in a:
    print( ' '.join (list(map(str,row))) )