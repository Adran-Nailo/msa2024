#create a program that accepts a highway number and outputs the direction
#User enters: 95
#output: Interstate 95 runs North to South
def get_hwy_number():
    while(True):
        try:
            hwy_number = int(input("\nEnter the number of the Interstate: "))
            if hwy_number <= 0:
                print("\nERROR: please provide a number greater than 0")
                continue
            break
        except:
            print("\nERROR: please enter the number of the Interstate")
    return hwy_number

def calculate_hwy_number(hwy):
    hwy_even_or_odd = hwy % 2
    if hwy_even_or_odd == 1:
        is_hwy_even = False
    else:
        is_hwy_even = True
    return is_hwy_even

def main():
    hwy_number = get_hwy_number()
    is_even = calculate_hwy_number(hwy_number)
    if is_even == True:
        print(f"\nInterstate {hwy_number} runs from West to East\n")
    else:
        print(f"\nInterstate {hwy_number} runs from North to South\n")

main()