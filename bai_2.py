s, ans1, ans2 = {i for i in input().upper()}, {'H', 'I', 'T'}, {'1', '4'}
print(((len(ans1 & s) == 3) and "True" or "False") + "\n" + ((len(ans2 & s) == 2) and "True" or "False"))