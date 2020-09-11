message = "Hello World"

print(message)

# string spanning multiple lines
m = """ This is a string
that spans multiple lines.
    """
print(m)

# print length of string
print(len(m))

# accessing individual characters of string
print(message[10])

""" SLICING """
# accessing range of characters
print(message[0:5]) # begins from the start to character before 5
print(message[6:])

""" STRING METHODS """
# print(message.lower()) 

# print(message.upper())

print(message.count("l"))

# find the index of characters
print(message.find('World')) # RETURNS -1 INCASE NOT FOUND

# new_message = message.replace("World","Universe")

greeting = 'Hello'

name = 'Martins'

# morning = greeting + ', ' + name + '. Welcome!'


# use a formated string
morning2 = '{},{}. Welcome!'.format(greeting,name)



# f-strings
morning3 = f'{greeting},{name.upper()}. Welcome!!!'

print(morning3)