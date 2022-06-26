import re

pattern = r"colour"
text = "My favourite color is red"

ans = re.sub(pattern,"color",text) #count=1

print(ans)