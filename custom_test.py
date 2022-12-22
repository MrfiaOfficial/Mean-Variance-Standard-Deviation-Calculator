import mean_var_std as mvs

# ask the user to input multiple integers or floats
numbers = input("Enter multiple integers or floats separated by a space: ")

# split the input string on the space character to create a list of strings
list = numbers.split()

# check if the number of inputted figures are 9 or not
mvs.calculate(list)
