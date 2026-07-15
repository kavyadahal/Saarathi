#Read
"""with open("test_file.txt","w") as f:
    content = f.read()

print(content)"""

#Append doesnt overwrite
"""with open("test_file.txt","a") as f:
    content = f.write("Hello i am  very happy")"""

#Write overwrites previous text
"""with open("test_file.txt","w") as f:
    content = f.write("Hello i am  very happy")"""

count = 0 
with open("data/test_file.txt",'r') as f:
    for line in f:
        line = line.strip()
        if line:
            count +=1

print(count)

open("data/test_file.txt").read()

    


