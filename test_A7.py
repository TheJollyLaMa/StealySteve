# python3 -m unittest test_A7
# practicing classes with a Test Class
import unittest
import cars
import A7
#  TODO: define unit tests
class TestStealySteve(unittest.TestCase):
    """This is the Unit Test Class for the car dealer program. "Each unit test should be designed to verify that the behaviour of our class is correct when a specific sequence of events occurs. As part of each unit test you provide a set of inputs and then verify the output is the same you expected using the concept of assertions." - The CodeFather """
    def test_print_menu(self):
        # Test for proper menu
        # not sure how to do that ...
        # test if string printed at global menu is the same as a local instance of that menu stringified?
        pass

    def test_add_vehicle(self):
        """tests the add_vehicle function of Stealy Steve's Car Stealer inventory program"""
        # the program should be able to add vehicles
        # Stealy Steve needs some junkers in his lot. Let's take a trip down memory lane ...
        # She's not much to look at, but she hauls like a cement truck on a new airport runway!
        new_car1 = cars.Car(\
            "Chevrolet", "Cheyenne", "Craaslkfjaskdjvakjfvadsff1234",\
             "180000", "3000", "Sweet Bed, Bumpin Stereo, and a dent in the quarter panel")
        # Picked up in manhattan on an ebay deal before the towers fell, this 190E has a long body for easy highway cruising
        new_car2 = cars.Car(\
            "Mercedes-Benz", "190E", "Asdlkfjqrefvc09wrjgvlakjej905",\
             "120000", "3000", "T-Jack, Bumpin Stereo, custom rims, leather interior, moon roof")
        # It's no prize, and it's the color of a turd - but it's got Spirit Baby! Until the gastank fell out on the highway coming home from work...
        new_car3 = cars.Car(\
             "Dodge", "Spirit", "hgjfhdtrsnbfmwreyw64u75imjdgf",\
              "210000", "500", "ashtray in the floor board")
         # Bought in Germany with an Austrian Custom's stamp, this Rallye Edition can race the autobahn or romp through any cornfield!
        new_car4 = cars.Car(\
             "Jeep", "Compass", "23krjnlfugh3958hgsdvkbdf8ygsg",\
              "8", "28000", "Rallye Edition, TCS")
        new_cars = [new_car1,new_car2,new_car3,new_car4]
        # add vehicles & check global inventory variable
        print("\n\t\t  *------ Test Report ------*\n")
        print("\t*Original*\t\t\t  *Global Test Assignment*  ")
        # iterate the list
        for vehicle in new_cars:
            # add_vehicle should return the vehicle added
            self.assertEqual(A6.add_vehicle(vehicle), vehicle, "should be able to add a vehicle.")
            # the vehicle added should be added to the global assignment of the vehicle_inventory dictionary
            self.assertEqual(A6.vehicle_inventory[vehicle.vin].vin, vehicle.vin, "should add the vehicle object to global inventory collection.")
            # print(vehicle.get_data())
            # compare local test instance to global assignment
            print("\n{}\t\t{}\n".format(vehicle.get_data().split("VIN: ")[1].split("\n")[0], A6.vehicle_inventory[vehicle.vin].vin))
        # no need for all this ... it's the long form of the above
        # self.assertEqual(A6.add_vehicle(new_car2), new_car2, "should be able to add a second vehicle.")
        # self.assertEqual(A6.add_vehicle(new_car3), new_car3, "should be able to add multiple vehicles.")
        # self.assertEqual(A6.add_vehicle(new_car4), new_car4, "should be able to add multiple vehicles.")
        # to the global inventory collection
        # self.assertEqual(A6.vehicle_inventory[new_car2.vin], new_car2, "should add the second vehicle object to global inventory collection.")
        # self.assertEqual(A6.vehicle_inventory[new_car3.vin], new_car3, "should add the third vehicle object to global inventory collection.")
        # self.assertEqual(A6.vehicle_inventory[new_car4.vin], new_car4, "should add the fourth vehicle object to global inventory collection.")
        # print("\n", new_car1.get_data())
        # print("\n", new_car2.get_data())
        # print("\n", new_car3.get_data())
        # print("\n", new_car4.get_data())

    def test_edit_vehicle(self):
        # TODO: the program should be able to edit a vehicle's properties
        #
        pass

    def test_delete_vehicle(self):
        # TODO: the program should be able to delete a vehicle
        #
        pass

    def test_display(self):
        # TODO: the program should display the vehicle inventory
        #
        pass


# after all this I'm wondering .... just where does the TestStealySteve class get called?
# from unittest somehome I'm guessing? googled it ...
# CodeFather. (2021). How To Write A Unit Test In Python. https://codefather.tech/blog/write-unit-test-python/
# Aha! The above test class inherits unittest.TestCase! of course...
# and as per the CodeFather, we can add an entry point to execute the tests from the command line using unittest.main.
# "The value of __name__ is checked when you execute the test_user.py file via the command line with the below condition."
if __name__ == '__main__':
    print("\n*--What's it about?\n")
    help(TestStealySteve.__doc__)
    unittest.main()
# now just run the file from the command line to test.
# python3 test_A6.py

# either way, the unittest.Testcase is getting passed in to my custom tests
# but..
# Q: what is happening in there that makes it run through all my test methods in my custom test class?
