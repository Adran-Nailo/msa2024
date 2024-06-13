def main():
    #list demo
    #create a kist if string names
    names = ["john","mary","alice","bob",]
    list_of_integers = [10,16,24,42,14,9]
    random_type_list = ["cyd", 15, 12.54, "frank"]

    print(names)
    print(list_of_integers)

    #add values to a list
    names.append("Jonny")
    list_of_integers.append(5)
    list_of_integers.append(63)

    print(names)
    print(list_of_integers)
    #get the number of items in a list
    number_of_items = len(list_of_integers)
    print("\n\n")
    print(f"number of items in interger list: {number_of_items}")

    #get values from our list

    print("\n")
    #print all items in the list of integers using while loop
    number = 0
    while number < len(list_of_integers):
        print(list_of_integers[number])
        number +=1
    print("\n")    
    
    #print all items in the list of integers using for loop
    for item in list_of_integers:
        print(item)
    
    #print all items in the list of integers using for loop and range function
    print("\n")
    for index in range(len(list_of_integers)):
        print(f"item {index+1} is {list_of_integers[index]}")


main()