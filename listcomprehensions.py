##################
## List Comprehensions
##################
## def: simple syntax for generating lists from other lists

####################
##basic syntax
###################
# [<expression> for <item> in <list>]
# This reads as: I want <expression> for each <item> in <list>

#########################
## Without Comprehensions
##########################
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# I want 'n * n' for each 'n' in nums 
squares = []
for n in nums:
	squares.append(n * n)
print(squares)


#############################
## With Comprehensions
############################
squares2 = [n*n for n in nums]
print(squares2)


#########################
## Without Comprehensions
##########################

# I want 'n * n' for each 'n' in nums  if 'n * n' is even
even_squares = []
for n in nums:
	square = n * n 
	if square % 2 == 0:
		even_squares.append(square)
print(even_squares)

#############################
## With Comprehensions
############################
## [EXPRESSION for ITEM in LIST if BOOLEAN EXPRESSION]
even_squares2 = [n * n for n in nums if (n * n) % 2 == 0]
print(even_squares2)


