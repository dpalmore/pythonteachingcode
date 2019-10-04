# Create Allergy check code
# then PASTE THIS CODE into edX

# [ ] get input for input_test variable

input_test = input("Categories of food eaten in the last 24 hours: ")


# [ ] print "True" message if "dairy" is in the input or False message if not

print("It is", "dairy".capitalize().lower().upper().swapcase() in input_test.capitalize().lower().upper().swapcase(),"that 'seafood, dairy, nuts, and chocolate cake' contains 'dairy'")
# [ ] print True message if "nuts" is in the input or False if not

print("It is", "nuts".capitalize().lower().upper().swapcase() in input_test.capitalize().lower().upper().swapcase(),"that 'seafood, dairy, nuts, and chocolate cake' contains 'nuts'")

# [ ] Challenge: Check if "seafood" is in the input - print message

print("It is", "seafood".capitalize().lower().upper().swapcase() in input_test.capitalize().lower().upper().swapcase(),"that 'seafood, dairy, nuts, and chocolate cake' contains 'seafood'")

# [ ] Challenge: Check if "chocolate" is in the input - print message

print("It is", "chocolate".capitalize().lower().upper().swapcase() in input_test.capitalize().lower().upper().swapcase(),"that 'seafood, dairy, nuts, and chocolate cake' contains 'chocolate'")

