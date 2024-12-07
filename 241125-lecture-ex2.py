file_in = open('./241125-payments.txt', 'r')
file_out = open('./241125-payments-final.txt', 'a')

for line in file_in:
    line_parts = line.split(' ')
    print(line_parts)
    # if line_parts[-1] != 'N.Korea': # this didn't work because line_parts[-1] can ALSO contain \n, so using != is too precise and doesn't catch it
    if 'N.Korea' not in line_parts[-1]:
        print(line)
        file_out.write(line)
file_out.write('\n \n')

file_in.close()
file_out.close()




