import student
from datetime import datetime
"""
Function to write error log file
input: error message
Output: none
"""
def write_to_error_log(error_message):
    try:
        #open log file
        log_file = open("error_log.txt", "a")
        #write error message to log file
        log_file.write(f"{datetime.now()}: {error_message}\n")
        #close log file
        log_file.close()
    except Exception as err:
        print(err)
    return

#function to load student data from file
#input: path to a file
#output: list of students
def load_students(file_name):
    #create an empty list to store automobile data
    student_list = []
    #open the file
    student_file = open(file_name, "r")
    student_file.readline()
    #read each line of the file in a for loop
    line_number = 1
    for line in student_file:
        #increment line_number by 1
        line_number += 1
        #split each line at the comma to get the values
        student_data = line.split(",")
        

        #check that student data contains six items
        #if not, raise error and skip that line of data
        try:
            if len(student_data) != 6:
                raise Exception (f"There is an error in your data file. The error was found on line {line_number}.")
        except Exception as err:
            write_to_error_log(str(err))
            continue

        #get individual values from the resulting list
        try:
            first_name = student_data[0]
            last_name = student_data[1]
            major = student_data[2]
            credit_hours = int(student_data[3])
            if credit_hours < 0:
                raise Exception (f"Credit hours less than 0")
            gpa = float(student_data[4])
            if gpa < 0:
                raise Exception (f"GPA less than 0")
            id_number = int(student_data[5])
        except Exception as err:
           write_to_error_log(f"ERROR: {err} on line {line_number}")


        #create automobile objects with the data
        new_student = student.Student(first_name,last_name,major,credit_hours,gpa,id_number)
        #append each student to the list of students
        student_list.append(new_student)
    #close the file and retrun the list of students
    student_file.close()
    return student_list

#create a function called student_to_dictionary that creates a student dictionary for each student object
#add student dictionaries to a list
#function


def student_to_dictionary(student_list):
    list_of_student_dictionaries = []
    for student in student_list:
        student_dictionary = {
            "first_name": student.get_first_name(),
            "last_name": student.get_last_name(),
            "id": student.get_id(),
            "major": student.get_major(),
            "gpa": student.get_gpa(), 
            "class": student.get_class_level()
        }
        list_of_student_dictionaries.append(student_dictionary)
    return list_of_student_dictionaries
        


def get_student_dictionaries():
    #load a list of students from data in a file
    student_list = load_students("students.csv")
    #print info for each student in a for loop

    student_dictionaries = student_to_dictionary(student_list)
   
    return student_dictionaries
