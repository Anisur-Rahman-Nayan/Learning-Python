# stack
# colors = []
# colors.append("Black")
# colors.append("white")
# colors.append("blue")
#
# print(colors)
#
# colors.pop()
#
# if not colors :
#     print("no colors left")
#
# print(colors)

# queue
from collections import deque

bank = deque(["A","B","C"])
bank.popleft()
print(bank)