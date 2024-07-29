li = [1,2,3,4,5,6,7,8,9,10]

def func(x):
    return x**x

# Map function takes a function and takes a list
# Applies the function to each 
# element in the list

'''print(list(map(func, li)))'''

# list comprehension
'''print([func(x) for x in li])'''

print([func(x) for x in li if x%2==0])

