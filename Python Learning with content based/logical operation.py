#and , or , not

mark = int(input("Enter Your Mark : "))

if(mark <= 100 and mark >= 80):
    print("A+")
elif(mark <= 79 and mark >= 70):
    print("A")
elif(mark <= 69 and mark >= 60):
    print("A-")
elif(mark <= 59 and mark >= 50):
    print("B")
elif(mark <= 49 and mark >= 40):
    print("C")
elif(mark <= 39 and mark >= 33):
    print("D")
else:
    print("F")