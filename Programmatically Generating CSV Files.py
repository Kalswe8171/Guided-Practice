
# Student ID: Kalswe8171
# Date: October 25, 2026
# Description: Save and read spreadsheet data using a CSV file.

from datetime import datetime
import os


# This function converts measurements based on the spreadsheet type.
def convertData(dataValue):
    if spreadsheetType == "1":
        return (dataValue - 32) * 5 / 9
    elif spreadsheetType == "2":
        return dataValue / 2.205
    elif spreadsheetType == "3":
        return dataValue * 2.54
    else:
        raise ValueError("Invalid spreadsheet type.")


# This function adds data to a CSV file or creates it if needed.
def insertData(filePath, commaSeparatedData):
    try:
        with open(filePath, "a", encoding="utf-8") as csvFile:
            csvFile.write(commaSeparatedData + "\n")
        return True

    except OSError as error:
        print("Error saving data:", error)
        return False


# This function reads and displays the CSV file and its path.
def viewData(filePath):
    try:
        with open(filePath, "r", encoding="utf-8") as csvFile:
            print("\nReading file:", os.path.abspath(filePath))
            print("--- Saved Data ---")

            savedData = csvFile.read()
            print(savedData if savedData else "The file is empty.")

    except FileNotFoundError:
        print("ZooData.csv does not exist yet.")
        print("Choose option 1 to save data first.")

    except OSError as error:
        print("Error reading data:", error)


# This function collects, converts, and saves each data entry.
def getInput():
    global spreadsheetType

    print("\nChoose the type of data:")
    print("1. Temperature (Fahrenheit to Celsius)")
    print("2. Weight (pounds to kilograms)")
    print("3. Rainfall (inches to centimeters)")

    spreadsheetType = input("Choose type (1-3): ")

    if spreadsheetType not in ("1", "2", "3"):
        print("Invalid spreadsheet type.")
        return

    try:
        numberOfEntries = int(input("How many entries will you enter? "))

        if numberOfEntries <= 0:
            print("Please enter a number greater than zero.")
            return

    except ValueError:
        print("Please enter a valid whole number.")
        return

    spreadsheetNames = {
        "1": "Temperature (F to C)",
        "2": "Weight (lbs to kg)",
        "3": "Rainfall (in to cm)"
    }

    for entryNumber in range(numberOfEntries):
        try:
            print(f"\nEntry {entryNumber + 1}:")

            entryDate = input("Enter date (MM/DD/YYYY): ")
            dataValue = float(input("Enter the measurement: "))

            convertedValue = convertData(dataValue)

            commaSeparatedData = (
                f"{entryDate},{spreadsheetNames[spreadsheetType]},"
                f"{dataValue},{convertedValue:.2f}"
            )

            if insertData("ZooData.csv", commaSeparatedData):
                print(
                    f"The following data was saved at "
                    f"{datetime.now()}: {commaSeparatedData}."
                )

        except ValueError:
            print("Invalid number. This entry was not saved.")

        except OSError as error:
            print("Could not process this entry:", error)


# This function displays the menu and handles user selections.
def main():
    print("Kalswe8171 Spreadsheet Automation Menu")

    while True:
        print("\n1. Input Data")
        print("2. View Current Data")
        print("3. Generate Report")
        print("4. Exit")

        # The next line retrieves the inputted option
        # and stores it in the variable called choice.
        choice = input("Enter your option number (1-4): ")

        if choice == "1":
            getInput()

        elif choice == "2":
            viewData("ZooData.csv")

        elif choice == "3":
            print("The report feature has not been added yet.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Enter 1, 2, 3, or 4.")


main()
