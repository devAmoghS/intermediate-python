# range is a generator

# example of a list comprehension
num_list = [i for i in range(5)]
# num_list is [0, 1, 2, 3, 4]

# this is same as 
# num_list = []
# for i in range(5):
#   num_list.append(i)
# print(num_list, "using append")

# generator expression for the same
num_list_gen = (i for i in range(5))
# print(num_list_gen) # this is a generator object
# instead iterate over num_list_gen

# for n in num_list_gen:
#   print(n)

i = range(999)
# i is a range object range(0, 999)

# List comprehension are *faster* than generators in most cases
# But they take up *more memory* unlike generators

something = [i for i in range(50000000)] # this takes some time and memory
print("done")
something = (i for i in range(50000000)) # this takes no memory
print(something)
