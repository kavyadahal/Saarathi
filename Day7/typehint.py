
def greet(name):
    return f"Hi {name}"

def add(a : int, b: int)-> int:
    return a+b

def to_f(c:float)->float:
    return c*9/5+32

count :int = 0

def total(nums:list[int])->int:
    return sum(nums)

def count_words(text:str)->dict[str,int]:
    ...

def find(name:str)->str|None:
    ...
