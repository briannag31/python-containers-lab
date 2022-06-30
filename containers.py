#################################
#Dictionaries
###############################
# Def: a key value pair similar to a JS Object but syntactically different

# they are mutable - meaning they can be changed
#other types can be used as keys which is why we have to put quotations on the key for strings
student = {
    "name": "Brianna",
    "course": "seirfx222",
    "current_week": 18
}

print(student)

#Two ways to access keys:
print(student["name"]) #will error if the key does not exist

## using .get, I can specify a default value
print(student.get("email", None)) #email was never specified because this method says, if they key doesn't exist, use the second value to fill it out, basically giving it a fallback value. Can assign it as "None" to not get an error

## change the value of a key
student["name"] = "Brianna Gaines"
student["email"] = "briannagaines31@gmail.com"

print(student)

if 'name' in student:
    print (f"{student['name']}")
else:
    print("nay")

## remove a key from a dict
del student['email']
print(student)

## length of a dictionary (num of keys)
print(len(student))

## Loop over keys only
for key in student: ## key could be any variable
    print(student[key])

print(student.items()) #returns an array of tuples (fixed arrays where you can't add anything to them)

for key, val in student.items():
    print(key, val)

where_my_things_are = {
    "cat": "in the window",
    "ice_cream": "in the freezer",
    "keys": "on the counter"
}

for key, val in where_my_things_are.items():
    print(f"My {key} is kept {val}")


