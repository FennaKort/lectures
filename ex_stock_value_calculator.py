present_value = float(input('Enter the present value of the stock: $'))
growth_rate = (float(input('Enter the expected growth rate without the percentage sign: ')))/100
time = float(input('Enter the number of years you expect to let the stock grow: '))

def future_value(present_value: float, growth_rate: float, time: float)-> float:
    "Calculate the future value of a stock based on user input"
    future_value = present_value * ((1 + growth_rate) ** time)
    return future_value
print(f'The expected future value of your stock is: ${future_value(present_value, growth_rate, time) : ,.2f}')