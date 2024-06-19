import random

def main():
    
    #print a random number between 1 and 10
    print("random number 1-10:")
    random_value = random.randint(1,10)
    print(f"Random Value: {random_value}")

    #Generate 10 random numbers between 1 and 10
    random_list = []
    for number in range(1, 11):
        random_list.append(random.randint(1,100))

    #choose a random value from a list of values
    rand_list = [4,7,10,23,44,18,9,12]
    random_index = random.randint(0,len(rand_list)-1)
    print("\nchoose random value form list\n----------------")
    print(f"random index: {random_index}")
    print(f"random list value: {rand_list[random_index]}")

    # ask a user for the start and stop values to generate a random number between
    # ask the user how many random numbers to generate and generate that many
    print("\nUser generated random numbers\n------------------------------")
    while True:
        try:
            start_value = int(input("please enter the first number: "))
            end_value = int(input("please enter the last number: "))
            repitions = int(input("number of random numbers: "))
            int_list = []
            summation = 0
            for repeats in range(repitions):
                rand_int = random.randint(start_value, end_value)
                print(f"Value {repeats+1}: {rand_int}")
                int_list.append(rand_int)
            for number in range(len(int_list)-1):
                summation = summation + int_list[number]
            average = summation / len(int_list)
            print(f"Average of random numbers: {average}")
            break
        except:
            print("ERROR: enter a valid number")
            continue

        
main()