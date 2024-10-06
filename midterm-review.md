what is the data type for text?
    a string
    str()
what is the data type for whole numbers?
    an integer
    int()
what is the date type for decimal numbers?
    a float
    float()
what is a function?
    a grouping of instructions assigned to one name
what is string concatenation?
    attaching a string on the end of another string
what can be concatenated? 
    only strings and variables that currently have the data type string can be concatenated, because it uses the + operant; you cannot do addition with a number and a string or concatenate a string and a number. numbers must be cast to strings in order to concatenate them
what are escape characters?
    escape characters provide special formatting to strings by beginning with a backslash. 
    \n = includes a new line inside the string
    \t = include the tabbed space inside the string
    \' = includes a single quote inside the string
    \" = includes a double quote inside the string
    \\ = includes a backslash inside the string
what are f-strings?
    - formatted string literals
    - start an f string by putting the letter f in front of a string
    - f strings let you format a string's contents easily and insert a variable's value into a string, even if the variable is not a string
        name = "Fenna"
        print(f"Hi {name} :3") 
        # rather than print("Hi " + name + " :3")
what are format specifiers?
    format specifiers are a special codes that let you format a f strings place holder values in certain ways
    {placeholder : format-specifier}
    {placeholder : [alignment][minimum field width][,][.precision][type]}
    alignment: what side of the field to output on; <>+^ 
    width: string length to output when printing; integer
    .precision: how many decimal digits to display; .float
    type: how the date should be presented. 
        integer types:
            b: binary, outputs in base 2
            c: character, converts integer into unicode character before printing
            d: decimal integer, outputs in base 10
            o: octal format, outputs in base 8
            x: hex format, outputs in base 16
            X: hex format with numbers above 9 in uppercase letters, outputs in base 16
            n: number format, outputs a decimal integer with local formatting for character separators
        float types:
            e: exponent notation, prints number in scientific notation
            f: fixed point, prints as a fixed-point number
            g: general format, prints a number as a fixed-point number if it is small enough, otherwise, it will print in scientific notation
            %: percentage
what are built in functions?
    built in functions come with python and let you execute certain types of actions such as printing an output without having to define the function yourself each time
what are methods?
    methods are functions that belong to a specific object and work on that object only
    string methods are functions that belong to and operate on particular strings that they are assigned to
        "<string>".<method_name>
        upper() = converts a string to uppercase
        lower() = converts a string to lower case
        strip() = removes white space from the string
        replace(<old>,<new>) = within the string replace all occurrences of the string old with the string new
    string methods return a new string leaving the original string unaffected
what is the index?
    the index is the numerical position within a string. the index begins at 0 rather than at one. for example, the fourth character in a string is located at the index position 3
    len() function returns length of a string
    == checks if two things are equal
    <in> checks if one thing is contained in the other