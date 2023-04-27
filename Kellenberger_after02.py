#after 02
def add1(x):  # function to add 1 to any number passed to it (x) integer or float
    #return the result
    #example add1(4) returns 5
    
    return x+1
    

def mult(x,y): # function to multiply any two numbers (x,y) passed in
    #return the result
    #example mult(5,4) returns 20
    
    return x*y
    

def concat(a,b): #function that concatenates two strings(a,b) with a single space in between
    #return the string result
    #example concat('Bob','Jones') returns 'Bob Jones'
    
    string = a + " " + b
    return string
    

def repeat(a,num): #function to repeat a string (a) a user requested number (num) of times
    #return the string result
    #example repeat('Ha',3) returns "HaHaHa'
    
    string = a*num
    return string
    

def slopedeg(dx,dy): # function use the math or numpy library to compute the slope of a line in degrees given the rise (y) and run (x)
    #return the slope as an integer number by conversion to int()
    #example slopedeg(4,4) returns 45, slopedeg(3,4) returns 53
    
    import numpy as np
    x = np.arctan(dy/dx)
    y = np.rad2deg(x)
    return int(y)
    
    

def power(x,y): # function to return the value of one variable (x) rasied to the power of a second variable (y)
    # return the result as a decimal number
    #example power(2,3) returns 8.0
    
    return x**y
    

def into(x,y): # function to answer how many times the first number (x) goes into the second(y), both are integers 
    # return both the number of integer times and the remainder 
    # Example: into(3,10) returns (3,1) 
    
    times = y / x
    rem = y % x
    return (int(times), int(rem))
    

def makestr(x): # a function that takes any numeric input (x)  and returns a string
    #return the string
    #example: makestr(55.75) returns '55.75'
    
    return str(x)
    

def rectp(x1,y1,x2,y2): # a function that takes two corners of a rectangle (x1,y1) and (x2,y2) and returns the perimeter. Do not assume x2 and y2 are greater than x1, y1.
    #return the perimeter as a decimal number
    #example(rectp(2,2,4,4) returns 8.0
    
    length = x2-x1
    width = y2-y1
    p = (length*2) + (width*2)
    return float(p)
    

def rectarea(x1,y1,x2,y2): # a function that takes two corners of a rectangle (x1,y1) and (x2,y2) and returns the area. Do not assume x2 and y2 are greater than x1, y1.
    #return the area as a decimal number
    #example: rectarea(2,2,4,4) returns 4.0
    
    length = x2-x1
    width = y2-y1
    return float(length) * float(width)