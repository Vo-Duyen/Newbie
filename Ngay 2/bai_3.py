exec('k = int(input())\nfor i in range(k): s, d1, d2 = input(), int(input()), int(input()); print(str(i + 1) + " " + s + " " + str(d1 + d2) + " " + (d1 + d2 >= 190 and "Xuat sac" or d1 + d2 >= 150 and "Gioi" or d1 + d2 >= 100 and "Kha" or "Yeu"))')