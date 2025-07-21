# Comma Code

# I need to write a function that takes a list value as an argument and returns a string with all the items seperated by a comma and a space, with 'and' inserted before the last item.

def commaCode(items):

    if len(items) == 0:
        return ''
    elif len(items) == 1:
        return items[0]
    else:
        return ', '.join(items[0:-1]) + ' and ' + items[-1]
    
print(commaCode([]))
