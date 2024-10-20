# slide19
def a() -> bool:
    print('getting a')
    return True

def b() -> bool:
    print('getting b')
    return False

def c() -> bool:
    print('getting c')
    return True

print(
'a or (b and c) = ', a() or (b() and c()) # print string typing out boolean equation; then calls functions that are used in boolean equation and prints the return value for the finished boolean equation
)
print(
'b and (c or a) = ', b() and (c() or a())
)
