s1, s2 = {int(i) for i in input("Nhap vao ma sinh vien da duoc dang ki o ban thu 1: ").split()}, {int(i) for i in input("Nhap vao ma sinh vien da duoc dang ki o ban thu 2: ").split()}
print("Khong co sinh vien nao dang ki hoc tai ca 2 ban!\nSinh vien dang ki hoc o ca 2 ban la: {}.\nSinh vien dang ki o duy nhat 1 ban co msv la: {}.".format(str(s1 | s2)[1: -1], str((s1 | s2) - (s1 & s2))[1: -1])) if len(s1 & s2) == 0 else print("Sinh vien dang ki hoc tai ca 2 ban la: {}.\nSinh vien dang ki hoc o ca 2 ban la: {}.\nSinh vien dang ki o duy nhat 1 ban co msv la: {}.".format(str(s1 & s2)[1: -1], str(s1 | s2)[1: -1], str((s1 | s2) - (s1 & s2))[1: -1]))