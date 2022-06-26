
# try:
#     list = [10,0,2]
#     result = list[0] / list[1]
#     print(result)
# except ZeroDivisionError:
#     print("Dividing by Zero is not possible")

# try:
#     list = [10,0,2]
#     result = list[0] / list[3]
#     print(result)
# except IndexError:
#     print("Index Error")

try:
    list = [10,0,2]
    result = list[0] / list[1]
    print(result)
except ZeroDivisionError:
    print("Dividing by Zero is not possible")
finally:
    print("Successful")