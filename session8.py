from math import *
# # Question-1
def outer_func(fn):

    '''
    This function was created to demonstrate the Closure feature.
    The Outer Function
    ====================
    It takes a function as input and calculates the number of characters present in it's doc string 
    Check_func
    ============
    It is the inner function which takes the function passed to the outer function 
    and  
    take the non local variable which tells what is the length of doc string be 
    Returns : True if the doc string contains more than 50 characters 
            False if either the doc string is not present or less than 50 characters
    '''
    len_doc_string=50
    def check_func():
        if not hasattr(fn,'__call__'):
            raise ValueError('Please pass a valid function object ')
        if bool(fn.__doc__) and len(fn.__doc__) >= len_doc_string:
            return True
            #print('Doc string has more than 50 characters')
        else:
            return False
            #raise ValueError('Doc String value is less than 50')
    return check_func

# # Question-2

def nextfibonacci(n): 
    '''
    This function is created to demonstrate the Closure feature.
    The Outer function takes the number as input 
    The inner function takes this variable and calculates the next value in the fibonacci 
    Returns the Next number in series 
    '''
    def generate_fib():
        if not isinstance(n,int):
            raise ValueError('Please pass a integer value to find nth fibonnacci number')
        return round(n*(1 + sqrt(5))/2.0)
        #return round(a) 
    return generate_fib

# # Question-3

dict_ops=dict()

def counter(fn):
    '''
    The Inner function takes the count of each function being called. 
    Here we are using a global dictionary which can keep a track of how many times add/mul/div functions 
    were called, and update with the counts
    Takes function as input and returns the dictionary
    '''
    global dict_ops
    cnt = 0
    def inner(*args, **kwargs):
        if not hasattr(fn,'__call__'):
            raise ValueError('Please pass a valid function object ')
        nonlocal cnt
        print(dict_ops,fn.__name__)
        if str(fn.__name__) in dict_ops :
            dict_ops[str(fn.__name__)] +=1
        else:
            dict_ops[str(fn.__name__)] =1

        cnt += 1
        print('{0} has been called {1} times'.format(fn.__name__, cnt))
        return fn(*args, **kwargs)
    return inner

def add(a, b):
    return a + b
def mul(a, b):
    return a*b
def div(a,b):
    return a/b

counter_add = counter(add)
counter_mul = counter(mul)
counter_div = counter(div)

# # Question-4
add_dict=dict()
mul_dict=dict()
div_dict=dict()

def counter_new(fn,dict_ops):
    '''
    The Inner function takes the count of each function being called. 
    Here we are using separate dictionary which can keep a track of how many times add/mul/div functions 
    were called, and update with the counts
    Takes function and the respective dictionary  as input and returns the dictionary
    '''
    if not isinstance(dict_ops,dict):
        raise ValueError("need to pass a dictionary per user")
    #global dict_ops
    cnt = 0
    def inner_new(*args, **kwargs):
        if not hasattr(fn,'__call__'):
            raise ValueError('Please pass a valid function object ')
        nonlocal cnt
        print(dict_ops,fn.__name__)
        if str(fn.__name__) in dict_ops :
            dict_ops[str(fn.__name__)] +=1
        else:
            dict_ops[str(fn.__name__)] =1

        cnt += 1
        print('{0} has been called {1} times'.format(fn.__name__, cnt))
        return fn(*args, **kwargs)
    return inner_new
counter_add_new = counter_new(add,add_dict)
counter_mul_new = counter_new(mul,mul_dict)
counter_div_new = counter_new(div,div_dict)