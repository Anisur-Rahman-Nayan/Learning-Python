import re

pattern = r"color"

#if re.match(pattern,"color , I love red color"):
#if re.search(pattern,"Red is a color , I love red color"):

# if re.search(pattern,"Red is a color , I love red color"):
#     print("Match")
# else:
#     print("Not Match")

print(re.findall(pattern,"Red is a color , I love red color"))