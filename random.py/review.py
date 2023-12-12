# This program calculates miles per gallon
print("this program calculates mpg")

#Enter the number of miles the user drives
miles_driven = input("Enter miles driven:  ")

# Convert to float
miles_driven = float(miles_driven)

# Enter number of gallons used
gallons_used = input("Enter gallons used:  ")

#Convert to float
gallons_used = float(gallons_used)

# Calculate and print the answer
mpg = miles_driven/gallons_used
print("miles per gallons is:",mpg)