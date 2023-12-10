class Matrix:
    def __init__(self, n, m, value):
        self.n = n
        self.m = m
        self.value = value

    def __add__(self, other):
        if self.n != other.n or self.m != other.m:
            raise ValueError("Khong khop kich thuoc")
        result = []
        for i in range(self.n):
            row = []
            for j in range(self.m):
                row.append(self.value[i][j] + other.value[i][j])
            result.append(row)
        return Matrix(self.n, self.m, result)

    def __sub__(self, other):
        if self.n != other.n or self.m != other.m:
            raise ValueError("Khong khop kich thuoc")
        result = []
        for i in range(self.n):
            row = []
            for j in range(self.m):
                row.append(self.value[i][j] - other.value[i][j])
            result.append(row)
        return Matrix(self.n, self.m, result)

    def __mul__(self, other):
        if self.m != other.n:
            raise ValueError("Ma tran khong kich thuoc")
        result = []
        for i in range(self.n):
            row = []
            for j in range(other.m):
                element = 0
                for k in range(self.m):
                    element += self.value[i][k] * other.value[k][j]
                row.append(element)
            result.append(row)
        return Matrix(self.n, other.m, result)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            result = []
            for i in range(self.n):
                row = []
                for j in range(self.m):
                    row.append(self.value[i][j] / other)
                result.append(row)
            return Matrix(self.n, self.m, result)
        else:
            raise TypeError("Toan hang khong duoc ho tro de chia")

    def __eq__(self, other):
        if self.n != other.n or self.m != other.m:
            return False
        for i in range(self.n):
            for j in range(self.m):
                if self.value[i][j] != other.value[i][j]:
                    return False
        return True

    def __str__(self):
        result = ""
        for i in range(self.n):
            for j in range(self.m):
                result += str(self.value[i][j]) + "\t"
            result += "\n"
        return result

A = Matrix(2, 2, [[1, 2], [3, 4]])
B = Matrix(2, 2, [[5, 6], [7, 8]])

C = A + B
print("A + B:")
print(C)

D = A - B
print("A - B:")
print(D)

E = A * B
print("A * B:")
print(E)

F = A / B
print("A / B:")
print(F)

print("A == B:", A == B)