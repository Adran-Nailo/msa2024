#Function to load menu items from the file and create a dictionary
#Input: none
#output: dictionary of menu items
def get_menu_items():
    #create a file handle that gives access to to the file 
    data_file = open("menu.txt", "+r")
    #create an empty dictionary to store the menu items and prices
    menu_items = {}

    #loop through data in the file and read the file one line at a time
    for line_of_data in data_file:
        
        #split the line of data at the comma using .split
        keys_and_values = line_of_data.split(",")

        #get item and price from the resulting list and store in the dictionary 
        item = keys_and_values[0]
        price = float(keys_and_values[1])
        menu_items[item] = price

    #close the file
    data_file.close()
    return menu_items

def get_cost():
    get_menu_items()
    

    #create dictionary
    menu_options = get_menu_items()
    print("\n\n")
    for key, value in menu_options.items():
        print(f"{key}: ${value: .2f}")
    user_input = ""
    total = 0
    #end the program when the user says "END"
    while user_input != "END":
        #prompt user for input
        user_input = input("\nItem:\n")
        user_input = user_input.upper()
        if user_input == "END":
            print(f"AMOUNT DUE:\n${total: .2f}", sep="")
            continue
        #ignore invalid input
        elif not user_input in menu_options:
            print("ERROR: pleasee enter a menu item")
            continue
        cost = round(menu_options[user_input],2)
        #add the value of the item to the current total
        total += cost
        #print the new total
        print(f"Total: ${total: .2f}")
    return total

def get_coin(amount_due):
    #prompt user for coin, and check with a list (1,5,,10,20 50)
    while(True):
        valid_coins = [1,5,10,25]
        try:
            print(f"Amount Due: {amount_due}")
            user_input = int(input("Insert Bill:\n"))
            print("-----------------")
            if user_input in valid_coins:
                
                break
            continue
        except:
            print("-----------------")
            continue
    return user_input

def main():
    #Display amount due with a print statement
    amount_due = get_cost()
    print(amount_due)
    while amount_due > 0:
        coin_value = get_coin(amount_due)
        amount_due = amount_due - coin_value
    change_owed = amount_due * -1
    print (f"Change Owed: {change_owed}")
main() 