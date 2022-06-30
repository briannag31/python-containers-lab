##################
## Tuples
##################
## def: immutable lists - an array/list of items that cannot be changed once set - use parentheses instead of square brackets

colors = ("pink", "purple", "violet")
print(colors)

print(len(colors))

## single element tuples need a trailing comma
print(("hello"))
print(("hello",))

##Tuples can be created without using any parentheses
colors2 = 'red', 'green', 'blue'
print(type(colors2))

## Unpacking
colors3 = ('red', 'green', 'blue')
red, green, blue = colors3
print(red, green, blue)

###########
##assign a slice of a sequence to a variable
nums = [1,2,3,4,5,6,7]

some_nums = nums[1:5]

copy = nums[0:]

print(some_nums)
print(copy)