# Exercise: Chaining logical operations
# Given bools a, b, c, and d, write python expressions for the following:
# everything (all variables are True)
# anything (at least one variable is True)
# nothing (all variables are false)
def everything(a: bool, b: bool, c: bool, d: bool) -> bool:
    if a and b and c and d:
        return True
    else:
        return False

def anything(a: bool, b: bool, c: bool, d: bool) -> bool:
    if a or b or c or d:
        return True
    else:
        return False
        
def nothing(a: bool, b: bool, c: bool, d: bool) -> bool:
    if not a and not b and not c and not d:
        return True
    else:
        return False

def input_to_bool(val: str) -> bool:
    val = val.lower()
    if val in ('yes', 'y', 'true', 't', 'on', 'checked', '1'):
        return True
    elif val in ('no', 'n', 'false', 'f', 'off', 'unchecked', '0'):
        return False
    else:
        return print(ValueError(f"{val} is an Invalid Input"))

# my intention is to create a function that accepts user input and uses the input to bool function to convert the input string to a boolean data type. i want to be able to make sure that the input prompt will be repeated until a valid True or False result is input
def input_true_or_false():
    user_input = input('Select True or False: ')
    bool_user_input = input_to_bool(user_input)
    while (bool_user_input != True) and (bool_user_input != False):
        user_input = input('Try again! Select True or False: ')
        bool_user_input = input_to_bool(user_input)
    return bool_user_input
        # I figured out that I was missing the return statement OUTSIDE of the while loop!
    # when I do the following, I get stuck in an endless loop until I input "true". why is that?
    # while value != (True or False): # same thing happens with "is not (True or False)"
    #     value = input('select True or False: ')
    #     value = input_to_bool(value)
    #  
    # i thought i had fixed the problem with by using an and statement as per below,but this repeated the error where the function will only continue when a True value  is input
    # while value != True and value != False:
    #     value = input('select True or False: ')
    #     value = input_to_bool(value)
    #
    # ok the following managed to get me out of the endless loop of not accepting False as an input, but it doesnot address the goal of having the loop continue until there is a correct boolean value
    # if bool_user_input is True or bool_user_input is False:
    #     return bool_user_input
    # else:
    #     user_input = input('Try again! Select True or False: ')
    #     bool_user_input = input_to_bool(user_input)

def main():
    a = input_true_or_false()
    print("a is", a)
    b = input_true_or_false()
    print("b is", b)
    c = input_true_or_false()
    print("c is", c)
    d = input_true_or_false()
    print("d is", d)
    
    print("All variables are True:", everything(a, b, c, d))
    print("Some variables are True:", anything(a, b, c, d))
    print("All variables are False:", nothing(a, b, c, d))

main()
