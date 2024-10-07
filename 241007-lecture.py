#___TASK: practice value returning functions by creating a program that evaluates multiple user inputs for occurrences of a disallowed word
# planning program:
# accept input
# count number of times "eric" appears - .count string method
# case-insensitive
# output: count for string argument
# use function in program that asks user to enter 3 text strings, prints total number of usages across all 3

def count_erics(user_text: str)-> int:
    "Evaluates content of variable user_text for number of occurrences of word 'eric'"
    erics_in_user_text = user_text.count("eric")
    return erics_in_user_text

total_number_of_erics = 0
counter = 0

while counter < 3:
    user_text = input("Write a sentence: ").casefold()
    erics_per_string = count_erics(user_text)
    total_number_of_erics = total_number_of_erics + erics_per_string
    counter = counter + 1

print(f'The total number of disallowed words is: {total_number_of_erics : n}')

