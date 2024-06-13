def main():
    #create a while loop that prints integers between 0 and 10
    
    stop_value=10
    number=0
    #run the loop while output_value <= stop_value
    while (number <= stop_value):
        print(number)
        #increment number
        number +=1
    print("\n\n")
    number=0
    while (True):
        
        print(number)
        number +=1
        #if output_value is greater than number, break
        if number > stop_value:
            break  
main()