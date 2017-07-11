# Define a class for my car

class Car(object):
    # implement the car object.
    
    def __init__(self):
        self.__colour = ''
        self.__make = ''
        self.__mileage = 0
        self.engineSize = ''
	
	# functions allow user to change mileage, make etc
    def getColour(self):
        return self.__colour

    def getMake(self):
        return self.__make

    def getMileage(self):
        return self.__mileage

    def setColour(self, colour):
        self.__colour = colour

    def setMake(self, make):
        self.__make = make

    def setMileage(self, mileage):
        self.__mileage = mileage

    def paint(self, colour):
        self.__colour = colour
        return self.__colour

    def move(self, distance):
        self.__mileage = self.__mileage + distance
        return self.__mileage

	# records fuel cells for electric cars
class ElectricCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 1

    def getNumberFuelCells(self):
        return self.__numberFuelCells

    def setNumberFuelCells (self, numberFuelCells):
        self.__numberFuelCells = numberFuelCells

	# records fuel type for petrol	
class PetrolCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__fuelType = ''

    def getFuelType(self):
        return self.__fuelType

    def setFuelType(self, fuelType):
        self.__fuelType = fuelType
		
	# records miles per gallon for diesel cars
class DieselCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__milesGallon = 0
 
    def getMilesGallon(self):
        return self.__milesGallon
	
    def setMilesGallon(self, milesGallon):
        self.__milesGallon = milesGallon
	
	# uses both fuelcells and cylinders
class HybridCar(Car):
    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 1
        self.__numberCylinders = 1
		
    def getNumberFuelCells(self):
        return self.__numberFuelCells

    def setNumberFuelCells (self, numberFuelCells):
        self.__numberFuelCells = numberFuelCells

    def getNumberCylinders(self):
        return self.__numberCylinders

    def setNumberCylinders(self, numberCylinders):
        self.__numberCylinders = numberCylinders
		
	# calculates profit at 20 euro per car
class CarFleet(object):

    def __init__(self):
        self.__cars = []
        self.__numAvailable = 40
        self.__profit = 0.0
		
    def getProfit(self):
        return self.__profit

    def getNumAvailable(self):
        return self.__numAvailable

    def rentCar(self, numCars):
        self.__numAvailable -= numCars
        self.__profit += (numCars * 20)
        print('Charge ' + str(self.__profit))
        print('Available ' + str(self.__numAvailable))

    def returnCar(self, numCars):
        self.__numAvailable += numCars
        #print('Available ' + str(self.__numAvailable))
		
        
        
        
        
        
        
        


        
