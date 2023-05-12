# Find text in files
This Python code searches for a specific word or string within all the files present in a specified directory.

First, it imports two modules from the Python Standard Library: ```os``` and time. The os module is used to handle directory operations, while the time module is used to measure the execution time of the script.

Next, the script prompts the user to input the directory path where the search should be performed. The variable searchstring is also initialized, which will contain the string to search.

The os.listdir() method is used to iterate through all the files in the specified directory. For each file, the script first checks if it is a file (as opposed to a subdirectory), and then opens it for reading using the open() method with the r mode. The script then checks if the search string is present in the file's contents using the in operator. If the string is found, the file name is printed to the console.

The script keeps track of the number of files where the search string is found using the cont variable.

Finally, the script calculates the total execution time by subtracting the start time (starTime) from the end time (endTime), and prints the total number of times the search string was found as well as the elapsed execution time to the console.

Note that the directory variable is currently set to an empty string, so the user will need to input the directory path when prompted in order for the script to function properly.
