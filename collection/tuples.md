# Python Tuples

---

A tuple in Python is an immutable ordered collection of elements.

- Tuples are similar to lists, but unlike lists, they cannot be changed after their creation (i.e., they are immutable).
- Tuples can hold elements of different data types.
- The main characteristics of tuples are being ordered, heterogeneous and immutable.

## Creating a Tuple

---
A tuple is created by placing all the items inside parentheses (), separated by commas. A tuple can have any number of items and they can be of different data types.

```python
tup = ()
print(tup)

# Using String
tup = ('Geeks', 'For')
print(tup)

# Using List
li = [1, 2, 4, 5, 6]
print(tuple(li))

# Using Built-in Function
tup = tuple('Geeks')
print(tup)
```

#### Output
```
()
('Geeks', 'For')
(1, 2, 4, 5, 6)
('G', 'e', 'e', 'k', 's')
```

Let's understand tuple in detail:

### Creating a Tuple with Mixed Datatypes

---
Tuples can contain elements of various data types, including other tuples, lists, dictionaries and even functions.
```python
tup = (5, 'Welcome', 7, 'Geeks')
print(tup)

# Creating a Tuple with nested tuples
tup1 = (0, 1, 2, 3)
tup2 = ('python', 'geek')
tup3 = (tup1, tup2)
print(tup3)

# Creating a Tuple with repetition
tup1 = ('Geeks',) * 3
print(tup1)

# Creating a Tuple with the use of loop
tup = ('Geeks')
n = 5
for i in range(int(n)):
    tup = (tup,)
    print(tup)
```
#### Output
```
(5, 'Welcome', 7, 'Geeks')
((0, 1, 2, 3), ('python', 'geek'))
('Geeks', 'Geeks', 'Geeks')
('Geeks',)
(('Geeks',),)
((('Geeks',),),)
(((('Geeks',),),),)
((((('Geeks',),),),),)
```
