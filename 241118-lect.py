def my_ver()->None:
    entry = input('enter some text, press enter to quit: ')
    entries = []
    while entry != '':
        # process the input by adding it to a list
        # only keep last 3 entries
        # entries.append(entry) - if i do just lns 8-10, it deletes and only stores two list items. 
        if len(entries) >= 3:
            del entries[0]
            entries.append(entry)
        else:
            entries.append(entry)
        print(entries)
        entry = input('enter some text, enter to quit: ')

def erics_ver()-> None:
    entry = input('enter some text, press enter to quit: ')
    entries = []
    while entry != '':
        entries.append(entry)
        if len(entries) > 3:
            del entries[0]

        print(entries)
        entry = input('enter some text, enter to quit: ')

erics_ver()
