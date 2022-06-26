def remove_duplicate(text):
    result = ''
    for char in text:
        if char not in result:
            result = result+char
    return result

user_input = input("What is your String: ")

no_duplicate= remove_duplicate(user_input)
print(no_duplicate)
