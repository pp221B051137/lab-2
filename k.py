import re
s = input()
ans = []
x = re.split("[;, !?=]", s)
for i in range(len(x)):
    if x[i] != "":
        ans.append(x[i])
m = list(set(ans))
print(len(m))
m.sort()
for j in range(len(m)):
    print(m[j])
