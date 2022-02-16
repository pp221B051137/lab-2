n = int(input())
a =  [ int (i) for i in input().split() ]
b = sorted(a)
print(b[n-1] * b[n-2])
# er = 0
# mx = a[0]
# for i in a:
#     if i > mx:
#         mx = i
# mx = er
# for i in a:
#     a.pop(mx)    
# mx2 = a[0]  
# for i in a:
#     if i > mx2:
#         mx2 = 1
# print(er * mx2)
# print(er, " " ,mx2)
