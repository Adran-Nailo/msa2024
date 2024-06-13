
def main():
    #print integers between 0 and 10:
    for number in range(11):
        print (number)

    #print integers between 5 and 10::
    print("\n\n")
    for number in range(5,11):
        print(number)

    print("\n\n")
    #print even numbers between 0 and 10
    for number in range(0,11,2):
        print(number)

    #prompt the user for start and stop values and print the numbers between start and stop
    #get the start value from the user and convert it to an integer
    #get the stop value from the user and convert it to an integer
    #use the start and stop in  a for loop
    while(True):
        try:
            start_num = int(input("pleasae provide a starting number: "))
            end_num = int(input("pleasae provide a stoping number: "))
            break
        except:
            print("please provide an integer :(")
            continue
    for number in range(start_num,end_num):
        print(number)


main()