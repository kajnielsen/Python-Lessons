import os

# os.O_RDONLY = Open file for reading only
# os.O_WRONLY = Open file for writing only
# os.O_RDWR = Open for reading and writing
# os.O_NONBLOCK = Do not block on open
# os.O_APPEND = Append on each write
# os.O_CREAT = Create file if it does not exist
# os.O_TRUNC = Truncate size to 0
# os.O_EXCL = Error if create and file exists
#
# os.close(fd) = Close the file descriptor.
# os.open(file, flags[, mode]) = Open the file and set various flags according to flags and possibly its mode according to mode.
# os.read(fd, n) = ead at most n bytes from file descriptor fd. Return a string containing the bytes read. If the end of the file referred to by fd has been reached, an empty string is returned.
# os.write(fd, str) = Write the string str to file descriptor fd. Return the number of bytes actually written.


def myOS_File_write():
    script_dir = os.path.dirname(__file__)
    filename = "os.myfile.dat"
    path = script_dir + '/' + filename
    f = os.open(path, os.O_WRONLY | os.O_CREAT) #using pipe means that it will be both operations
    data="Goodmorning ÆØÅæøå class".encode('utf-8')
    os.write(f,data)
    os.close(f)

def myOS_File_read():
    f=os.open("test.dat", os.O_RDONLY)
    data=os.read(f,20)
    print (data.decode('utf-8'))


myOS_File_write()