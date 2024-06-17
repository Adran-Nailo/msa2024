def change_calculator(money):
    hundreds = round(money // 100)
    print(f"hundreds: {hundreds}")
    remainder = round(money % 100, 2)
    fifties = round(remainder // 50)
    print(f"fifties: {fifties}")
    remainder = round(remainder % 50, 2)
    tens = round(remainder // 10)
    print(f"tens: {tens}")
    remainder = round(remainder % 10, 2)
    fives = round(remainder // 5)
    print(f"fives: {fives}")
    remainder = round(remainder % 5, 2)
    ones = round(remainder // 1)
    print(f"ones: {ones}")
    remainder = round(remainder % 1, 2)
    quarters = round(remainder // 0.25)
    print(f"quarters: {quarters}")
    remainder = round(remainder % 0.25, 2)
    dimes = round(remainder // 0.1)
    print(f"dimes: {dimes}")
    remainder = round(remainder % 0.1, 2)
    nickles = round(remainder // 0.05)
    print(f"nickles: {nickles}")
    remainder = round(remainder % 0.05, 2)
    pennies = round(remainder // 0.01)
    print(f"pennies: {pennies}")

def get_user_input():
    while(True):
        try:
            number = float(input("Enter Your Change:\n"))
            if number < 1:
                print("ERROR: enter a value greater than 0")
                continue
            break
        except:
            print("ERROR: please enter a number")
            continue
    return number

def main():
    change = get_user_input()
    change_calculator(change)

main()