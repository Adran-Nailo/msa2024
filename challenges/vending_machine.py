

#subtract the coin from the total
#display current total
#if the user puts in more coins than required, return the amount of change

def get_coin(amount_due):
    #prompt user for coin, and check with a list (1,5,,10,25)
    while(True):
        valid_coins = [1,5,10,25]
        try:
            print(f"Amount Due: {amount_due}")
            user_input = int(input("Insert Coin:\n"))
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
    print("\nVending Machine\n-----------------")
    amount_due = 50
    while amount_due > 0:
        coin_value = get_coin(amount_due)
        amount_due = amount_due - coin_value
    change_owed = amount_due * -1
    print (f"Change Owed: {change_owed}")
main()
