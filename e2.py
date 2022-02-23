# n = input().split()
n , x = map(int, input().split())
# # arr = [int (i) for i in range(n)]
# for i in range(n):
#     arr[i] = x + 2*i
#     arr[i] &=arr[i]
# print(arr[i])
arr = []
a = 0

for i in range(n):
    arr.append(x + 2*i)
    a ^= arr[i]
print(a)