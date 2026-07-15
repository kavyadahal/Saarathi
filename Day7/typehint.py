
def greet(name):
    return f"Hi {name}"

def add(a : int, b: int)-> int:
    return a+b

def to_f(c:float)->float:
    return c*9/5+32

def grade(score: int) -> str:
    if score >= 80:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 40:
        return "C"
    else:
        return "Fail"

def average(nums:list[float])->float:
    return sum(nums)/len(nums)

def total(num:list[int])->int:
    return sum(num)

count :int = 0

def count_words(text:str)->dict[str,int]:
    ...

def find(name:str)->str|None:
    ...

#Stretch : returns a string OR None:
def find_name(names:list[str],target:str)->str |None:
    for name in names:
        if name == target:
            return name
    return None
print(to_f(30))            # 86.0
print(grade(72))                   # B
print(average([4, 9, 1, 6]))       # 5.0
print(total([1, 2, 3, 4]))         # 10
print(find_name(["ai", "ml"], "ml"))   # ml
print(find_name(["ai", "ml"], "rag"))  # None
