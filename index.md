Alicia Young

February 28, 2022

IT FDN 110 A 

Assignment 7

https://github.com/aliciay22/IntroToProg-Python-Mod07



# Pickling and Error Handling Demos

## Introduction

The goal of this lesson is to demonstrate how pickling and error handling work in Python.  Pickling refers to converting a python object to a binary file, and unpickling refers to converting the object back to its original form.  Error handling refers to telling python how to handle errors, rather than having the program crash when they are encountered. 

## Summary

### Pickling/Unpickling

First the script demonstrates how pickling and unpickling work.  To begin the pickling process, the code must import the pickle module.

![image](https://user-images.githubusercontent.com/99776233/156312015-f928bd33-7d22-4194-94fc-fc7cbb988c16.png)

This example pickles a python dictionary object into a binary file.  The dictionary object is defined.

![image](https://user-images.githubusercontent.com/99776233/156312178-0288ca6b-00a6-4375-9f4b-594d9381b59f.png)
 
Next, the file is opened, specifying the ‘wb’ option, which refers to write binary.

![image](https://user-images.githubusercontent.com/99776233/156312288-7ba9e177-703e-4202-a73a-50cd32591c83.png)
 
Then we use the pickle.dump() function to store (dump) the data into the file.  The functions takes two argument, the object to be pickled and the file to which the object will be saved.	  After pickle.dump, we close the file.
 
![image](https://user-images.githubusercontent.com/99776233/156312365-6f12c4f7-b7a6-4cea-bd4b-9ee6c0afe1d9.png)

The file, BinDict.dat in this example, will be saved in the working directory.

To then unpickle a file, we open the file and then use the pickle.load() function with the ‘rb’ option (read binary) to load the data back into a python object. Then close the file.

![image](https://user-images.githubusercontent.com/99776233/156312422-614ea7c6-0ad6-405b-a407-eb932c0a3b25.png)

We can print the data the new object, dictionary in this case, to make sure the results are as expected.
 
![image](https://user-images.githubusercontent.com/99776233/156312449-5f4f590d-6407-4257-bb19-3f4b5f5c6215.png)

I found the following websites helpful, and the first one inspired this example.

https://www.datacamp.com/community/tutorials/pickle-python-tutorial

https://sites.pitt.edu/~naraehan/python3/pickling.html

https://towardsdatascience.com/do-not-use-python-pickle-unless-you-know-all-these-facts-d9e8695b7d43

### Exceptions and Error Handling

Error handling in Python makes the code more robust and can prevent the code from crashing by diverting to an alternate path when errors are identified or prompting the user for correct input when invalid data are supplied.

To demonstrate error handling, I created functions that checked that the user input either numeric or character data using a try/except block with a raise condition.
The code under the try block executes unless the condition under raise is met. Meeting this condition forces an exception.

In this example, I defined two error function classes, one to check for numeric data and one to check for character data.

![image](https://user-images.githubusercontent.com/99776233/156312943-6e2e3d1f-4886-4efa-a2e2-427400623f80.png) 

In the main script, the user has a choice to enter either an ID (numeric data) or a name (character data).  If the user enters character data when integer data is expected or numeric data when character data is expected an exception is raised and a message is printed to the user.  The code continues to run then even when the user enters something unexpected.

![image](https://user-images.githubusercontent.com/99776233/156313053-cb6da8b9-4829-4743-918a-db6c87f0e586.png)
 

I found the following websites helpful for error handling:

https://www.w3schools.com/python/gloss_python_error_handling.asp

https://www.datacamp.com/community/tutorials/exception-handling-python

https://rollbar.com/blog/throwing-exceptions-in-python/

## Summary

This script provides simple demonstrations of pickling/unpickling in python and how error handling can be utilized.  Pickling may be useful in help code run faster, and error handling is important for catching input and other errors.

