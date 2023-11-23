import re
temp, ans = [], []
for i in sorted(re.findall(r"\w+", input())):
    if not temp or i != temp[0]:
        temp = [i, 1]
        ans.append(temp)
    else:
        temp[1] += 1
print("".join({"[" : "(", "]" : ")"}.get(c, c) for c in str(ans)))