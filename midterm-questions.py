# Should define a function for dealing with the calculations that will take the values of the variables in the main function as arguments; calculations function can be inserted into main function
# how can i calculate the number of coins purchased? (1 BTC/$price per BTC)*value purchased
# how can i calculate the value of coins owned? (coins owned*current value)
# inputs assigned to variables should be variables local to the main function:

def bitcoins_purchased(bitcoin_price: float, dollar_value_purchased: float)-> float:
    number_of_bitcoins = ((1/bitcoin_price) *  dollar_value_purchased)
    return number_of_bitcoins 

def value_of_bitcoins_owned(bitcoins_owned: float, bitcoin_price: float)-> float:
    value_owned = (bitcoins_owned * bitcoin_price)
    return value_owned

def change_in_value(current_value: float, purchase_price: float)-> float:
# How do I calculate the change in value? Current value - purchase price 
    price_difference = current_value - purchase_price
    return price_difference

def percent_change_in_value(current_value: float, purchase_price: float)-> float:
# How do I calculate %change? 1-(current_value /purchase_price)?
    if current_value > purchase_price:
        percent_change = 1-(current_value/purchase_price)
        return percent_change
    if current_value < purchase_price:
        percent_change = -(1-(current_value/purchase_price))
        return percent_change

def main()-> None:
    # user input:
    bitcoin_price_at_purchase = float(input('Enter BTC purchase price: $'))
    bitcoin_dollar_value_purchased = float(input('Enter money to spend: $'))
    bitcoin_price_current = float(input("Enter new BTC price: $"))

    # bitcoins owned calculation:
    bitcoins_owned = bitcoins_purchased(bitcoin_price_at_purchase, bitcoin_dollar_value_purchased)

    # OUTPUT: bitcoins purchase 
    print(f'You spent ${bitcoin_price_at_purchase : ,.2f} CAD to purchase {bitcoins_owned : .6f} BTC.')

    # bitcoins current value calculation:
    current_value = value_of_bitcoins_owned(bitcoins_owned, bitcoin_price_current) 

    # bitcoins absolute change calculation:
    absolute_value_change = change_in_value(current_value, bitcoin_dollar_value_purchased)

    # bitcoins percent change calculation:
    percent_change = percent_change_in_value(current_value, bitcoin_dollar_value_purchased)

    # OUTPUT: bitcoins owned current value and percent change 
    print(f'Now your BTC are worth ${current_value : ,.2f} CAD. \n A change of ${absolute_value_change : ,.2f} or a percentage change of {percent_change : .2%}.')

main()
