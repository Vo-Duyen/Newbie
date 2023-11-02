a = int(input())
print("So luong bits can thiet de bieu dien a duoi dang nhi phan (khong bao gom dau) la: " + str(len(bin(a >= 0 and a or - a)) - 2))