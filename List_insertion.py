# Inserting an item to a list
my_list = []
some_variable = 3

# insert item some_variable into the list 

# Inserting using the append method
my_list.append(some_variable)  

my_list.append("some string")

# Inserting using the lists index. NB This will replace the item in that index with the new item

my_list[0] = 1


#Inserting Using the + operator with another list NB This is known as concatenation

new_list = ['ass', 234]

my_list = my_list + new_list

# Inserting using the * operator and an int NB This will duplicate the items in the list by the given number
my_other_list = my_list * 3

# Removing an item from the lis is simple
del my_list[0]
print(my_list)
print(my_other_list)



#Resources used https://www.digitalocean.com/community/tutorials/understanding-lists-in-python-3