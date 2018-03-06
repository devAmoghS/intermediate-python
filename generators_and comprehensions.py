input_list = [10,2,20,54,55,15,5,30,26,58,14]

def div_by_five(num):
  if num % 5 == 0:
    return True
  else:
    return False

# generator    
factors_of_five = (i for i in input_list if div_by_five(i))
[print(i) for i in factors_of_five]

# list comprehension
factors_of_five = [i for i in input_list if div_by_five(i)]
[print(i) for i in factors_of_five]

# one-line nested for loops in python
[[print(i, ii) for ii in range(5)] for i in range(5)]
