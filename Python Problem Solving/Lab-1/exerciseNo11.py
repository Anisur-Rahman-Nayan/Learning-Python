'''Given a string, display only those characters which are present at an even index number. Read inputs
from the user.
'''

def text(s):
    st =''
    for i in range(len(s)):
        if i % 2 ==0:
            st = st+ s[i]
    print(f"Even index Number characters is : {st}")

user_input = str(input("Enter the any String: "))
text(user_input)