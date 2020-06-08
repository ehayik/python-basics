
# More about iteration

"""
Write a function, sublist, that takes in a list of numbers as the parameter. 
In the function, use a while loop to return a sublist of the input list. 
The sublist should contain the same values of the original list up until 
it reaches the number 5 (it should not contain the number 5).
"""
def sublist(numbers):
    index = 0
    sb_list = []

    while index < len(numbers) and numbers[index] != 5:
        sb_list.append(numbers[index])
        index += 1

    return sb_list


"""
Write a function called beginning that takes a list as input and contains a while loop that only stops once the element of the list is the string ‘bye’. 
What is returned is a list that contains up to the first 10 strings, regardless of where the loop stops. (i.e., if it stops on the 32nd element, 
the first 10 are returned. If “bye” is the 5th element, the first 4 are returned.) If you want to make this even more of a challenge, do this without slicing
"""
def beginning(lst):
    index = 0
    sb_lst = []

    while index < len(lst) and index < 10 and lst[index] != "bye":
        sb_lst.append(lst[index])
        index += 1

    return sb_lst

# Advanced Functions 

"""
Create a function called mult that has two parameters, the first is required and should be an integer, 
the second is an optional parameter that can either be a number or a string but whose default is 6. 
The function should return the first parameter multiplied by the second.
"""
def mult(integer, opt = 6):
    return integer * opt


"""
Write a function, test, that takes in three parameters: a required integer, 
an optional boolean whose default value is True, and an optional dictionary, 
called dict1, whose default value is {2:3, 4:5, 6:8}. If the boolean parameter 
is True, the function should test to see if the integer is a key in the dictionary. 
The value of that key should then be returned. If the boolean parameter is False, return the boolean value “False”.
"""
def test(num, flag = True, dict1 = {2:3, 4:5, 6:8}):

    if flag:
        return dict1.get(num, None)
    else:
        return False
