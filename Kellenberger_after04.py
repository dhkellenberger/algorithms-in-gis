#after 04
def addodds(s):    #add all odd integers less than a passed value (s)
    #return the sum
    # example addodds(5) returns 4 (1 + 3), addodds(4) returns 4 (1 + 3)
    
    total = 0
    i = 1
    
    while i < s:
        total += i
        i += 2
        
    return total
        
def addevens(s):    #add all even integers less than or equal to a passed value (s)
    #return the sum
    # example addevens(5) returns 6 (2 + 4)
    # example addevens(24) returns 156
    
    total = 0
    i = 2

    while i <= s:
        total += i
        i += 2
    
    return total

def multints(a,b): #given two integers, 
    #return the result of multiplying all intermediate integers including the lowest and not including the highest
    #example multints(2,6) returns 120.0 (2*3*4*5)
    
    total = 1.0
    i = a
    
    while i < b:
        total *= i
        i += 1
        
    return total

def nest(xmin, xmax, ymin, ymax): # given 4 integers 
    #return the sum of all pairs of those integers in an inclusive nested loop set
    #example nest(1,2,5,6) returns 28 (1+5 + 1+6 + 2+5 + 2+6)
    #example nest(11,12,3,4) returns 60 (11+3 + 11+4 + 12+3 + 12+4)
    #example nest(1,12,6,17) returns 2592
    
    total = 0
    i = xmin
    j = ymin
    
    while i <= xmax:
        total += i+j
        j += 1
        if j > ymax:
            j = ymin
            i += 1
    
    return total

def else1(n): # given a number, we want to see if it has a factor 5 or less
    #return True if so, False if not, stop checking once you know it is True
    #example else1(23)  returns False as none of the values 2, 3, 4, 5 are integer factors of 23
    #example else1(15) returns True as 3 is a factor of 15
    
    i = 2
    
    while i <= 5:
        if n % i == 0:
            return True
        else:
            i += 1
    
    if i > 5:
        return False

def small(n): #divide a number by 1.05 until the result is <= 1.0.  
    #Return the number of divisions when the result falls <= 1.0
    #example small(5) returns 33, small(1) returns 0, small(1.05) returns 1
    
    total = 0
    
    if n / 1.05 >= 1.000:
        total += 1
        n = n / 1.05
        while n > 1.000:
            total += 1
            n = n / 1.05
    
    return total

def saveit(interest): #how many years does it take to grow $1000 to at least $10000 given an interest rate (interest)_
    # enter the interest rate as a decimal (for example for 5% enter 0.05)
    # return the number of years it will take 
    #example saveit(.05) returns 48, saveit(.07) returns 35, saveit(1) returns 4

    total = 1
    current = 1000
    goal = 10000
    
    while current * (1+interest) <= goal:
        total += 1
        current *= (1+interest)
        
    return total
