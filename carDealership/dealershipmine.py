## car rental agency 'DBS Car Dealership'


from car import Car, ElectricCar, PetrolCar, DieselCar, HybridCar, CarFleet

print
print " 		Hi! Thanks for coming to DBS Car Dealership"
print
print " You have the option to rent any of our cars listed below. If you are a returning customer, press 'n' to get to the return car option"
print


class Dealership(object):  

	def __init__(self):
		self.electric_cars = []
		self.petrol_cars = []
		self.diesel_cars = []
		self.hybrid_cars = []
		
	# creates a stock of 40 cars   4 electric, 20 petrol, 8 diesel, 8 hybrid	
	def create_current_stock(self):
		for i in range(4):
		   self.electric_cars.append(ElectricCar())
		for i in range(20):
		   self.petrol_cars.append(PetrolCar())
		for i in range (8):
		   self.diesel_cars.append(DieselCar())
		for i in range (8):
		   self.hybrid_cars.append(HybridCar())
	
	# checks the number of cars available
	
	def stock_count(self):
		print '   petrol cars in stock:	  ' + str(len(self.petrol_cars))
		print '   electric cars in stock: 	  ' + str(len(self.electric_cars))
		print '   diesel cars in stock:	  ' + str(len(self.diesel_cars))
		print '   hybrid cars in stock:	  ' + str(len(self.hybrid_cars))
		print
		
	# rent function: user is limited to available cars only
	
	def rent(self, car_list, amount):  
		if len(car_list) < amount:
			print 'Not enough cars in stock'
			return
		total = 0
		while total < amount:
			car_list.pop()  #stack functionality, takes whatever is last on the list
			total = total + 1

	# return function updates available cars once returned. 
	def return_car(self,car_list,amount):
		total = 0
		while  total < amount:
			car_list.append(amount)
			total = total+1
			
	## attempt to calculate charge for going over mileage limit, didn't work
	#def process_mileageCharge(self, mileage, new_mileage):
	#	difference = int(new_mileage - mileage)
	#	if difference > 200:
	#		print " I'm sorry, that's over 200! We have to charge 50"
	#	else:
	#		print "Great, thanks for using our service!"
		
		
		
	# rental process - user is offered petro/diesel etc and to choose model and record mileage
	
	def process_rental(self):
		answer = str.lower(raw_input('  Would you like to rent a car? Yes: "Y", No: "N" : '))
		if answer == 'y':
			answer = str.lower(raw_input('  Choose "p" for Petrol, "d" for Diesel, "e" for electric and "h" for Hybrid:   '))
			amount = int(raw_input('   How many would you like?  '))
			if answer == 'p':
				self.rent(self.petrol_cars, amount)
				choice = raw_input('   Write the model you would like: Toyota, Kia, Volkswagon, Ford:    ')
				petrol_car = PetrolCar()
				petrol_car.setMake(choice)
				mileage = int(raw_input('   Record the mileage here before you start driving. '))
				petrol_car.setMileage(mileage)
				print 'Your car is: ', petrol_car.getMake()
				print 'The current mileage is set at: ',  petrol_car.getMileage()
				
				
			elif answer == 'd':
				self.rent(self.diesel_cars, amount)
				choice = raw_input('   Write the model you would like: Nissan or Hyundai:  ')
				diesel_car = DieselCar()
				diesel_car.setMake(choice)
				mileage = int(raw_input('   Record the mileage here before you start driving. '))
				diesel_car.setMileage(mileage)
				print 'Your car is: ', diesel_car.getMake()
				print 'The current mileage is set at: ',  diesel_car.getMileage()
				
				
			elif answer == 'e':
				self.rent(self.electric_cars, amount)
				choice = raw_input('   We have a Nissan or a Tesla, please write your choice:   ')
				electric_car = ElectricCar()
				electric_car.setMake(choice)
				mileage = int(raw_input('   Record your mileage here before you start driving. '))
				electric_car.setMileage(mileage)
				print 'Your model is', electric_car.getMake()
				print 'Fuel cells available are', electric_car.getNumberFuelCells()
				print 'Your current mileage is set to:  ', electric.car.getMileage()
			
			else:
				self.rent(self.hybrid_cars,amount)			
				choice = raw_input(' what hybrid do you want, Prius or Lexus?  ')
				hybrid_car = HybridCar()
				hybrid_car.setMake(choice)
				mileage = int(raw_input('   Record your mileage here before you start driving.  '))
				hybrid_car.setMileage(mileage)
				print 'Your model is', hybrid_car.getMake()
				print 'Our hybrid cars come with :', hybrid_car.getNumberFuelCells(), 'fuel cells and ', hybrid_car.getNumberCylinders(), 'cylinders '
				print 'Your current mileage is set to:  ', hybrid_car.getMileage()
			car_fleet = CarFleet()
			car_fleet.rentCar(amount)
		if answer == 'n':
			self.process_returnCar()
		self.stock_count()
	

			
	# user inputs how many cars they are returning and type
	
	def process_returnCar(self):
		answer = raw_input('   would you like to return a car? Yes: "Y", No: "N" : ')
		if answer == 'y':
			answer = raw_input('   what car are you returning? Petrol: "p" , Electric: "e" , Diesel: "d" , Hybrid: "h"  : ')
			amount = int(raw_input('   how many are you returning?  '))
			#new_mileage = int(raw_input('  what is the new mileage on your car: '))
			#self.process_mileageCharge(self.process_rental,new_mileage)
			if answer == 'p':
				self.return_car(self.petrol_cars, amount)
			elif answer == 'e':
				self.return_car(self.electric_cars, amount)
			elif answer == 'h':
				self.return_car(self.hybrid_cars,amount)			
			else:
				self.return_car(self.diesel_cars, amount)
			car_fleet = CarFleet()
			car_fleet.returnCar(amount)
			
		if answer == 'n':
			self.process_rental()
		self.stock_count()
	
	
		
	
	
	

		
	
dealership = Dealership()
dealership.create_current_stock()
dealership.stock_count()



proceed = 'y'
while proceed == 'y':
	dealership.process_rental()
	dealership.process_returnCar()
	proceed = raw_input('continue? y/n')
	
