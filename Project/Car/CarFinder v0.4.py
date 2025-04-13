# CarFinder.py

# Make the list global so all functions share it and can modify it
allowedVehicles = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan', 'Rivian R1T', 'Ram 1500']

def displayMenu():
    print("\n********************************")
    print("AutoCountry Vehicle Finder v0.4")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicles")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")
    print("********************************")

def printVehicles():
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in allowedVehicles:
        print(vehicle)

def searchVehicle():
    searchQuery = input("\nPlease Enter the full Vehicle name: ")
    if searchQuery in allowedVehicles:
        print(f"\n{searchQuery} is an authorized vehicle")
    else:
        print(f"\n{searchQuery} is not an authorized vehicle, if you recieved this in your error please check the spelling and try again")

def addVehicle():
    newVehicle = input("\nPlease Enter the full Vehicle name you would like to add: ")
    allowedVehicles.append(newVehicle)
    print(f'\nYou have added "{newVehicle}" as an authorized vehicle')

def deleteVehicle():
    vehicleToRemove = input("\nPlease Enter the full Vehicle name you would like to REMOVE: ")
    if vehicleToRemove in allowedVehicles:
        confirmation = input(f'\nAre you sure you want to remove "{vehicleToRemove}" from the Authorized Vehicles List?\n').lower()
        if confirmation == "yes":
            allowedVehicles.remove(vehicleToRemove)
            print(f'\nYou have REMOVED "{vehicleToRemove}" as an authorized vehicle')
        else:
            print()
    else:
        print(f'\n"{vehicleToRemove}" was not found in the Authorized Vehicles List.')


def main():
    while True:
        displayMenu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            printVehicles()
        elif choice == "2":
            searchVehicle()
        elif choice == "3":
            addVehicle()
        elif choice == "4":
            deleteVehicle()
        elif choice == "5":
            print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("\nInvalid selection. Please enter 1, 2, 3, 4 or 5.")

if __name__ == "__main__":
    main()