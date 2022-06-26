import re
pattern = r"[aeiou]"

# pattern = r"[A-Z]"
# pattern = r"[0-9]"
# pattern = r"[0-9][A-Z][a-z]"

if re.match(pattern,"anisur rahman nayan"):
    print("Match")
else:
    print("not Match")