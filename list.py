###############################
## Lists
##############################
## def: ordered list of elements - like arrays in JS

colors = ["violet", "pink", "purple"]

## print the list
print(colors)
##get the length of the list
print(len(colors))
## Access individual elements using an index
print(colors[0])

## accessing items by index programmatically
print(colors[2-1])

## use negative numbers to go backwards

print(colors[-1]) #last item in list
print(colors[-2]) ##second to last item in list

## changing items in the list
colors[0] = "cerulean"
print(colors)

#add Item in the list (like push in JS - but can only add one)
colors.append("ocean blue")
print(colors)

# add multiple items to list
colors.extend(["yellow", "peach", "gray"])

print(colors)

#inserting a color into a specific spot
colors.insert(1, "green")
print(colors)

#remove items at a particular index
colors.pop(3)
print(colors)

del colors[1]
print(colors)

## remove()method that removes the first item that matches what you pass in
colors.remove("yellow")
print(colors)

##clear method clears the list
colors.clear()
print(colors)

colors.extend(["violet", "pink", "purple"])
print(colors)

for color in colors:
	print(color) 

##gives you the index 
for idx, color in enumerate(colors):
	print(idx, color)