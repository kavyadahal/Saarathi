# --- Day 1: types, operators, truthiness ---
print(7 // 2, 7 % 2, 2 ** 3)        # predict:
print(bool(""), bool("0"), bool(0))  # predict:

# --- Day 2: strings, f-strings, conditions ---
s = "Python"
print(f"{s[:2]}-{s[-1]}")            # predict:
print("a,b,c".split(","))

x = 10
if x > 5 and x < 20:
    print("A")                       # predict: does this run?
else:
    print("B")

# --- Day 3: loops, accumulate, break/continue ---
total = 0
for i in range(1, 6):
    if i % 2 == 0:
        continue
    total += i
print(total) 

n = 10
while n > 1:
    n = n // 2
print(n) 

# --- Day 4: collections ---
words = "ai ml ai".split()
#A set stores only unique values. Duplicate values are removed.
print(len(words), len(set(words)))

d = {"a": 1}
print(d.get("b", 0) + d["a"])

xs = [5, 3, 8]
xs.append(1)
xs.sort()
print(xs, sum(xs), max(xs))