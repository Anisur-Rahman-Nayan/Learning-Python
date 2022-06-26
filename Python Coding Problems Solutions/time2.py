from datetime import date

today = date.today()

#dd/mm/yy

d1 = today.strftime("%d/%m/%Y")
print("d1 : ", d1)

#Textual month , day , year

d2 = today.strftime("%B %d, %Y")
print("d2 : ",d2)

#mm/dd/y

d3 = today.strftime("%m/%d/%y")
print("d3 : ",d3)

#month abbreviation, day and year

d4 = today.strftime("%b-%d-%Y")
print("d4 : ",d4)