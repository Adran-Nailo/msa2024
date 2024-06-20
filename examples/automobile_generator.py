import automobile

def main():
    #create automobile objects
    auto1 = automobile.Automobile("Ford","Focus","1234",2.2,"Alice",2013)
    auto2 = automobile.Automobile("Honda","Accord","23456", 3.0, "Bob", 2017)

    print(f"{auto1.make} {auto1.model}: {auto1.year}")
main()