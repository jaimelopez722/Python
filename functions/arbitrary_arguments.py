# *args     = allows you to pass multiple non-key arguments
# **kwargs  = allows you to pass multiple keyword-arguments
#             * unpacking operator

def add(*args):
    result = 0
    for arg in args:
        result += arg
    return result

def details(**kwargs):
    for key, value in kwargs.items(): # items method returns key value pairs
        print(f'{key}: {value}')

# *args
print(add(1,2,3,4))


# **kwargs
print(details(class1 = "Math",
              class2 = "Python",
              class3 = "Programming",))
