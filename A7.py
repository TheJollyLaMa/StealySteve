# for final addition-
#     TODO: Learning goal: get familiar with and attempt to deploy with Cyclic
#     TODO: Learning goal: practice with git
#     Use node and express to set up a server index.js - ::: with CYCLIC :::
#     Route an index.html for Stealy Steve's Homepage
#     call to this Python script in a child process in index.js express server
#     TODO: OBJECTIVE: Call Stealy Steve's main menu and demonstrate the power and proof of concept of
#                      (Node & Python) + (Git & Cyclic) by linking the 'Display Inventory' function
#     Route the remaining functioning
#         Add, Edit, Delete, Search, Save, Load forms to pass to this Python backend
#         Fillout ReadMe.md with installation instructions to run local server

# import car class
import sys # get the sys.argv
import StealySteve as StealySteve
# print(sys.argv)
# print('# Hello from python #')
# print('First param: '+sys.argv[1]+'#')
# print('Second param: '+sys.argv[2]+'#')
web_sent_val = sys.argv[1]
sent_val = '0'
print(web_sent_val)
#
# define program loop
def main():
    """... Stealy Steve's main loop prints a menu and calls the necessary functionality for Stealy Steve to run his shady car lot."""
    # init menu loop sentinel value
    # this would be an entry point for the node app I do believe ....
    # TODO: sent_val = sys.argv[1]   - first argument put into the call to the script will be the menu option
    # TODO: prototype menu option "4", display vehicles, with node through Cyclic .
    # This would be a reasonable stopping point and a good enough proof of concept for me :)
    # loop until sentinel value is given as input
    while sent_val != '9' or web_sent_val != '9':
        # print an unwelcome message
        StealySteve.print_menu()
        sent_val = input("\n\tWell, what are you here for❓ ")
        # add a vehicle
        if sent_val == '1':
            # StealySteve.add_vehicle(StealySteve.Car(\
            #     input("Enter the vehicle make: "),
            #     input("Enter the vehicle model: "),
            #     input("Enter the vin: "),
            #     input("Enter the mileage: "),
            #     input("Enter the price of the vehicle: "),
            #     input("Enter any remarkable vehicle features: ")
            # ))
            StealySteve.add_vehicle(StealySteve.Car(\
                "Mercedes-Benz", "190E", "Asdlkfjqrefvc09wrjgvlakjej905",\
                 "120000", "3000", {"interior":["Bumpin Stereo", "leather interior", "moon roof"], 'exterior':[ "custom rims","T-Jack"]}))
            print("\n\t✅ Vehicle added to inventory. ✅\n")

        # edit a vehicle by vin
        elif sent_val == '2':
            StealySteve.edit_vehicle(input("Enter the VIN of the vehicle you want to edit: "))
            print("\n\t✅ Vehicle details edited in global inventory. ✅\n")

        # delete a vehicle by vin
        elif sent_val == '3':
            StealySteve.delete_vehicle(input("Enter the VIN of the vehicle you want to delete: "))
            print("\n\t✅ Vehicle deleted from inventory. ✅\n")

        # display the entire inventory of cars
        elif sent_val == '4' or web_sent_val == '4':
            StealySteve.display_vehicle_inventory()

        #  TODO: Load function
        elif sent_val == '5':
            StealySteve.load_vehicle_inventory()
            pass
        # Save function
        elif sent_val == '6':
            StealySteve.save_vehicle_inventory()
            pass
        # exit option
        elif sent_val == '9':
            return
        # default case if input is not a menu option
        else:
            print("\n  Perdón⁉️  That's not a menu choice. Try again.\n")

# main()
