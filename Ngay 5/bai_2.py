n, se, k = input(), [int(i) for i in input().split(", ")], int(input())
print({i for i in se if sum(se[: se.index(i) + 1]) <= k})