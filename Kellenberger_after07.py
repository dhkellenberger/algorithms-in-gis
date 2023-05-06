# In after 07, your will create dictionaries from list data on state demographics, using single values, from a list of lists of values 
# and from dictionary values. 
#  
# The samples are shown and I will test your functions with different sample data using the same keys, but different values.  
# For the last two I will use a different file that is similar with three data values.


#test on these sample input data: li = [['Virginia', 800000],['North Carolina', 9000000],['South Carolina', 5000000]]

def makedicts(li):  #function to make a dictionary of keys tied to single values from a list of lists
    #return the dictionary
    #example result is {'Virginia': 800000, 'North Carolina': 9000000, 'South Carolina': 5000000}
    
    d = {}
    
    for i in li:
        d.update({i[0]: i[1]})
    
    return d


#test on these sample input data: li = [['Virginia', 800000, 51, 6.1],['North Carolina', 9000000, 50.24,5.2],['South Carolina', 5000000, 52.1,3.3]]

def makedictl(li): #function to make a dictionary of keys tied to lists of values from a list of lists
    #return the dictionary
    #example result is: {'Virginia': [800000, 51, 6.1], 'North Carolina': [9000000, 50.24, 5.2], 'South Carolina': [5000000, 52.1, 3.3]}
    
    d = {}
    
    for i in li:
        d.update({i[0]: i[1:]})
    
    return d


#test on these sample input data: li = [['Virginia', 800000, 51, 6.1],['North Carolina', 9000000, 50.24,5.2],['South Carolina', 5000000, 52.1,3.3]]
#value keys in the lists are 'population', 'percent female', and 'percent over 80'

def makedictd(li): #function to make a dictionary of keys tied to dictionaries of data
    #return the dictionary
    #example result is: {'Virginia': {'population': 800000, 'percent female': 51, 'percent over 80': 6.1}, 'North Carolina': {'population': 9000000, 'percent female': 50.24, 'percent over 80': 5.2}, 'South Carolina': {'population': 5000000, 'percent female': 52.1, 'percent over 80': 3.3}}
    
    d = {}
    
    for i in li:
        d.update({i[0]: {'population': i[1], 'percent female': i[2], 'percent over 80': i[3]}})
    
    return d