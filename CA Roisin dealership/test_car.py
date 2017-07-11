import unittest

from car import Car, CarFleet, ElectricCar, PetrolCar, DieselCar, HybridCar

# test the car functionality
class TestCar(unittest.TestCase):

	def test_car_mileage(self):
		self.car = Car()
		self.assertEqual(0, self.car.getMileage())
		self.car.move(15)
		self.assertEqual(15, self.car.getMileage())
		self.car.setMileage(45)
		self.assertEqual(45, self.car.getMileage())

	def test_car_make(self):
		self.car = Car()
		self.assertEqual('', self.car.getMake())
		self.car.setMake('Ferrari')
		self.assertEqual('Ferrari', self.car.getMake())

	def test_car_colour(self):
		self.car = Car()
		self.assertEqual('', self.car.getColour())
		self.car.paint('red')
		self.assertEqual('red', self.car.getColour())
		self.car.setColour('yellow')
		self.assertEqual('yellow', self.car.getColour())

	def test_car_engine_size(self):
		self.car = Car()
		self.assertEqual('', self.car.engineSize)
		self.car.engineSize = '2.0tdi'
		self.assertEqual('2.0tdi', self.car.engineSize)

	def test_electric_car_fuel_cells(self):
		electric_car = ElectricCar()
		self.assertEqual(1, electric_car.getNumberFuelCells())
		electric_car.setNumberFuelCells(4)
		self.assertEqual(4, electric_car.getNumberFuelCells())
		
	def test_petrol_car_petrol_type(self):
		petrol_car = PetrolCar()
		self.assertEqual('', petrol_car.getFuelType())
		petrol_car.setFuelType('petrol')
		self.assertEqual('petrol',petrol_car.getFuelType())
	
	def test_diesel_car_miles_gallon(self):
		diesel_car = DieselCar()
		self.assertEqual(0, diesel_car.getMilesGallon())
		diesel_car.setMilesGallon(20)
		self.assertEqual(20, diesel_car.getMilesGallon())
	
	def test_hybrid_car_fuel_cells(self):
		hybrid_car = HybridCar()
		self.assertEqual(1, hybrid_car.getNumberFuelCells())
		hybrid_car.setNumberFuelCells(2)
		self.assertEqual(2,hybrid_car.getNumberFuelCells())
		self.assertEqual(1,hybrid_car.getNumberCylinders())
		hybrid_car.setNumberCylinders(2)
		self.assertEqual(2,hybrid_car.getNumberCylinders())

	def test_car_fleet(self):
		car_fleet = CarFleet()
		self.assertEqual(0, car_fleet.getProfit())
		self.assertEqual(40, car_fleet.getNumAvailable())
	

		car_fleet.rentCar(5)
		self.assertEqual(100, car_fleet.getProfit())
		self.assertEqual(35, car_fleet.getNumAvailable())


		car_fleet.returnCar(2)
		self.assertEqual(37, car_fleet.getNumAvailable())


		car_fleet.returnCar(3)
		self.assertEqual(40, car_fleet.getNumAvailable())

		car_fleet.returnCar(3)
		car_fleet.rentCar(50)
		
	

if __name__ == '__main__':
	unittest.main()
