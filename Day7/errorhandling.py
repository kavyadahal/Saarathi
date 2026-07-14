try:
    n = int("abc")

except ValueError:
    print("Not a number")
    n = 0

print(n) #->0 , no crash
def set_age(age:int)->int:
    if age<0:
        raise ValueError("age < 0")
    return age

try:
    