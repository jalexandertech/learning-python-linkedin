# 
# Example file for variables
#

# Declare a variable and initialize it

carName = "Nissan Rouge"
print(carName)

# re-declaring the variable works

carName = "Nissan 370z"
print(carName)

# ERROR: variables of different types cannot be combined

x = 1
y = "Dog"
print(str(x) + y)

# Global vs. local variables in functions

favoriteName = "Kaliyah" #Global variable 

def name():
    global favoriteName #This will make it where the variable is in fact global so the variable outside the function will not print. 
    favoriteName = "Jose" #Local variable 
    print(favoriteName)

name() #This is printing the local variable defined in the function
print(favoriteName) #This is printing the global variable declared outside of the function

