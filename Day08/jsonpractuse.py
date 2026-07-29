import json
contacts = {
    "Bishal" : 90132541,
    "Kavya" : 908576,
    "kripa" : 9875469,
    "Humans" : False
}

#save dict as json
with open('Day8/jsonpractise.json','w') as f:
    json.dump(contacts,f,indent=2) #Indentation is used to organise and group statements into blocks of code
    print("Done")

#load it back:

with open("Day8/jsonpractise.json") as f:
    loaded = json.load(f)
print(loaded)

#Add a contact and save again:
loaded["Gita"] = "909000000"
with open('Day8/jsonpractise.json','w') as f:
    json.dump(loaded,f,indent=2)
    print('done')
print(loaded)

with open('jsonpractise.json') as f:
    new = json.load(f)
#prit only contact
print("Contacts:",list(new.values()))
#print only 2 first contact:
print("First two contacts:",list(new.values())[:2])

#For name only:
print("Names:",list(new.keys())[::])

print("Contacts now :",len(new))
print("Gita:",new)