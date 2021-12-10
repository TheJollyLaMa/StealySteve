# https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/
import sys

print(sys.argv)
print('# Hello from python #')
print('First param: '+sys.argv[1]+'#')
print('Second param: '+sys.argv[2]+'#')


class pyNodeXfer:
    """this is a class used to transfer arguments between python and nodejs"""

    def __init__(self):
        super(pyNodeXfer, self).__init__()
        self.menu_choice = sys.argv[1]
    #
    # if sys.argv[1] == 4:
    #     print(StealySteve.display_vehicle_inventory())
    # elif sys.argv[1] == 2:
    #     print(StealySteve.edit_vehicle())
    # elif sys.argv[1] == 3:
    #     print(StealySteve.delete_vehicle())
    # elif sys.argv[1] == 4:
    #     print(StealySteve.display_vehicle_inventory())
    # elif sys.argv[1] == 5:
    #     print(StealySteve.load_vehicle_inventory())
    # elif sys.argv[1] == 6:
    #     print(StealySteve.save_vehicle_inventory())
    # elif sys.argv[1] == 9:
    #     print(StealySteve.load_vehicle_inventory())
