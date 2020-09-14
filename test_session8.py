import pytest
import session8
import os
#import numpy as np
import inspect
import re

README_CONTENT_CHECK_FOR = [
     
]

CHECK_FOR_THINGS_NOT_ALLOWED = [
    
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r",encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 301, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r",encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r",encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 6


def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session8)
    spaces = re.findall('\n +.', lines)
    line_no =1
    for space in spaces:
        line_no +=1
        print('=====', line_no, space)
        #print(lines)
        #assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        #assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 
        assert re.search('[a-zA-Z#@=1234\'\"]', space), "Your code intentation does not follow PEP8 guidelines"
        assert len(re.sub(r'[a-zA-Z#@=1234\n\"\']', '', space)) % 4 == 0, \
        "Your code intentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session8, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

# def test_not_a_function_valueerror():
#     with pytest.raises(ValueError):
#        session8.outer_func()

# def test_not_number_valueerror():
#     with pytest.raises(ValueError):
#         session8.nextfibonacci('a')

# def test_not_function_valueerror():
#     with pytest.raises(ValueError):
#         session8.counter_add(4,5)

def test_func():
    '''
    This is a test function to test the test case number one
    '''
def test1_func():
    '''
    This
    '''
def test2_func():
    return True

# def test_not_number_valueerror():
#     with pytest.raises(ValueError):
#         session7.check_fibonocci('a')
def test_for_doc_value_fifty():
    fn= test_func
    out_fn= session8.outer_func(fn)
    assert bool(out_fn()), "Your function is not working properly"
def test_for_doc_value_not_fifty():
    fn= test1_func
    out_fn= session8.outer_func(fn)
    assert not bool(out_fn()), "Your function is not working properly"
def test_for_doc_value_no_val():
    fn= test2_func
    out_fn= session8.outer_func(fn)
    assert not bool(out_fn()), "Your function is not working properly"

def test_fib_series():
    next_val=session8.nextfibonacci(8)
    assert next_val() == 13, "Your function is not working properly"
    next_val=session8.nextfibonacci(13)
    assert next_val() == 21, "Your function is not working properly"
    next_val=session8.nextfibonacci(21)
    assert next_val() == 34, "Your function is not working properly"

def test_dict_add_val():
    assert session8.counter_add(4,5) == 9 , "Your Add function is not working properly" 
def test_dict_mul_val():
    assert session8.counter_mul(4,5) == 20 , "Your multiplication function is not working properly" 
def test_dict_div_val():
    assert session8.counter_div(40,5) == 8 , "Your division function is not working properly" 
def test_dict_all_val():
    session8.counter_add(4,5)
    session8.counter_mul(4,5)
    session8.counter_div(4,5)
    assert session8.dict_ops['add'] == 2 , "Your Add dictionary is not working properly" 
    assert session8.dict_ops['mul'] == 2 , "Your multiplication dictionary is not working properly" 
    assert session8.dict_ops['div'] == 2 , "Your division dictionary is not working properly" 

def test_dict_add_new_val():
    assert session8.counter_add_new(4,5) == 9 , "Your Add function is not working properly"
    assert session8.add_dict['add'] == 1 , "Your Add dictionary is not working properly" 
def test_dict_mul_new_val():
    assert session8.counter_mul_new(4,5) == 20 , "Your Add function is not working properly"
    assert session8.mul_dict['mul'] == 1 , "Your Multiply dictionary is not working properly" 
def test_dict_div_new_val():
    assert session8.counter_div_new(40,5) == 8 , "Your Add function is not working properly"
    assert session8.div_dict['div'] == 1 , "Your Division dictionary is not working properly" 
def test_dict_add_new_val_next():
    assert session8.counter_add_new(6,5) == 11 , "Your Add function is not working properly"
    assert session8.add_dict['add'] == 2 , "Your Add dictionary is not working properly"   
    assert session8.mul_dict['mul'] == 1 , "Your Multiply dictionary is not working properly"
    assert session8.div_dict['div'] == 1 , "Your Division dictionary is not working properly" 

def test_dict_mul_new_val_next():
    assert session8.counter_mul_new(6,11) == 66 , "Your Add function is not working properly"
    assert session8.add_dict['add'] == 2 , "Your Add dictionary is not working properly"   
    assert session8.mul_dict['mul'] == 2 , "Your Multiply dictionary is not working properly"
    assert session8.div_dict['div'] == 1 , "Your Division dictionary is not working properly" 

def test_dict_div_new_val_next():
    assert session8.counter_div_new(66,11) == 6 , "Your Add function is not working properly"
    assert session8.add_dict['add'] == 2 , "Your Add dictionary is not working properly"   
    assert session8.mul_dict['mul'] == 2 , "Your Multiply dictionary is not working properly"
    assert session8.div_dict['div'] == 2 , "Your Division dictionary is not working properly" 

def test_dict_add_new_val_next_n():
    assert session8.counter_add_new(6,5) == 11 , "Your Add function is not working properly"
    assert session8.add_dict['add'] == 3 , "Your Add dictionary is not working properly"   
    assert session8.mul_dict['mul'] == 2 , "Your Multiply dictionary is not working properly"
    assert session8.div_dict['div'] == 2 , "Your Division dictionary is not working properly" 

def test_dict_mul_new_val_next_n():
    assert session8.counter_mul_new(6,11) == 66 , "Your Add function is not working properly"
    assert session8.add_dict['add'] == 3 , "Your Add dictionary is not working properly"   
    assert session8.mul_dict['mul'] == 3 , "Your Multiply dictionary is not working properly"
    assert session8.div_dict['div'] == 2 , "Your Division dictionary is not working properly" 

def test_dict_div_new_val_next_n():
    assert session8.counter_div_new(66,11) == 6 , "Your Add function is not working properly"
    assert session8.add_dict['add'] == 3 , "Your Add dictionary is not working properly"   
    assert session8.mul_dict['mul'] == 3 , "Your Multiply dictionary is not working properly"
    assert session8.div_dict['div'] == 3 , "Your Division dictionary is not working properly" 

def test_things_not_allowed():
    code_lines = inspect.getsource(session8)
    for word in CHECK_FOR_THINGS_NOT_ALLOWED:
        assert word not in code_lines, 'Have you heard of Pinocchio?'
