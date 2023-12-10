class Pycon:
    id = 0
    def __init__(self, name = "", age = -1):
        Pycon.id += 1
        self.id = Pycon.id
        self.__name = name
        self.__age = age
    def nhap(self):
        self.__name = input("Enter name: ") 
        self.__age = int(input("Enter age: "))
    def __str__(self) -> str:
        return f"ID: {self.id}\tName: {self.__name}\tAge: {self.__age}"
    @classmethod
    def averAge(cls, adj):
        sumAge = sum(i.__age for i in adj)
        return sumAge / len(adj)
n = int(input("Enter n: "))
adj = []
for i in range(n):
    pycons = Pycon()
    pycons.nhap()
    adj.append(pycons)
print('\n'.join(str(i) for i in adj))