try:
    n = int("abc")

except ValueError:
    print("Not a number")
    n = 0

print(n) #->0 , no crash

def safe_int(text:str)->int:
    try:
        return int(text)
    except ValueError:
        return 0
    
def safe_div(a:float,b:float)->float|None:
    try:
        return a/b
    except ZeroDivisionError:
        return None
    
print(safe_int("42"))
print(safe_int("abc"))
print(safe_int(""))

print(safe_div(10,2))
print(safe_div(10,0))

    