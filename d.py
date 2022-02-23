n = int(input())

A = [ ["#"] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if n%2==0 and i < j:
            A[i][j] = "."
        elif n%2==0 and i >= j:
            A[i][j] = "#"
        if n%2 != 0 and i+j == n:
            A[i][j] = "#"
        elif n%2 != 0  and i+j < n-1:
            A[i][j] = "."
        
# for i in range(n):
#     for j in range(n):
        
for row in A:
    print(''.join(list(map(str,row))))