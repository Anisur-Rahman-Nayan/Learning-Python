file = open("sports","r+") #file = open("sports","w") #file = open("sports","r")
print(file.readable())    #print(file.writable())
text = file.read()        #text = file.readlines()[1]
print(text)
file.close()