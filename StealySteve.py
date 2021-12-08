import os # just for SEEK_SET to search inventory file for duplicate
import json
# car class - make, model, vin, mileage, price, features [dict]

class Car:
    """This is a class defining what a Car is to Stealy Steve."""
    # global vehicle inventory

    def __init__(self, make, model, vin, mileage, price, features):
        super(Car, self).__init__()
        self.make = make
        self.model = model
        self.vin = vin
        self.mileage = mileage
        self.price = price
        # TODO: features should be a dictionary
        self.features = features

    def get_data(self):
        """This is a function to return the data about a Car in a formatted string."""
        return "Make: {}\nModel: {}\nVIN: {}\nMileage: {}\nPrice: {}\nFeatures: {}"\
            .format(self.make,self.model,self.vin,self.mileage,self.price,self.features)

vehicle_inventory = {}
data_path = 'data/'
default_data_file = "Main_and_West.json"
# create data path if none
if not os.path.exists(data_path):
    os.makedirs(data_path)
# define CLI menu - add, edit, remove, display
# global menu choice list
menu_choices = ["add a vehicle", "edit a vehicle", "delete a vehicle", "display vehicle inventory","load inventory","save inventory"]
def print_menu():
    """enumerates the list of menu choices and prints them to the screen."""
    print('🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁')
    print("\n\t  Welcome To Stealy Steve's Corner Lot Auto Stealer!\n")
    print("🚙 🚙 🚙 🚙 🚙 🚙 🚙 🚙 🚙 🚙 🚙 🚙 🚙 🚙 🚙 🚙 🚙 🚙 🚙 🚙 🚙 🚙 🚙")
    print('🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁')
    # iterate and print
    print("\n\t____🚙__ Menu __🚙____\n")
    for i, choice in enumerate(globals()['menu_choices']):
        print("    🚩{}. {}\n".format(i+1,choice))
    print('\n    🚩9. exit\n')
# define add vehicle function
def add_vehicle(_new_car):
    """... adds the vehicle as a new Car object"""
    # add vehicle to globals inventory
    globals()['vehicle_inventory'][_new_car.vin] = _new_car
    return _new_car

# define edit vehicle function
def edit_vehicle(_vin):
    """... edits the vehicle of the VIN input"""
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

# define delete vehicle function
def delete_vehicle(_vin):
    """... deletes the vehicle of the VIN input"""
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

# define display vehicle function
def display_vehicle_inventory():
    """displays Stealy Steve's entire vehicle inventory."""
    inventory = globals()["vehicle_inventory"]
    print("\n\t\t🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁")
    print("\t\t🚙          Vehicle Inventory       🚙")
    print("\t\t🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁\n")
    if (inventory.keys()):
        # for every car in inventory
        for vin in inventory.keys():
            print("\n\t__🚙 ",vin," 🚙__\n")
            vehicle = inventory[vin].__dict__
            # for every attribute belonging to a car
            for attribute in vehicle.keys():
                # handle the features dictionary
                if type(vehicle[attribute]) is dict:
                    print("\t{}:".format(attribute))
                    for feature in vehicle[attribute].keys():
                        # print(type(vehicle[attribute][feature]))
                        if isinstance(vehicle[attribute][feature], list):
                            print("\t    {}: ".format(feature), end='')
                            for cat in vehicle[attribute][feature]:
                                print(" ", cat, ",", end='')
                            print()
                        else:
                            print("\t    {} : {}".format(feature, vehicle[attribute][feature]))

                else:
                    print("\t{}\t:   {}".format(attribute, vehicle[attribute]))
            print()
    else:
        print("\n\t🚫 No vehicles to display! Load a data file ... 🚫\n")
    print("\n\t\t🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁")
    print("\t\t🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁\n")
    print(" 🚙 Remember to save local inventory to data file before exiting!🚙")

#  Load Vehicle Inventory
# makes use of the 'Walrus :=  ' operator
# -https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list
# and the docs: https://docs.python.org/3/whatsnew/3.8.html#assignment-expressions
# TODO: Finish load function
def load_vehicle_inventory():
    """loads a data file into the Stealy Steve Program's inventory"""
    #  check for data path
    data_file = str(input("\tWhat is the name of the inventory lot you are at?(Main_and_West)")) #default to Stealy's Main lot
    data_file = data_path + data_file + ".json"

    # check if user input file is in data path and if not, set data to default
    if not os.path.exists(data_file):
        print("\n\t🚫 Uhoh! Looks like Stealy Steve had to trash that record when the Feds came! 🚫")
        data_file = data_path + default_data_file
    # make a file if none
    with open(data_file, "a+") as f:
        f.seek(0)
        while (l := f.readline().rstrip()):
            print("\n",l)
            try:
                make, model, vin, mileage, price, features = l.split(",") # multiple variable assignment, Toastyyyy!
            except:
                print("failed multi-variable split string assignment")

            globals()["vehicle_inventory"][vin] = {'make':make, 'model': model, 'vin': vin, 'mileage': mileage, 'price': price, 'features': features}
        print("\n\t✅ We've loaded the data from the lot on site  ...✅\n")
        print()
# Save to file
def save_vehicle_inventory():
    """saves newly added inventory to a data file"""
    #  check for data path
    data_file = str(input("\tWhat is the name of the inventory lot you are at?(Main_and_West)")) #default to Stealy's Main lot
    if (data_file == ''):
        data_file = data_path + default_data_file
    else:  #go to default if no file is given by the user
        data_file = data_path + data_file + ".json"
    # print("\n\tData File: ",data_file)
    inventory = globals()["vehicle_inventory"]
    if (inventory.keys()):
        with open(data_file, "a+") as f:
            # for/else statement
            # https://stackoverflow.com/questions/28385337/python-open-a-file-search-then-append-if-not-exist
            # print(inventory.keys())
            for vin in inventory.keys():
                # print("line: ")
                f.seek(0, os.SEEK_SET)
                for line in f:
                    # print("line: ")
                    # print(json.loads(line))
                    if vin in line:
                        print("\n\t🚨 That {} is already in the date file! skipping it ... 🚨".format(inventory[vin].make))
                        break
                else:
                    f.write(json.dumps(inventory[vin].__dict__))
                    f.write("\n")


        print("\n\t✅ Saved local inventory to {} ✅".format(data_file))

    else:
        print("\n\t🚨 There is no new inventory in local memory to save...🚨 ")
        print("\n\t   Try adding a car...")

# for vin, vehicle in globals()["vehicle_inventory"].keys():
#     f.write(json.dumps( globals()["vehicle_inventory"].__dict__[vin][vehicle] ))
