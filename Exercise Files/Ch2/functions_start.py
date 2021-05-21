#
# Example file for working with functions
#

# define a basic function
def customerInformation():
    print("Her name is Jada and she is 25 years old.")
customerInformation()

# function that takes arguments
def customerNames(name1 = "Jada", name2 = "John", name3 = "Kiana"):
    print("First customer is " + name1 + ". Second customer is " + name2 + ". Lastly, the third customer is " + name3)
customerNames()

# function that returns a value
def mathEquation(x):
    return x + x
print(mathEquation(25)) #To run it in the terminal must print the function with a value to be assigned to x

# function with default value for an argument
def customerGreeting(name = "Jada"):
    print("Hello, " + name +"."  " How are you doing?")
customerGreeting("John") #No value in the parentheses will output Jada as default but when a new name is given then it will output the name given in the paratheses.

#function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result
print(multi_add(5, 10, 20, 45))
#Read https://www.geeksforgeeks.org/args-kwargs-python/ for more information

