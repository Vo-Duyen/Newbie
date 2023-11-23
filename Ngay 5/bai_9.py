import random
temp, n, ans = ["CNTT", "KHMT", "KTPM", "HTTT"], int(input()), dict()
for i in range(n):
    tam = {}
    tam["Username"] = i + 2021600001
    tam["Password" ] = random.choice(temp) + str(i + 2021600001)
    ans["Account {}".format(i + 1)] = tam
print(ans)