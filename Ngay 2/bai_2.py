exec('n, m = int(input()), int(input())\nfor i in range(n): s = input(); print(s[:-m] + s[:m - 1:-1])')