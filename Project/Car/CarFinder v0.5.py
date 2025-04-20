# CarFinder.py

db = "AuthorizedVehicles.txt"

# Load vehicles from file

def loadVehicles():
    try:
        with open(db, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []
    
# Save vehicle to file
def saveVehicles(vehicles):
    with open(db, "w") as file:
        for vehicle in vehicles:
            file.write(vehicle + "\n")

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
    vehicles = loadVehicles()
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in vehicles:
        print(vehicle)

def searchVehicle():
    vehicles = loadVehicles()
    searchQuery = input("\nPlease Enter the full vehicle name: ")
    if searchQuery in vehicles:
        print(f"\n{searchQuery} is an authorized vehicle")
    else:
        print(f"\n{searchQuery} is not an authorized vehicle, if you received this in error please check the spelling and try again")

def addVehicle():
    vehicles = loadVehicles()
    newVehicle = input("\nPlease Enter the full Vehicle name you would like to add: ")
    vehicles.append(newVehicle)
    saveVehicles(vehicles)
    print(f'\nYou have added "{newVehicle}" as an authorized vehicle')

def deleteVehicle():
    vehicles = loadVehicles()
    vehicleToRemove = input("\nPlease Enter the full Vehicle name you would like to REMOVE: ")

    if vehicleToRemove in vehicles:
        confirmation = input(f'\nAre you sure you want to remove "{vehicleToRemove}" from the Authorized Vehicles List?\n').lower()
        if confirmation == "yes":
            vehicles.remove(vehicleToRemove)
            saveVehicles(vehicles)
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