file = open('./241125-payments.txt', 'r')

sum = 0

for line in file:
    line_parts = line.split(' ') #str mthd splits on space; assigns parts to list
    dollar_amt_str = line_parts[0][1:] #all characters except first one from first list item
    dollar_amt_int = int(dollar_amt_str)
    sum += dollar_amt_int
file.close()
print(f"${sum}")

file = open('./241125-payments.txt', 'a')
file.write(f"${sum}")
file.close()

######################
