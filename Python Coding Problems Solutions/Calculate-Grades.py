print("Enter Your Marks.....")

sub1 = int(input("1st Subject: "))
sub2 = int(input("2nd Subject: "))
sub3 = int(input("3rd Subject: "))
sub4 = int(input("4th Subject: "))
sub5 = int(input("5th Subject: "))

avg = (sub1+sub2+sub3+sub4+sub5)/5

if avg >= 90:
    print("Grade: A ")
elif avg >=80:
    print("Grade: B ")
elif avg >=70:
    print("Grade: C")
elif avg >=60:
    print("Grade: D")
else :
    print("Grade: F")
