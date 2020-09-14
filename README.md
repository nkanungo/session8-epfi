# Assignment - 8
================
This Assignment is to demonstrate the capabilities of Scopes and Closures 

# Question -1 

Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 
50 is stored as a free variable

Solution 

def outer_func(fn)

    
    This function was created to demonstrate the Closure feature.
    
    The Outer Function : It takes a function as input and calculates the number of characters present in it's doc string 
    Check_func : It is the inner function which takes the function passed to the outer function 
    and  take the non local variable which tells what is the length of doc string be 
    Returns : True if the doc string contains more than 50 characters 
              False if either the doc string is not present or less than 50 characters

# Question -2 

Write a closure that gives you the next Fibonacci number

Solution 

def nextfibonacci(n)
   
    This function is created to demonstrate the Closure feature.
    The Outer function takes the number as input 
    The inner function takes this variable and calculates the next value in the fibonacci 
    Returns the Next number in series 
    

# Question -3 

We wrote a closure that counts how many times a function was called. Write a new one that can keep a track of how many times add/mul/div 
functions were called, and update a global dictionary variable with the counts

Solution 

def counter(fn)
 
    The Inner function takes the count of each function being called. 
    Here we are using a global dictionary which can keep a track of how many times add/mul/div functions 
    were called, and update with the counts
    Takes function as input and returns the dictionary
  
# Question -4 

Modify above such that now we can pass in different dictionary variables to update different dictionaries

Solution 

def counter_new(fn,dict_ops)
   
    The Inner function takes the count of each function being called. 
    Here we are using separate dictionary which can keep a track of how many times add/mul/div functions 
    were called, and update with the counts
    Takes function and the respective dictionary  as input and returns the dictionary
    
            
#

