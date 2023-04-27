#after 03
def div3(x,y):  # determine if a first integer (x) is an even multiple of the second (y) 
    #return a Boolean - True or False (not a string!!!)
    #example div3(10,5) returns True, div3(5,10) returns False, div3(11,5) returns False
    
    if x % y == 0:
        return True
    else:
        return False



def rps(u1,u2): # rock, paper, scissors game with two text inputs of ('rock', 'paper', or scissors').  
    #Return winner as a string ('u1' or 'u2'), or if same  "It's a tie" (case matters - be precise as shown)
    #  Rock beats scissors - Scissors beats paper - Paper beats rock
    #example rps('rock','paper') returns 'u2'
    
    if u1 == u2:
        return "It's a tie"
    elif u1 == "rock":
        if u2 == "scissors":
            return "u1"
        elif u2 == "paper":
            return "u2"
    elif u1 == "paper":
        if u2 == "rock":
            return "u1"
        elif u2 == "scissors":
            return "u2"
    elif u1 == "scissors":
        if u2 == "paper":
            return "u1"
        elif u2 == "rock":
            return "u2"


def bmi(weight, height):  #computes a fitness category based on the body mass index (bmi). bmi = weight (lbs.) / height**2 (inches) * 703
    # return the BMI number and class in () on the return line: 
    #   > 30 "obese", 
    #   25-30 "overweight", 
    #   18.5 - 25 "healthy weight", 
    #   16 - 18.5 "underweight", 
    #   < 16 "severely underweight"
    # example bmi(230,73) returns (30.34152749108651, 'obese'), boundary values go in the lower (for example 25 returns 'healthy weight')
    
    bmi = (weight/(height**2.0)) * 703.0
    
    if bmi > 30:
        return (bmi, "obese")
    elif bmi > 25 and bmi <= 30:
        return (bmi, "overweight")
    elif bmi > 18.5 and bmi <= 25:
        return (bmi, "healthy weight")
    elif bmi > 16 and bmi <= 18.5:
        return (bmi, "underweight")
    elif bmi <= 16:
        return (bmi, "severely underweight")

    
def factodd(n):   # compute the factorial of only odd numbers <= (n), if start value is even, start at n-1.
    #return the factorial value
    #example factodd(7) returns 105 (that is 7*5*3), factodd(6) returns 15 (that is 5*3)
  
    
   if n % 2 != 0:
       nextnum = n-2
       result = n
       while nextnum > 1 and n > 1:
           result *= nextnum
           n = n-2
           nextnum = n-2
   else:
        n = n-1
        nextnum = n-2
        result = n
        while nextnum > 1 and n > 1:
            result *= nextnum
            n = n-2
            nextnum = n-2

   return result