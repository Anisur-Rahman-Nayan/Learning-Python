def reverse_stack(str):
    stack = []

    for char in str:
        stack.append(char)

    rev = ''
    while len(stack) > 0:
        last = stack.pop()
        rev = rev + last

    return rev

user_str = input("What is your string: ")
reverse = reverse_stack(user_str)
print(reverse)