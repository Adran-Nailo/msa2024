import automobile as auto
import color_testing 
color = color_testing.Color()
#function to load vehicle data from file
#input: path to a file
#output: list of automobiles
def load_vehicles(file_name):
    #create an empty list to store automobile data
    auto_list = []
    #open the file
    auto_file = open(file_name, "r")
    auto_file.readline()
    #read each line of the file in a for loop
    line_number = 1
    for line in auto_file:
        #increment line_number by 1
        line_number += 1
        #split each line at the comma to get the values
        vehicle_data = line.split(",")
        

        #check that veicle data contains six items
        #if not, raise error and skip that line of data
        try:
            if len(vehicle_data) != 6:
                raise Exception (f"{color.red}{color.bold}{color.underline}There is an error in your data file.\nThe error was found on line {line_number}. {color.default}")
        except Exception as err:
            print(str(err))
            continue

        #get individual values from the resulting list
        try:
            make = vehicle_data[0]
            model = vehicle_data[1]
            vin = vehicle_data[2]
            if vehicle_data[3].lower() == "electric":
                engine_size = 0
            else:
                engine_size = float(vehicle_data[3])
            owner_name = vehicle_data[4]
            year = int(vehicle_data[5])
        except Exception as err:
            print(f"{color.red}{color.bold}{color.underline}ERROR: {err} on line {line_number}{color.default}")


        #create automobile objects with the data
        new_auto = auto.Automobile(make,model,vin,engine_size,owner_name,year)
        #append each automobile  to the list of automobiles
        auto_list.append(new_auto)
    #close the file and retrun the list of automobiles
    auto_file.close()
    return auto_list

def main():
    #load a list of automobiles from data in a file
    automobile_list = load_vehicles("vehicle_data.csv")
    #print info for each automobile in a forr loop
    for vehicle in automobile_list:
        vehicle.print_info()

main()