def prime_test(num,testing_num):
    for test_num in range(2,testing_num):
        test_prime = num % test_num
        is_prime = True
        if test_num == num:
            continue
        if test_prime != 0:
            is_prime = True
            continue
        else:
            is_prime = False
            break
    if is_prime == True:
        return num

def get_user_input():
    while(True):
        try:
            user_input = int(input("Enter the upper limit of the numbers you want to check for primes: "))
            if user_input < 2:
                print("ERROR: number must be higher than 1")
            break
        except:
            print("ERROR:enter a whole number")
            continue
    return user_input

def main(user_input):
    print("\n")
    user_input = get_user_input()
    for tested_number in range(1,user_input):
        number=prime_test(tested_number,user_input)
        try:
            int(number)
            print(number)
        except:
            continue
        
main()
print("\n")