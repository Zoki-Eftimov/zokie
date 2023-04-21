#!/usr/bin/python3
# This script will calculate average of 3 postiive numbers and will print error if the conditions are not met.
#< 
#Replace the line above with a short description of the script.  Sometimes
#people use multiple lines todescribe the inputs and expected outputs.
#>

# Versioning
# Zoki-2020-04-21: initial versionv.0.0.1
#<
#Replace the line above with the date you finished and your name
#As you revise it, add in more lines with what you changed
#>

# Set up initial variables and imports
#import sys
#SITES = ['bhs','ah','lms']
#MAIL_SERVER = 'smtp.google.com'
#< 
#Put any global or initial variables here. This is the only place where folks
#should make quick changes to the script such as using a different mail server
#account.  Change/remove the example lines above as needed 
#>

# Main routine that is called when script is run
def main():
# 
# This command defines the main function
    print("Hello, there!\n")
# Greeting the user


    print("This script will calculate the average of 3 positive numbers!\n")
# Describing the script to the user

# While loop so the error message can be processed if invalid entry
    while True:
# setting variable nums that will prompt user to enter 3 positive numbers separated by space
        nums = input("Enter 3 positive numbers separated by a space: ")
        try:
#setting the parameters and setting the input to accept integers, I was confused if I was supposed to use float or int, I decided to go with int, based on the example output.
            num1, num2, num3 = map(int, nums.split())
            break
# setting exception for the error, if user enter anything other than 3 integer values separated by space
        except ValueError:
            print("\nError\u2757 Please enter 3 positive numbers separated by a space\u2757\n")
# printing the error message


#calculate the average of the 3 numbers
    avg3 = (num1 + num2 + num3) / 3
# rounding the result to two decimals
    avg3print = round(avg3, 2)
# print/output the result
    print("\nThe average of",num1,",",num2,", and",num3,"is",avg3print)

#another greeting for the user
    print("\nThank you for using this script.\U0001F60E\n\nGoodbye!")



# Subroutines not needed for this script
#<
#The subroutines called by the main function are listed here
#>


# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()


