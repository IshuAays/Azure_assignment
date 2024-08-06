"""
module provides a function to get square of all the elements present in a list and then return a list
"""


def square_of_list(input_list):
    """ 
    This function takes a list as input and does square of the elements present in the list using a for loop 
    and append all the results in a new list and returns it. 
    """
    
    output_list = []
    for i in input_list:
        output_list.append(i*i)
    return output_list


  