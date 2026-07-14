def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return "cannot divide by zero"
    return a / b


print(add(2, 3))     # 5
print(sub(10, 4))    # 6
print(mul(6, 7))     # 42
print(div(20, 5))    # 4.0
print(div(5, 0))     # cannot divide by zero