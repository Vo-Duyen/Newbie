import re
ans = dict()
for i in sorted(re.findall(r".", input())):
    if i not in ans:
        ans[i] = 1
    else:
        ans[i] += 1
print(ans)