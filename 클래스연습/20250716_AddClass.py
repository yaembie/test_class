class Operation:
    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2
    
op = Operation()

res = op.add(op.add(3, 5), 2)
print(res)