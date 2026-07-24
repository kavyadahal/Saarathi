"""Bulletproof calculator (buffer / stretch)
Type hints + a custom exception + try/except."""

class DivbyzeroError(Exception):
    pass

def add(a:float,b:float)->float:
    return a+b
def mul(a:float,b:float)->float:
    return a*b
def div(a:float,b:float)->float:
    if b == 0:
        raise DivbyzeroError("Cannot divide by zero")
    return a/b

print(add(1,2))
print(mul(1,2))
print(div(1,2))

#Call the risky one inside try/except:

try:
    print(div(5,0))
except DivbyzeroError as e:
    print(f"Handled:{e}")
        



