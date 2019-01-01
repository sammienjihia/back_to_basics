"""
In this python code, we shall discuss about the python yield keyword, generators and iterables

"""

# 1. Iterables
"""
When you create a list, you can access it's items one by one and that's called iteration
"""

arr = [1,2,3,4,5]

for item in arr:
	print(item)

# List comprehension, creating a list from another iterable

new_list = [item**2 for item in arr]

print(new_list)

"""
Iterables are handy because you can read them as much as you want, but you store all the values in memory
 and it's not always what you want when you have alot of values
"""

# 2. Generators
"""
Generators are iterators but you can only iterate over them once
"""

my_gen = (item*item for item in arr)

for i in range(2):
	print("{}'th iteration".format(i))
	for key in my_gen:
		print(my_gen)


# 3. Yield
"""
Yeild is a keyword same as return except the function will return a generator. 

NB: When you call the function, the code in the function body does not run. The function only return a genarator object 
"""

def my_Gen():
	my_list = range(3)

	for i in my_list:
		yield i*i

# Create a generator object
gen_object = my_Gen()

for i in range(2):
	print("{}'th iteration".format(i))
	for item in gen_object:
		print(item)
