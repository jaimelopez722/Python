# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. positional 2. default 3. KEYWORD 4. arbitrary

def hello(greeting, title, first, last):
    print(f"Hello {greeting} {title} {first} {last}")

hello("Hello", title = "Mr.", first = "John", last = "Doe")