def main():
#list [1, 4, 6, 7, 78]
    scores = [1, 4, 6, 7, 78]
    student_names = ["Alice", "Bob", "Jerry", "Jane", "Bill"]
    for index in range(len(scores)):
        print(f"{student_names[index]}: {scores[index]}")

    #Create a dictionary of names and scores
    student_scores = {
        "Alice": 87, 
        "Bob": 79,
        "Jerry": 94,
        "Sara": 90
    }
    #print Bob and Sara's scores
    print(student_scores["Bob"])
    print(student_scores["Sara"])

    #get all the keys and values from the student_scores dictionary
    print("\n\n")
    for student in student_scores:
        print(f"{student}: {student_scores[student]}")

    #declare a car dictionary
    car = {
        "make": "Ferrari",
        "model": "F-50",
        "year": 2021,
        "value": 500000,
        "engine": 4.8
    }
    #get all the keys and values from the car dictionary
    print("\n\n")
    for key, value in car.items():
        print(f"{key}: {value}") 
main()