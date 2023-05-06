#after 08

import struct

def printnums(num): #function to return a formatted strng with NO SPACES that gives the decimal and binary of an input integer between 1-100 
    #separated by a comma 
    # example: printnums(2) gives '2,10', printnums(99) returns '99,1100011'
    
    x = bin(num)[2:]
    
    y = str(num) + "," + str(x)
    
    return y

    
def binread(fl):  #reads a binary file ('binread.bin' is on canvas in this assignment) with 5 integers 4 floats from file "fl", 
    #returns a tuple of the contents
    # example: binread('binread.bin') returns (12, 14, 54, 65, 78, 12.100000381469727, 24.600000381469727, 54.79999923706055, 52.099998474121094)
    #I will use a file with a different set of data but the same types and order
    
    with open(fl,'rb') as f:
        data = f.read()
        x = struct.unpack('5i4f', data)
    
    return x

