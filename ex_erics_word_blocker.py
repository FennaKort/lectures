#---string methods exercise: 
# input: any string
# read string
# "eric" in lower("")

user_text = input("Write some text here: ")
# test print to ensure proper implementation of lower() string method:
user_text = user_text.casefold()
print(f"Is there a bad word here? {"eric" in user_text}")
if "eric" in user_text:
    # censored_input = (user_input.replace("eric","cats"))
    
    print(f"That word is not allowed! Your input will be altered to read \"{user_text.replace("eric".casefold(),"cats")}\"")
else:
    print(f"Your input \"{user_text}\" has been accepted!")