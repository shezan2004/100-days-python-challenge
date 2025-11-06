info = {
    "key" : "value",
    "name": "shezan",
    'subjects': ["python", "c++"],
    "learning" : "coding",
    "age" : 35,
    "is_adult" : True,
    "marks" : 94.4,
    12.99 : 45.6
}
info["name"] = "Touhid"
print(info["name"])
print(info.get("learning"))# get method to call values
print(info)
#nesting dictionary
student ={
    "name": "rafi",
    "subjects": {
        "phy":50,
        "che": 98,
        "math": 95
    }
}
student.update({"city" : "Dhaka", "age":16})
print(student["subjects"]["che"])
#print(len(student))
#typecasting 
print(len(list(student.keys()))) 
print(list(student.values()))
pairs =list(student.items())
print(pairs[0])