mydict = {"name": "Max", "age": 28, "city": "New York"}
mydict["email"] = "max@xyz.com"
print(mydict)

# del mydict["name"]
# print(mydict)

# mydict.popitem()
# print(mydict)

if "age" in mydict:
    mydict.pop("age")
print(mydict)

try:
    print(mydict["name"])
except:
    print("error")

for key in mydict.keys():
    print(key)

mydict_cpy = mydict
mydict_cpy["email"] = "max@xyz.com"
print(mydict_cpy)
print(mydict)



