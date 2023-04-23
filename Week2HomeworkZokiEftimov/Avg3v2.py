#!/usr/bin/python3
# This script will calculate average of 3 postiive numbers and will print error if the conditions are not met.

# Versioning
# Zoki-2020-04-21: initial versionv.0.0.1
# Zoki-2020-04-23: revised version v.0.0.2   
# Zoki-2020-04-23: revised version v.2
# Added import sys, sys.argv, instead of using while loop, my script now has if and else statements that validate arguments, the exception stayed there to validate
# the error, and print error message if the conditions are not met.
# Added color to the print statement

# Set up initial variables and imports
import sys

# Main routine that is called when script is run
def main():
    total = 0.0 
# This command defines the main function

    # Getting the length of command line arguments
    n = len(sys.argv)

    #This line will check if there are exactly 4 command line arguments, like in this example the script name plus three numbers to calculate the average
    if n == 4:
    #The following command will convert the second, third and 4th argument to integers using map(int,sys.argv[1:])'. Then assigns the integers to the variables
        #num1, num2, and num3, then calculates the total and divides by 3 to find the average
        try:
            num1, num2, num3 = map(float, sys.argv[1:])
            total = num1 + num2 + num3
            average = total / 3.0
            #This is a print statement to greet the user and give description of what this script does
            print("\nHello, there!\U0001F604\n\nThis script will calculate the average of the 3 positive numbers you entered!\n")
            #This prints the results, if the conversion is succesful; I made these two print statements next to each other because I realized
            #Tto not print description of the program to the user if the error kicks in to not repeat the text
            print('\x1b[0;39;43m' + "The average of {},{}, and {} is {:.2f} \x1b[0m".format(num1, num2, num3, average))
        #If the conversion is not succesful, this block of code catches the ValueError exception and prints the error message telling the user to provide valid numbers
        except ValueError:
            print("Error\u2757 Please provide 3 valid numbers as input")
    #if there is only one command line argument just the script name, this block of code prints different error message telling the user to enter 3 positive numbers
    elif n == 1:
        print("\nError\u2757 Please enter 3 positive numbers separated by a space\u2757\n")
    #If there are any number of arguments other than 4, this block of code will print the error message to prompt user to enter 3 positive numbers
    else:
        print("\nError\u2757 Please provide exactly 3 positive numbers separated by spaces\u2757\n")
    #This line prints a goodbye message to the user.    
    print("\nThank you for using this script.\U0001F60E\n\nGoodbye!")


# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()
