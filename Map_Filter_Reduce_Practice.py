# Created by Noel Willems
# Sources:
# https://docs.python.org/3/howto/functional.html (understanding functional programming in Python)
# https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/ (understanding reduce in Python - had to figure out that I had to import functools)

from functools import reduce

my_in = [5,10,15,20,25,30]
result = []
print("starting point")
print(my_in)
print("multiply elements by 2")
result = list(map(lambda x: x*2, my_in))
print(result)
print("square elements")
result = list(map(lambda x: x**2, my_in))
print(result)

my_in = ["one", "fish", "two", "fish","red","fish","blue","fish"]
print("starting point")
print(my_in)
print("capitalize")
result = list(map(lambda x: x.capitalize(), my_in))
print(result)

my_in = [5,10,15,20,25,30]
print("starting point")
print(my_in)
print("select even")
result = list(filter(lambda x: (x % 2 == 0), my_in))
print(result)

my_in = ["one", "fish", "two", "fish","red","fish","blue","fish"]
print("starting point")
print(my_in)
print("not fish")
result = list(filter(lambda x: (x != "fish"), my_in))
print(result)

my_in = [5,10,15,20,25,30]
print("starting point")
print(my_in)
print("sum the squares (optional)")
result = reduce((lambda x, y:x + y), my_in)
print(result)