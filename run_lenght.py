arg = "aaabbccccddd"
def runlenght(arg):
    result = ''
    last_char = ''
    count = 1

    for char in arg:
        if char != last_char:
            if last_char:
                result += str(count) + last_char
            count = 1
            last_char = char
        else:
            count += 1
    result += str(count) +  last_char
    return result
