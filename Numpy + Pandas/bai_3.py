import numpy as np
arr = np.random.uniform(0, 10, (3, 20))
print(arr)

print(f"Vi tri max: {np.argmax(arr)}")
print(f"Vi tri min: {np.argmin(arr)}")

arr = arr.ravel()
print(np.delete(arr, 0))

arr = np.sort(arr, kind='quicksort')[::-1]
print(arr)

k = float(input(f"Nhap vao so k: "))
l, r = 0, len(arr) - 1
while l <= r:
    m = l + r >> 1
    if arr[m] < k:
        r = m - 1
    else:
        l = m + 1
print(f"Vi tri them k: {l}")