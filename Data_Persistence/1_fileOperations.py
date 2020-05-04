import sys, os

#readline() takes 'one' inputline from console
def myReadline():
    x = sys.stdin.readline()
    print('From readline(): ' + x)


# the open() function is used to interact with files
# it uses the following arguments:
# variable = open(name, mode, buffering)
# The following parameters are avialable:
# r = open for reading
# w = open for writing, truncating the file first
# x = create new file and open it for writing
# a = open for writing, append to the end of the file if it exists
# b = binary mode
# t = text mode (default)
# + = open a file for updating (read and write)
# w+ = simultanious write and read mode, without closing a file - it is important to use .close after operations has ended.

def myFileWrite():
    myFile = open('fileOperations.txt', 'w')
    #string = ['vi19iisa220', 'stud1', 1234560001]
    string = "vi19iisa220	stud1	123456-0001	Donna Montoya	55511111	03-02-2020	19-06-2020	8kjAXWRLQT	Donna	Montoya	Prinsens alle 2, 1234	8800	Viborg	51234	55511111	stud1@student.eadania.dk	Programming, Network, IoT, How not to fall alseep during an online lecture, pentest\n"
    myFile.write(string)
    myFile.close  # remember to use .close to make sure that the stream has finished writing and the content is saved to the file



def myFileRead():
    f = open('fileOperations.txt', 'r')
    string = f.read()
    print(string)


def multiLineWrite():
    f=open('fileOperations.txt','a')
    lines=['Java Tutorials\n', 'DBMS tutorials\n', 'Mobile development tutorials\n']
    f.writelines(lines)
    f.close()

def readAndWriteBinary():
    f=open('fileOperations.bin', 'wb+')    
    print(f.write(b'013456789abcdef'))
    
    print(f.seek(5)) # using 'seek' we are moving the point to the position, here the 6th position

    print(f.read(1))

    print(f.seek(-3, 2)) # Sets the file's current position. 0-begin 1-current 2-end.

    print(f.read(1))

    f.close()


multiLineWrite()