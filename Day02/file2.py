raw = " Kavya DAHAL "
#Name formatiing 

print(raw.strip().title())

name = "Sprite fanta"
print(f"welcome, {name}!")

score = 72
if score >= 90:
    print("A")
elif score >= 60:
    print("B")
else:
    print("Keep going")

age = 20
has_id = True
if age>= 18 and has_id:
    print("Allowed")

if not has_id:
    print("Bring ID")

