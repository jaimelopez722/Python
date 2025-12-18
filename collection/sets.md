# Sets in Python

---
A Set in Python is used to store a collection of items with the following properties.

- No duplicate elements. If try to insert the same item again, it overwrites previous one.
- An unordered collection. When we access all items, they are accessed without any specific order and we cannot access items using indexes as we do in lists.
- Internally use hashing that makes set efficient for search, insert and delete operations. It gives a major advantage over a list for problems with these operations.
- Mutable, meaning we can add or remove elements after their creation, the individual elements within the set cannot be changed directly.
```python
s = {10, 50, 20}
print(s)
print(type(s))
```
#### Output
```
{10, 50, 20}
<class 'set'>
```
```
Note: There is no specific order for set elements to be printed
```


