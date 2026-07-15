import json

data = {"name":"Kavya","age":21} #dict

print(json.dumps({1:"x"}))

"""print(json.dumps({1,2}))  not serializable
print(json.dumps([1,2]) # List to string
"""

#indent breaks into different lines
json_example = json.dumps(data,indent=2) #string type
print(type(data))
print(type(json_example))
print(json_example)

#loads function:string and convert it into a corresponding Python object
json_strings= '{"name": "Kavya", "isStudent": false}'
print(json.loads(json_strings))
print(type(json.loads(json_strings)))