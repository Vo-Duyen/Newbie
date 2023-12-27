import numpy as np
a, b = np.array([float(i) for i in input("Nhap vao vector thu nhat: ").split()]), np.array([float(i) for i in input("Nhap vao vector thu hai: ").split()])
print(f"Max cua a: {np.max(a)}")
print(f"Min cua a: {np.min(a)}")
print(f"Gia tri trung binh cua a: {np.mean(a)}")
print(f"Do lech chuan cua a: {np.std(a)}")
print(f"Gia tri trung vi cua a: {np.median(a)}")

print(f"Max cua b: {np.max(b)}")
print(f"Min cua b: {np.min(b)}")
print(f"Gia tri trung binh cua b: {np.mean(b)}")
print(f"Do lech chuan cua b: {np.std(b)}")
print(f"Gia tri trung vi cua b: {np.median(b)}")

c = np.array([a, b])
print(f"Ma tran c: {c}")

d = np.random.normal(np.mean(b), np.std(b), (len(b), len(b)))
print(f"Ma tran d: {d}")

print(f"Tong: {d + d.T}")
print(f"Hieu: {d - d.T}")
print(f"Tich: {d * d.T}")
print(f"Tich ver2: {np.linalg.pinv(d) * np.transpose(d)}")

e = np.expand_dims(c, axis=0)
print(f"Ma tran e: {e}")

