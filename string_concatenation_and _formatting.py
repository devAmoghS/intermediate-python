names = ['Harish', 'Kaushik', 'Satyam', 'Sijil']

# for name in names:
#   # print('Hello there, '+ name)
#   print(''.join(['Hello there, '+ name]))

# useful for concatenating multiple strings  
print(', '.join(names))

# import os

# location_of_file = 'C:\\Users\\Amogh S\\Desktop\\Intermediate Python'
# file_name = 'example.txt'

# print(location_of_file, file_name)

# with open(os.path.join(location_of_file, file_name)) as f:
#   print(f.read())
  
who = 'Kaushik'
how_many = '12'

# Kaushik bought 12 mangoes today !
print(who, 'bought', how_many, 'apples today!')
print('{} bought {} apples today!'.format(who, how_many))

# using zero-based indexing to access inputs as parameters
# mandatory in Python 2.X
print('{0} bought {1} apples today!'.format(who, how_many))
print('{1} bought {0} apples today!'.format(who, how_many))
