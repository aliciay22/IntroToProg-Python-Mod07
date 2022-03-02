# ---------------------------------------------------------------------------- #
# Title: Assignment07
# Description: This script includes a demo of how pickling works in python and
#              a demo of how error handling works.
# ChangeLog (Who,When,What):
# Alicia Y, 2.28.20322, Created file
# ---------------------------------------------------------------------------- #


# Demo of how pickling works in python

import pickle  # This imports code from another code file!

#  Demonstrate how to pickle and unpickle a python dictionary object

# Define dictionary object
cats_dict = {'Gizmo': 'Tabby', 'Tribble': 'Calico', 'Jupiter': 'Siamese'}


# Open the file, use argument 'wb' to write to the file
filename= 'BinDict.dat'
outfile = open(filename,'wb')
pickle.dump(cats_dict,outfile)  # Store (dump) the data into the binary file
outfile.close()                 # Close the file, file appears in working directory


# Unpickle file
infile = open(filename,'rb')    # open the file
new_dict = pickle.load(infile)  # assign to object
infile.close()                  # Close the file

# Print the data to make sure unpickling worked
print(new_dict)
print(new_dict==cats_dict)
print(type(new_dict))

# Demo of error handling in python
# Suppose inputs must be certain types of data (integer, character, etc.)

# Define error function classes
class IntOnly(Exception):
    """  Error when integers are expected  """
    def __str__(self):
        return 'You must enter integers only.'

class CharOnly(Exception):
    """  Error when characters are expected  """
    def __str__(self):
        return 'You must enter characters only.'



while (True):
    print("""
        Menu of Options
        1. Enter ID
        2. Enter name
        3. Exit 
        """)
    strChoice = str(input("Which option would you like to perform? [1 - 3] - "))
    print()  # Adding extra line for breaks

    if strChoice == '1':
        try:
            strId = input("Enter an Id: ")  # only integer data
            if strId.isalpha():
                raise intOnly()

        except Exception as e:
            print("You must enter characters only.")

    elif strChoice == '2':
        try:
            strName = input("Enter a name: ")  # only character data
            if strName.isnumeric():
                raise CharOnly()

        except Exception as e:
            print("You must enter an integer.")


    elif strChoice == '3':
        print("Goodbye")
        break
