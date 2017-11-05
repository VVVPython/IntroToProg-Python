'''-------------------------------------------------
Assignment 6
Developer: Vladimir Vasilev
Version: New
Date:  Nov 5, 2017
Title: Working with classes / functions
-------------------------------------------------'''

# -- Data -- #
objFileName = "/Users/vladimir/_PythonClass/ToDo.txt"
strData = ""
dicRow = {}
lstTable = []

# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.

objFile = open(objFileName, "r")
for line in objFile:
    strData = line.split(",")  # readline() reads a line of the data into 2 elements
    dicRow = {"Task": strData[0].strip(), "Priority": strData[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Processing -- #
# -- define class -- #
class DataProcessor(object):
    """ This class contains methods for processing user data """

    # Define the method
    @staticmethod
    def showcurrentdata():
        """ This function show current dat """
        print("******* The current items ToDo are: *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")

    @staticmethod
    def addnewitem():
        strTask = str(input("What is the task? - ")).strip()
        strPriority = str(input("What is the priority? [high|low] - ")).strip()
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        #  Show the current items in the table
        print("******* The current items ToDo are: *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")

    @staticmethod
    def removeexistingitem():
        #  Allow user to indicate which row to delete
        strKeyToRemove = input("Which TASK would you like removed? - ")
        blnItemRemoved = False  # Creating a boolean Flag
        intRowNumber = 0
        while(intRowNumber < len(lstTable)):
            if(strKeyToRemove == str(list(dict(lstTable[intRowNumber]).values())[0])):  # the values function creates a list!
                del lstTable[intRowNumber]
                blnItemRemoved = True
            #  end if
            intRowNumber += 1
        #  end for loop
        #  Update user on the status
        if(blnItemRemoved == True):
            print("The task was removed.")
        else:
            print("I'm sorry, but I could not find that task.")

        #  Show the current items in the table
        print("******* The current items ToDo are: *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")

    @staticmethod
    def savedatatofile():
        #  Show the current items in the table
        print("******* The current items ToDo are: *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")
        #  Ask if they want save that data
        if("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):
            objFile = open(objFileName, "w")
            for dicRow in lstTable:
                objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
            objFile.close()
            input("Data saved to file! Press the [Enter] key to return to menu.")
        else:
            input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")


# -- Input/Output -- #
#  Display a menu of choices to the user
while(True):
    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()  # adding a new line


# -- presentation (I/0) code --
# Call the method (function)

    # Show the current items in the table
    if (strChoice.strip() == '1'):
        DataProcessor.showcurrentdata()
        continue  # to show the menu

    # Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        DataProcessor.addnewitem()
        continue  # to show the menu

    # Remove a new item to the list/Table
    elif(strChoice == '3'):
        DataProcessor.removeexistingitem()
        continue  # to show the menu

    # Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        DataProcessor.savedatatofile()
        continue  # to show the menu

    # Exit program
    elif (strChoice == '5'):
        break  # and Exit the program