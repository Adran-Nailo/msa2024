import color_testing
import datetime
color = color_testing.Color() 
#create an auto mobile class
class Automobile():

    #define a constructor
    #the constructor is a function that executes when an object is created
    def __init__(self,make,model, vin, engine_size, owner, year):
        #assign class properties values
        self.__make = make
        self.__model = model
        self.__vin = vin
        self.__engine_size = float(engine_size)
        self.__owner = owner
        self.__year  = int(year)
    
    #create get and set methods for class properties
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_vin(self):
        return self.__vin
    
    def get_engine_size(self):

        return self.__engine_size
    
    def set_engine_size(self, new_size):
        try:
            self.__engine_size = float(new_size)
        except:
            print(f"{color.red}{color.bold}{color.underline}ERROR: Engine size must be a number{color.default}\n")

    def get_owner(self):
        return self.__owner
    
    def set_owner(self, new_owner):
        if new_owner == "":
            print(f"{color.red}{color.bold}{color.underline}ERROR: Enter the new owner's name{color.default}\n")
        else:
            self.__owner = new_owner

    def get_year(self):
        return self.__year
    
    #create a method to get the automobile's age 
    def get_age(self):
        #get the current year
        current_date=datetime.datetime.now()
        this_year = current_date.year
        #return the difference between current year and auto year
        return this_year - self.__year
    
    #create a method to print automobile info
    def print_info(self):
        print(f"{self.__year} {self.__make} {self.__model}")
        print(f"VIN: {self.__vin}, Engine Size: {self.__engine_size}")
        print(f"Owner: {self.__owner}\n")        
        