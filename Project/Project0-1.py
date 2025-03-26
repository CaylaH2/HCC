# CarFinder.py

def displayMenu():
    print("\n********************************AutoCountry Vehicle Finder v0.1********************************")
    print("Please Enter the following number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print ("2. Exit")

def printVehicles():
    allowedVehicles = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in allowedVehicles:
        print(vehicle)

def main():
    while True:
        displayMenu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            printVehicles()
        elif choice == "2":
            print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("\nInvalid selection. Please enter 1 or 2.")

if __name__ == "__main__":
    main()