

def myExampleOne():
    numbers=[10,20,30,40]
    myFile=open('numbers.txt','wt')
    myFile.write(str(numbers))
    myFile.close()

def myExampleTwo():
    numbers=[10,20,30,40, 70, 80, 90]
    myFile=open('numbers.txt','wb+')
    data=bytearray(numbers)
    myFile.write(data)
    myFile.close()

def myExampleThree():
    myFile=open('numbers.txt','rb')
    data=myFile.read()
    print(list(data))


myExampleThree()



# Other options for serialization:
# pickle
# marshal
# shelve
# dbm
# csv
# json
