"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(my_list):
    frequencies = {}
    # Your code goes here
    for items in my_list:
        if(isinstance(items,str)):
         frequencies[items] = my_list.count(items)
        else:
         a= str(items)
         frequencies[a] = my_list.count(items)
        

     
   # for key, value in frequencies.items():
     #   print ("% d : % d"%(key, value))
   


   


    return frequencies
