# goal: write a to-do list program
# things program needs to be able to do:
    # read new_list_item
    # display list items
    # create an indefinite number of new list items
    # ask if I've completed any items; accept input relating to a specific item
# things I need to learn:
    # can I automatically create a new variable within a function or loop? how to do this?
        # is this what arrays could be used for? 
    # how to select from a list of options and have something new be done to them
    # lists + .append string methods etc may be a good way to do this? 
    # can I pass in input strings as arguments for strings? maaybe by assigning input to  variiiiiable then pass variable in as aaaaaaaaaaaaaaarg
# inputs:
    # new list item
    # a way to set the list item to completed
# instructions:
    # ask if user would like to input new list item or display current list or clear list
    # if add new list item:
    #     accept input for new list item, store string 
    #     repeat step 1
    # if read current list: 
    #     print current list (or text "no items on list")
    #     ask if user would like to input new list item or mark an item as completed or clear list
    #         if mark_as_completed:
    #             accept user input for specific list item (how to do this?) 
    #             mark selected list item as complete
    #             repeat step 1
    # if clear list:
    #     prompt "are you sure"
    #     delete all stored values if yes
    # else: 
    #     display "not a valid command"
    #     repeat step 1
    # output list
# simpler version:
#   ask how many list items user would like to create between 1-10
#   display that many input prompts
#   print list        
# I have this idea that I could have a new_list_item function that creates a list item, a select_list_item function that selects the desired item, a delete_item function that selects then deletes, and a mark_completed function that selects and then marks completed

