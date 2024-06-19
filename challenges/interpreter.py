def main():
    while True:
        expression= input("\nExpression: ")
        number_list = expression.split(" ")
        if len(number_list) != 3:
            print("ERROR: please enter an expression with the correct formating")
            continue
        try:
            x = int(number_list[0])
            z = int(number_list[2])
            y = number_list[1]
        except:
            print("ERROR: please enter an expression that uses integers")
            continue
        if y == "+":
            output = x + z
            print(f"{x} + {z} = {output: .1f}")
        elif y == "-":
            output = x - z
            print(f"{x} - {z} = {output: .1f}")
        elif y == "*":
            output = x * z
            print(f"{x} * {z} = {output: .1f}")
        elif y == "/":
            if z == 0:
                print("ERROR: can not divide by zero")
                continue
            output = x / z
            print(f"{x} / {z} = {output: .1f}")
        else:
            print("ERROR: please enter a valid operator")
            continue
        run_program_again = input("Do you want to do another calculation? Press y to continue or any other key to exit: ")
        if run_program_again.upper() == "Y":
            continue
        else:
            print("\n")
            break
main()