#write a program to calculate yearly wages
#write a function to geta positive number from the user for wages
def get_postitive_float_input(prompt, must_be_less_than_24):
  #ask a user to input their wages, and validate correct input
  #if bad input, reprompt the user
  gen_value = 0
  while (True):
    try:
      gen_value = float(input(prompt))
      #check if gen_value is greater than 0, if not reprompt the user
      if gen_value <= 0:
        print("ERROR: Enter a number greater than 0")
        continue
      if gen_value > 24 and must_be_less_than_24:
        print("ERROR: Hours worked must be less than 24")
        continue
      break
    except:
      print("ERROR: Please enter a number greater than 0")
  return gen_value

 

def main():
  while (True):
    #INPUT
    #get wages from the user
    wages_hourly = get_postitive_float_input("Enter your hourly wage:", False)

    #get hours from user
    hours = get_postitive_float_input("Enter your dialy hours:", True)
        

    #PROCESSING
    #calculate wages each year, before and after taxes
    tax_amount = 0.12
    wages_before_tax = hours * wages_hourly * 350
    taxes = 0.12 * wages_before_tax
    total_wages = wages_before_tax - taxes

    #OUTPUT
    #print output to the user
    print("")
    print("PAY ADVICE")
    print("--------------")
    print(f"Hours worked: {hours: .2f}")
    print(f"Hourly wage: ${wages_hourly: .2f}")
    print(f"Wages before taxes: ${wages_before_tax: .2f}")
    print(f"Tax ammount: ${taxes: .2f}")
    print(f"Annual wages after taxes: ${total_wages: .2f}")
    print("")

    #ask user if they want another pay advice
    response = input(f"do you want to run the program again? Enter 'y' to continue: ")
    if response == "yes":
      continue
    print("program ending...")
    break


#calls the main function
main()
