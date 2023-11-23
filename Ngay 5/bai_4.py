import re
n, s = input(), input()
print("{}\n{}".format(set(re.findall(r"\w+", s)), len(re.findall(r"\b\d+\b", s))))