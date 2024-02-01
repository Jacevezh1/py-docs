# Strings
first = 'Dave'
last = 'Ronald'

# Literal
print(type(first))
print(type(first) == str)
print(isinstance(first, str))

# Constructor
piza = str('Hello')
print(type(piza))
print(type(piza) == str)
print(isinstance(piza, str))

# Concat
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting number to string
decade = str(1980)
print(type(decade))
print(decade)

statement = 'I like sushi since' + decade
print(statement)

multiline = """
Helloooo!

How are you?
"""
print(multiline)

sentence = 'I\'m back at work!\tHey!\nThis is a new line\\this is at'
print(sentence)

print(first)
print(first.lower())
print(first.upper())
print(first)
