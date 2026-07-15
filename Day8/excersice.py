"""with open("data/excersice.txt", "w") as f:
    content = f.write("HI\nI am kavya\nI love coding\n")

with open("data/excersice.txt",'a') as f:
    content = f.write("Good morining")

with open("data/excersice.txt",'r') as f:
    context = f.read()

print(context[::-1])"""

with open("data/excersice.txt", "r") as f:
    lines = f.readlines()

for line in lines[::-1]:
    print(line, end="")

    
"""print(context)
count = 0
with open("data/excersice.txt",'r') as f:
    for line in f:
        line = line.strip()
        if line:
            count +=1
print(count)
"""

