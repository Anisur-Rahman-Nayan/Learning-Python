from datetime import datetime

date_string = "21 June, 2021"
print("date_String : ", date_string)

date_object = datetime.strptime(date_string,"%d %B, %Y")
print("Date_Object : ", date_object)