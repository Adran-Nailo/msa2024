#create dictionary
#prompt user for input
    #ignore invalid input
    #print valid input
#pass the value to the total_calculator
    #add the value of the item to the current total
    #return the new total to main()
#print the new total
#ask the user for another input
#end the program when the user says "END"

def main():
    menu_options = {
            "BAJA TACO": 4.00,
            "BURRITO": 7.50,
            "BOWL": 8.50,
            "NACHOS": 11.00,
            "QUESADILLA": 8.50,
            "SUPER BURRITO": 8.50,
            "SUPER QUESADILLA": 9.50,
            "TACO": 3.00,
            "TORTILLA SALAD": 8.00
        }
    print("\n\n")
    for key, value in menu_options.items():
        print(f"{key}: ${value: .2f}")
    user_input = ""
    total = 0
    while user_input != "END":
        user_input = input("\nItem:\n")
        user_input = user_input.upper()
        if user_input == "END":
            print(f"AMOUNT DUE:\n${total: .2f}", sep="")
            continue
        elif not user_input in menu_options:
            print("ERROR: pleasee enter a menu item")
            continue
        
        cost = round(menu_options[user_input],2)
        total += cost
        print(f"Total: ${total: .2f}")
main()