"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here

    # Your code goes here
   
    for inputs in items:
        frequencies[str(inputs)] = frequencies.get(str(inputs), 0) + 1
   
    return frequencies
     
   # for key, value in frequencies.items():
     #   print ("% d : % d"%(key, value))
   


   


    return frequencies
