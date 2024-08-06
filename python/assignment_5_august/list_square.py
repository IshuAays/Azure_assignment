"""
making a function to get square a list
"""


def square_of_list(input_list):
    """ 
    function takes list and and return squared list
    """
    output_list = []
    for element in input_list:
        squared_element = element * element
        output_list.append(squared_element)
    return output_list


if __name__ == "__main__":
    user_list = []
    length_of_list = int(input("How much element do you want in list: "))

    for i in range(0,length_of_list):
        number = int(input("Enter element: "))
        user_list.append(number)
    print("Squared List ",square_of_list(user_list))
