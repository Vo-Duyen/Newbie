import re
lis, ans = {int(i) for i in re.findall(r"-?\d+", input())} | {11}, ()
for i in lis:
    if 11 - i in lis and (11 - i, i) not in ans:
        ans += ((i, 11 - i),)
print("{}\n{}".format(lis, ans))