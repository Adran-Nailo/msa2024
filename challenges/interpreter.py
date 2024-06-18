def main():
    while True:
        expression= input("Expression: ")
        number_list = expression.split(" ")
        if len(number_list) == 3:
            break
        elif len(number_list) != 3:
            print("ERROR: please enter an expression with the correct formating")
            continue
        try:
            x = int(number_list[0])
            z = int(number_list[2])
            y = number_list[1]
        except:
            print("ERROR: please enter an expression with the correct formating")
            continue
        if y == "+":
            output = x + z
            print(f"{x} + {z} = {output}")