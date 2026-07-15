num = 7
total = 0

for i in range(1,11):
    result = num * i
    print(f"{num}*{i}={result}")
    total = total + result

#Sum of whole table:
print(f"Sum of the {num} times table : {total}")
