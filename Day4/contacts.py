contacts = {
    "Kavya": "9800000001",
    "Sita": "9800000002",
    "Ram": "9800000003",
}

#Print one persons number:
print("Sita :",contacts["Sita"])

#Add a fourth:
contacts["Gita"] = "98000004"

#Loop and print everyone

for name , phone in contacts.items():
    print(f"{name}:{phone}")

#Stretch : Safe lookup for a name that may not exist 
print("Hari : ",contacts.get("Hari","not found"))
