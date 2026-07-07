#!/usr/bin/env python3

'''''
Title: Pizza Order Cost Calculator

Author: Andrea Freeman

A Python script that calculates the total cost of a pizza order based on the following factors:
    - pizza size
    - amount of toppings
    - delivery distance
'''''

# Constant variables
SMALL_PIZZA = 8
LARGE_PIZZA = 12
TOPPING_FEE = 1 

# Delivery_fee is $2 for first 5 miles and $1 for every additional mile
five_mile_fee = 2
additional_mile_fee = 1

# Calculate the delivery fee based on miles inputted | outputs: delivery fee
def calculate_delivery_fee(delivery_distance):
    if(delivery_distance > 5):
        remaining_mile = delivery_distance - 5
        delivery_fee = (remaining_mile * additional_mile_fee) + (5 * five_mile_fee)
        return delivery_fee
    else:
        delivery_fee = delivery_distance * additional_mile_fee
        return delivery_fee

# Gathers pizza size, topping amount, and delivery distance from the user | outputs: pizza_charge, topping_charge, delivery_fee
def gather_order_details():
    while True:
        pizza_size_input = input("Please choose a pizza size: small, large: ")
        pizza_size = pizza_size_input.lower().strip()
        if pizza_size == "small":
            pizza_charge = SMALL_PIZZA
            print(pizza_charge)
            break
        elif pizza_size == "large":
            pizza_charge = LARGE_PIZZA
            print(pizza_charge)
            break 
        else:
            print("Invalid Input: Please enter 'large' or 'small' : ")
    while True:
        number_of_toppings_input = input("How many toppings would you like to add? : ")
        try:
            number_of_toppings = int(number_of_toppings_input)
            if number_of_toppings > 0:
                topping_charge = number_of_toppings * TOPPING_FEE
                print(topping_charge)
                break
            else:
                print("Please input a number greater than 0 ")
        except ValueError:
            print("Invalid Input. Please enter a number. ")
    while True:
        delivery_distance_input = input("Please enter the distance to your address in miles : ")
        try:
            distance_input = int(delivery_distance_input)
            if distance_input > 0:
                delivery_fee = calculate_delivery_fee(distance_input)
                print(delivery_fee)
                break
            else:
                print("Please enter a distance in miles as a whole number that is greater than 0.")
        except ValueError:
            print("Invalid Input : Please try again. ")
    print(pizza_charge, topping_charge, delivery_fee)
    return pizza_charge, topping_charge, delivery_fee

# Calculate the cost of toppings | outputs: formatted string 
def calculate_cost(pizza_charge, topping_charge, delivery_charge):
    order_sum = pizza_charge + topping_charge + delivery_charge
    print(f'Summary:')
    print(f'Pizza size fee: + {pizza_charge}')
    print(f'Topping fee: + {topping_charge}')
    print(f'Delivery fee: + {delivery_charge}')
    print(f'___________________________________')
    print(f'Thank you for your order! Your total is ${order_sum:.2f}')
    


# Program begins here :           
pizza_charge, topping_charge, delivery_charge = gather_order_details() 
calculate_cost(pizza_charge, topping_charge, delivery_charge)    

