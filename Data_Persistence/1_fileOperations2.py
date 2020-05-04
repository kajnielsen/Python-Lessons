import sys, os

def myWriteToFile():
    xw = sys.stdin.readline()
    fw = open('fileOperations2.txt', 'a+')
    fw.write(xw)
    print("Your input has now been written to file")
    string = fw.read()
    print("The file content is: \n" + string)
    fw.close()

myWriteToFile()