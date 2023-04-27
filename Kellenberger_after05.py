#after 05
def back(s):  #function to return the reverse of a string
    #return the string backwards
    #example: back('GIS') returns 'SIG'
    
    return s[::-1]


def ends(s):  # function that selects first 3 and last 3 letters in a string (s)
    #return the 6 letters in the original order in a single string
    #example: ends('Geography") returns 'Geophy'
    
    result = ""
    first = s[0:3]
    last = s[-3:]
    result = first + last
    return result

def skips(s):  # function that selects every third letter in a string
   # return a new string
   #example: skips('Geography') returns 'Ggp'
   
   return s[::3]


def bskips(s):  # function that returns every third letter in a string going backwards
    #return the string 
    #example: bskips('Geography') returns 'yao'
      
    return s[::-3]

    
def secone(s,l): #function that reports the second position of a letter (l) in a string (s), 
    # return the position as an integer or return -1 if not found
    #example: secone('geography','g') returns 3,  secone('geography','e') returns -1
    
    return s.find(l, s.find(l)+1)


def picklastone(s,l,n): #function that reports the nth to the last position of a letter (l) in a string (s), 
    # return the position as an integer or return -1 if not found
    #example: picklastone('beekeeper','e',2) returns 5, picklastone('beekeeper','e',1) returns 7

    found = []
    i = 0
    
    while i < len(s) - 1:
        if s[i] == l:
            found.append(i)
        i += 1
    
    return found[-n]

 
def upit(s): #function to convert a string to upper case
     #return the upper case string
     #example: upit('Geography') returns 'GEOGRAPHY'
     
     return s.upper()

def breakit(s,c): #function to return a list of strings for a string (s) split on a particular character (c)
     #return the split list
     #example: breakit('Geography','g') returns ['Geo','raphy'], breakit('apple','p') returns ['a', '', 'le']
    
     return s.split(c)

def isthere(s,c): #function that finds a part (c) in a string(s)
    #return boolean True or False
    #example: isthere('Geography','gra') returns True
    
    if s.find(c) != -1:
        return True
    else:
        return False
