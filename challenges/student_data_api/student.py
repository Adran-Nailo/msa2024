
class Student():
    def __init__(self,first_name,last_name, major, credit_hours, gpa, id_number):
        #assign class properties values
        self.__first_name = first_name
        self.__last_name = last_name
        self.__major = major
        self.__credit_hours = int(credit_hours)
        self.__gpa = float(gpa)
        self.__id_number  = int(id_number)

    def get_first_name(self):
            return self.__first_name

    def get_last_name(self):
            return self.__last_name

    def get_major(self):
            return self.__major

    def get_credit_hours(self):
            return self.__credit_hours

    def get_gpa(self):
            return self.__gpa

    def set_gpa(self,new_gpa):
            try:
                self.__gpa = float(new_gpa)
            except:
                print(f"ERROR: GPA must be a number\n")


    def get_id(self):
            return self.__id_number

    def get_class_level (self):
            if self.__credit_hours >= 0 and self.__credit_hours <= 30:
                year = "Freshman"
            elif self.__credit_hours >= 31 and self.__credit_hours <= 60:
                year = "Sophomore"
            elif self.__credit_hours >= 61 and self.__credit_hours <= 90:
                year = "Junior"
            elif self.__credit_hours > 90:
                year = "Senior"
            return year

    def update_credit_hours (self, additional_hours):
        self.__credit_hours += additional_hours

    def print_student_data(self):
        print(f"\n{self.__first_name} {self.__last_name}")
        print(f"Major: {self.__major}")
        print(f"Credit Hours: {self.__credit_hours}")
        print(f"GPA: {self.__gpa}")
        print(f"ID Number: {self.__id_number}")
