for i in range(1,11):
    print(i)

#Only even number:
print("Evens:")
for i in range(1,11):
    if i % 2 == 0:
        print(i)

#How many numbers 1-100 are divisible by 7
count = 0
for i in range(1,101):
    if i%7 == 0:
        count = count+1
print(f"Divisible by 7:{count}")

#Each letter of your name with its position
name = "Kavya"
for i in range(len(name)):
    print(i,name[i])