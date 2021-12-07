# carrying over from last week
# The purpose of this assignment is for you to become familiar with utilizing Python’s file object streams to store and retrieve data from secondary storage.
# Instructions
# For this assignment you will be modifying the used car dealer application from last week. There will be no code file provided for this assignment, you will be working from the previous week’s project files. Be sure to make a backup copy of your project folder before you begin work on this assignment.
# This week, you will be modifying your application to add two new menu items: Save Data, Load Data. The Save Data option will write the current vehicle data to a text file, overwriting any existing data. Load data will open the specified text file and read in the vehicle data into memory.
# Once you have the desired functionality, you will take screenshots of your program executing and the contents of your text file in order to demonstrate your program is able to save and load data to and from the text file. Paste your screenshots into a Word doc along with your completed code.
# From this weeks NPTP, FileI/O:
# def load_numbers(numbers, filename):
#     in_file = open(filename, "rt")
#     while True:
#         in_line = in_file.readline()
#         if not in_line:
#             break
#         in_line = in_line[:-1]
        # name, number = in_line.split(",") # double variable assignment, Toastyyyy!
#         numbers[name] = number
#     in_file.close()
#
# def save_numbers(numbers, filename):
#     out_file = open(filename, "wt")
#     for k, v in numbers.items():
#         out_file.write(k + "," + v + "\n")
#     out_file.close()

#  TODO: Load function
#  TODO: Save function
#  TODO: look into making a front end Browser UI
    # TODO: Use node and express to set up a server index.js
    # TODO: Route an index.html for Stealy Steve's Homepage
    # TODO: call to this Python script in a child process in index.js express server
    # TODO:
#  TODO: practice with git repository
        # TODO: Fillout ReadMe.md with installation instructions to run local server
#  TODO: start adding exceptions
#  start with the menu
    # try:
    #     number = int(input("Enter a number: "))
    #     print("You entered:", number)
    # except ValueError:
    #     print("That was not a number.")

# import car class
import cars
# global vehicle inventory
vehicle_inventory = {}

# define CLI menu - add, edit, remove, display
# global menu choice list
menu_choices = ["add a vehicle", "edit a vehicle", "delete a vehicle", "display vehicle inventory"]
def print_menu():
    """enumerates the list of menu choices and prints them to the screen."""
    print('--------------------------------------------------------')
    print("\n  Welcome To Stealy Steve's Corner Lot Auto Stealer!\n")
    print('--------------------------------------------------------')
    # iterate and print
    print("\n\t*-- Menu --*\n")
    for i, choice in enumerate(globals()['menu_choices']):
        print("    {}. {}\n".format(i+1,choice))
    print('\n    9. exit\n')
# TODO: define add vehicle function
def add_vehicle(_new_car):
    # add vehicle to globals inventory
    globals()['vehicle_inventory'][_new_car.vin] = _new_car
    return _new_car

# TODO: define edit vehicle function
def edit_vehicle(_vin):
    # iterate through global vehicle inventory
    for vin, vehicle in globals()['vehicle_inventory'].items():
        #  select the car in the collection with the vin that matches the input
        if vin == _vin:
            attr_2_edit = ""
            #  print the details to show the selection was found
            print("\n\t*-- Vehicle Details --*\n")
            print("{}\n".format(vehicle.get_data()))
            # prompt user for which attribute they want to edit
            attr_2_edit = input("Which attribute do you want to edit? (q to exit) ").lower()
            while attr_2_edit != "q":
                #  reset the chosen attribute with the edited input
                if attr_2_edit == "make":
                    edit = input("Edit Make: ")
                    vehicle.make = edit
                elif attr_2_edit == "model":
                    edit = input("Edit Model: ")
                    vehicle.model = edit
                elif attr_2_edit == "vin":
                    edit = input("Edit VIN: ")
                    vehicle.vin = edit
                elif attr_2_edit == "mileage":
                    edit = input("Edit Mileage: ")
                    vehicle.mileage = edit
                elif attr_2_edit == "price":
                    edit = input("Edit Price: ")
                    vehicle.price = edit
                elif attr_2_edit == "features":
                    edit = input("Edit Features: ")
                    vehicle.features = edit
                else:
                    # if user enters some nonsense
                    print("\n\tThat's not an attribute.  Try again.")
                # reprint the vehicle details from the changed global to show the mutation
                print("\t*-- Vehicle Details --*\n")
                print("{}\n".format(globals()["vehicle_inventory"][vin].get_data()))
                attr_2_edit = input("Which attribute do you want to edit? (q to exit)").lower()
                return

# TODO: define delete vehicle function
def delete_vehicle(_vin):
    dbl_check = input("Are you sure you want to delete this vehicle from the inventory? (y/n) ")
    if dbl_check == 'y':
        # iterate through global vehicle inventory
        for vin, vehicle in globals()['vehicle_inventory'].items():
            #  select the car in the collection with the vin that matches the input
            if vin == _vin:
                # delete vehicle by vin from global vehicle_inventory
                print(vin)
                del globals()["vehicle_inventory"][vin]
                return
    else:
        return

# TODO: define display vehicle function
def display_vehicle_inventory():
    """displays Stealy Steve's entire vehicle inventory."""
    for vin, vehicle in globals()["vehicle_inventory"].items():
        print("\n*-- {} --*\n{}\n".format(vin, vehicle.get_data()))


# TODO: define program loop
def main():
    # init menu loop sentinel value
    sent_val = ""
    # loop until sentinel value is given as input
    while sent_val != '9':
        # print an unwelcome message
        print_menu()
        sent_val = input("\n\tWell, what are you here for? ")
        # TODO: add a vehicle
        if sent_val == '1':
            add_vehicle(cars.Car(\
                input("Enter the vehicle make: "),
                input("Enter the vehicle model: "),
                input("Enter the vin: "),
                input("Enter the mileage: "),
                input("Enter the price of the vehicle: "),
                input("Enter any remarkable vehicle features: ")
            ))
            print("\n  Vehicle added to inventory.")

        # TODO: editing a vehicle by vin
        elif sent_val == '2':
            edit_vehicle(input("Enter the VIN of the vehicle you want to edit: "))
            print("\n  Vehicle details edited in global inventory.")

        # TODO: deleting a vehicle by vin
        elif sent_val == '3':
            delete_vehicle(input("Enter the VIN of the vehicle you want to delete: "))
            print("\n  Vehicle deleted from inventory.")

        # TODO: display the entire inventory of cars
        elif sent_val == '4':
            display_vehicle_inventory()

        # exit option
        elif sent_val == '9':
            return
        # default case if input is not a menu option
        else:
            print("\n  Perdón? That's not a menu choice. Try again.\n")

main()
