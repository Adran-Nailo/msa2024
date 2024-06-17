def main():
    #capitalize a string
    my_name = "Oliver"
    print(my_name.capitalize())

    #make a string UPPERCASE
    print(my_name.upper())

    #make a string lowercase
    last_name = "FRAZIER"
    print(f"{my_name.capitalize()} {last_name.lower()}")

    #determine if a string starts with a set of characters
    print(my_name.startswith("O"))

    if( my_name.startswith("Oli") != True and my_name.startswith("oli") != True):
        print(f"You somehow spelled my name wrong!")
    else:
        print("you spelled my name correctly")

    #determine if a string ends with a specified set of charachters
    print(my_name.endswith("er"))

    if( my_name.endswith("er") != True):
        print(f"You somehow spelled my name wrong!")
    else:
        print("you spelled my name correctly")

    #find a set of characters in a string
    print(my_name.find("v",2))
    print("\n\n")
    for letter in my_name:
        print(letter)
        print(f"{my_name} has {len(my_name)} letters")
    
    for letter_index in range(len(my_name)):
        print(f"letter {letter_index+1}: {my_name[letter_index]}")

    print("\n\n")
    sentence = "I have a dog. My dog is cute. Do you want a dog?"

    #write a code that counts the number of appearances in sentence
    #expected output: 3
    #start at the begining string.
    #read the string until you find the first occurance of dog
    #add one to the number of found dogs
    #continue reading from the next index: update the start index in the find method
    letter_index = 0
    number_of_dogs = 0
    while letter_index <= len(sentence): 
        letter_index = sentence.find("dog", letter_index)+1
        if letter_index== 0:
            break
        number_of_dogs += 1
    print(f"Number of times dog was found: {number_of_dogs}")
    
    #how to use the split method
    car_info = "Ferrari, F-50, 2021, 500000, 4.8"

    car_data = car_info.split(sep=", ")
    print(car_data)
    
main()