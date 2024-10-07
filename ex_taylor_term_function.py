from math import factorial
def taylor_term (x: int, y: int)-> float:
    term = (x**y)/(factorial(y))
    return term
x = 2
estimate = taylor_term(x, 0)+taylor_term(x, 1)+taylor_term(x, 2)+taylor_term(x, 3)
print(estimate)