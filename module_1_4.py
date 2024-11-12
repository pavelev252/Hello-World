my_string = input()
print(len(my_string),
      my_string.upper(),
      my_string.lower(),
      ''.join(my_string.split()),
      my_string[0], my_string[-1],
      sep='\n')
