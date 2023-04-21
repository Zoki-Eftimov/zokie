#!/usr/bin/python3
# This script will ask a user for their name and their favorite color. Then it will print a statement
# that will print the user's name and their favorite color based on the user's input. 
#< 
#Replace the line above with a short description of the script.  Sometimes
#people use multiple lines todescribe the inputs and expected outputs.
#>

# Versioning
# Zoki2023-04-20: initial version:1.00
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
#  """What does this function do"""
#<
#For each function, put in a doc string that tells me what the function is
#suppose to do. For each block of code such as a loop, large if statement, 
#etc, put a single line comment describing why it is needed
#>
  # The first print message will greet the user
#<
    print("Hello there! Welcome to my first Python script. I hope that you are having a great day!")
#Setting the first variable name, which will get user's name    
    name = input("What is your name? ")
#Setting variable color that will get user's favorite color
    color = input("What is your favorite color? ")
#Printing the message along with the user's input
    print("The favorite color for", name, "is", color)
#Greeting the customer and saying goodbye to them
    print("Dear,",name,". Thank you for using my Python script today!  Goodbye!")

# Subroutines
#<
#The subroutines called by the main function are listed here
#>


# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()


