#create an auto mobile class
class Automobile():

    #define a constructor
    #the constructor is a function that executes when an object is created
    def __init__(self,make,model, vin, engine_size, owner, year):
        #assign class properties values
        self.make = make
        self.model = model
        self.vin = vin
        self.engine_size = engine_size
        self.owner = owner
        self.year  = year