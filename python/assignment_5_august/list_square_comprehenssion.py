"""
squaring element of list using comprehenssion
"""
def square_of_list(input_list):
    """
    function takes element from the list square it and append it to output_list
    """
    output_list = [x*x for x in input_list]
    return output_list

user_list = []
length = int(input("How much element do you want in list: "))

for i in range(0,length):
    element = int(input("Enter element: "))
    user_list.append(element)
print("Squared List ",square_of_list(user_list))
