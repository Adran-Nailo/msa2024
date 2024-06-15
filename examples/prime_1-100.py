def prime_test(num):
    for test_num in range(2,101):
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

def main():
    print("\n")
    for tested_number in range(1,101):
        number=prime_test(tested_number)
        try:
            int(number)
            print(number)
        except:
            continue
        
main()
print("\n")