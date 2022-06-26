import re

# pattern = r"colo.r"
# pattern = r"^colo.r$"

# pattern = r"a*"

# pattern = r"(ab)*"

# pattern = r"a+"
# pattern = r"a+b"
# pattern = r"a*b"

# pattern = r"ice(-)?cream"
pattern = r"a{1,3}$"
if re.match(pattern,"aaaa"):
    print("Matched")
else:
    print("Not Matched")