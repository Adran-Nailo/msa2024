"""
get the difficulty level from user
ask for the number of questions
run the function that coincides with that difficulty, and pass the number of questions to the other function
    get random numbers
    add the 2 numbers, and store in a variable
    print the two numbers and present them to the user
    get the input from the user
    compare the user's response to the sum of the two random numbers
    if it is wrong, add one to the "wrong" variable
        when 3 questions have been gotten wrong, show the correct answer
    if it is correct, repeat agin for the next question, and add one to the amount of questions gotten correct
    once all the questions have been completed, divide the number of questions correct by the amount of questions total, and print the result multiplied by 100
"""
import random

def get_level():
    while True:
        try:
            level = int(input("what level do you want to play? 1, 2, or 3: "))
            if level != 1 and level != 2 and level != 3:
                print("ERROR: Invalid Input!")
                continue    
            break
        except:
            print("ERROR: Invalid Input!")
    return level

def get_amount_of_questions():
    while True:
        try:
            amount_of_questions = int(input("Enter number of questions to ask: 3 to 10: "))
            if amount_of_questions < 3 or amount_of_questions > 10:
                print("ERROR: Please enter an integer value between 3 and 10!")
                continue    
            break
        except:
            print("ERROR: Invalid Input!")
    return amount_of_questions

def game(amount_of_questions,start_range,end_range):
    correct_answers = 0
    for number in range(amount_of_questions):
        wrong_answers = 0
        number_1 = random.randint(start_range,end_range)
        number_2 = random.randint(start_range,end_range)
        sum_of_numbers = number_1 + number_2
        for wrong_checks in range(3):
            try:
                answer = int(input(f"{number_1} + {number_2} = "))
                if answer == sum_of_numbers:
                    break
                else:
                    print("WRONG!!!")
                    wrong_answers += 1
                    continue
            except:
                print("WRONG!!!")
                wrong_answers += 1
                continue
        if wrong_answers == 3:
            print(f"Correct Answer: {number_1} + {number_2} = {sum_of_numbers}")
        else:
            correct_answers += 1
    percentage = (correct_answers / amount_of_questions) * 100
    print(f"You got {correct_answers} out of {amount_of_questions} correct. You got an {percentage}%")

def main():
    difficulty = get_level()
    amount_of_questions = get_amount_of_questions()

    if difficulty == 1:
        game(amount_of_questions, 0, 9)
    elif difficulty == 2:
        game(amount_of_questions, 10, 99)
    elif difficulty == 2:
        game(amount_of_questions, 100, 999)

main()