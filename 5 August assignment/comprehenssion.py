def square_of_list(input_list):
    output_list = [x*x for x in input_list]
    return output_list   

input_list = []
length = int(input("How much element do you want in list: "))

for i in range(0,length):
    element = int(input("Enter element: "))
    input_list.append(element)
    
print("Squared List ",square_of_list(input_list)) 