n = int(input("Enter The Last Number : "))
sum = 0

#
# for x in range(1,n+1,2):
#     sum = sum+x
#
# print(sum)

# for x in range(1,n+1,1):
#     sum = sum + x*x
#
# print(sum)

for x in range(1,n+1,1):
    sum = sum + (1/x)

print(sum)