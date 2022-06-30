###################################
## Functions
#################################
## def: creating bunches of code we can use over and over again

def add_nums():
    return 1 + 1

print(add_nums())

def add_nums2(num1, num2):
    print("num1 is: ", num1)
    print("num2 is: ", num2)
    return num1 + num2

print(add_nums2(4,12))
print(add_nums2(num2=4,num1=12))


### Args & Kwargs

def get_all_args(*args, **kwargs): #one asterisk (args) will get a tuple of all args, two asterisks (kwargs) will create  dictionary of any key arguments // kwargs stands for key word args
    print(args)
    print(kwargs)

get_all_args(1, 2, 3, 4,5, cheese="gouda", bread="rye")
## prints out (1,2,3,4,5) {'cheese': 'gouda', 'bread': 'rye'} - args pulls out everything that doesnt have a key and kwargs will

def add_all_nums(*args):
    count = 0
    for arg in args:
        count = count + arg
    return count

print(add_all_nums(1,2,3,4,5,6))
print(add_all_nums(1,2,3))


################################
## Defining empty functions
################################
def first_function():
  pass ## you have to add pass until you are ready to actually add data to the function

########################################
## lambda functions
##################
## Pythons version of arrow functions - mainly for functions that take callbacks - single line of code

## normal version
def add_numbers_long_way(x,y):
    return x+y

## Lambda version
add_numbers = lambda x,y: x + y

print(add_numbers(4,7))

######################
## python callback functions
#######################

##map(callback/lambda, array) - in python you say lambda, not callback - does something on each item of the array

nums = [1, 2, 3, 4, 5, 7,9]
map_result = map(lambda x: x+1, nums)

print(map_result) ## this will give you the map object back which means nothing: <map object at 0x1046a0fa0>

map_result2 = list(map(lambda x: x+1, nums))

print(map_result2)

## using comprehensions
result3 = [x+1 for x in nums]
print(result3)

## Filter Function - returns filtered items
##filter(lambda, list)
filter_result = list(filter(lambda x: x%2==0, nums))
print((filter_result))

## Using list comprehension
result4 = [x for x in nums if x % 2 == 0]
print(result4)

## Using List Comprehension
final_result = [x + 1 for x in nums if x % 2 == 0 ]
print(final_result)

## Dictionary comprehension
## key:value for item in collection
alex = [("name", "Alex"), ("age", 36)]

alex_dictionary = {x[0]:x[1] for x in alex}

print(alex_dictionary)
def add(a, b):
    return a + b

# print(add(10, 100.))
# print(add(10, '10')) wrong
# print(add(100)) wrong
# print(add('abc', 'def'))
# print(add(10, 20, 30)) wrong