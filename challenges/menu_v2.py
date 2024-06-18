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

def main():
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
main()