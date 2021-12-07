# TODO: define car class - make, model, vin, mileage, price, features [dict]
class Car:
    """This is a class defining what a Car is to Stealy Steve."""

    def __init__(self, make, model, vin, mileage, price, features):
        super(Car, self).__init__()
        self.make = make
        self.model = model
        self.vin = vin
        self.mileage = mileage
        self.price = price
        #  TODO: features should be a dictionary
        self.features = features

    def get_data(self):
        """This is a function to return the data about a Car in a formatted string."""
        return "Make: {}\nModel: {}\nVIN: {}\nMileage: {}\nPrice: {}\nFeatures: {}"\
            .format(self.make,self.model,self.vin,self.mileage,self.price,self.features)

    # def add_feature(self, args*):
    #     for each in args*:
    #         self.features[i] = args[i]
