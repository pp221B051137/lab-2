import re
n = int(input())
m = []
mm = []
for i in range(n):
    soz = input()
    if soz not in m:
        m.append(soz)
for j in range(len(m)):
    x = re.search("[a-z]", m[j])
    y = re.search("[A-Z]", m[j])
    z = re.search("[0-9]", m[j])
    if x and y and z:
        mm.append(m[j])
print(len(mm))
mm.sort()
for i in range(len(mm)):
    print(mm[i])
