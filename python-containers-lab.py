## Exercise 1
students = ['brianna', 'jack', 'ryan']
print(students[1])
print(students[-1])

## Exercise 2
foods = ('cheese', 'cake', 'bread')
for food in foods:
    print(f"{food} is a good food")

## Exercise 3
# for food in foods:
print(foods[1:])

## Exercise 4
home_town = {
    "city": "los angeles",
    "state": "california",
    "population": "TOO MANY PEOPLE"
}

print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")

## Exercise 5 -- I am not totally sure what the question is asking, so this may be incorrect :/

cohort = []
for name in students:
    cohort.append({"student": name, "fave_food": "cake"})

print(cohort)

## Exercise 7
awesome_students = [f"{student} is awesome" for student in students]
print(awesome_students)

## Exercise 8

foods_with_a = [food for food in foods if "a" in food ]

print(foods_with_a)
