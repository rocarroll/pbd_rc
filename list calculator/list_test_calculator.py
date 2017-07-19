## student number :  10361457, Roisin Carroll

# test calculator
# test_calculator.py

#
#
#		none work, don't understand

import unittest

from list_calculator import Calculator
calculator = Calculator()
#test the calculator functionality

class TestCalculator(unittest.TestCase):
	
	# checks adding positive, negative and fractions
	def testAdd(self):
		
		self.assertEqual([1,1,0,1,round(1/2)], calculator.add([1,0,-1,2,round(1/4)],[0,1,1,-1,round(1/4)]))
	
				
	# checks subtracting positive, negative and fractions
	def testSubtract(self):
		self.assertEqual([1,-1,-2,3,round(1/4)], calculator.subtract([1,0,-1,2,round(1/2)],[0,1,1,-1,round(1/4)]))
		
		
	# checks dividing positive, negative and fractions
	def testDivide(self):
		
		self.assertEqual ([-6,2,1,1.0], calculator.divide ([6,2,2,0.5],[-1,1,2,0.5]))
		
		
	# checks squaring positive, negative and fractions
	
	def testSquare(self):
		
		self.assertEqual([0,4,4,0.25], calculator.square([0,2,-2,0.5]))
		
		
	def testSum(self):
		
		self.assertEqual(2, calculator.sum([1,-1,1.5,0,0.5]))    
	
	def testMax(self):
		

		self.assertEqual(2, calculator.max ([2,2,2]))
		self.assertEqual(4, calculator.max ([2,1,4]))
		self.assertEqual(4, calculator.max ([4,1,2]))
		self.assertEqual(4, calculator.max ([4,1,0]))
		self.assertEqual(4, calculator.max ([4,1,-1]))
		self.assertEqual(2, calculator.max ([-2,1,2]))
	
	def testMin(self):
	
		self.assertEqual(2, calculator.min ([2,2]))
		self.assertEqual(2, calculator.min ([2,4]))
		self.assertEqual(2, calculator.min ([4,2]))
		self.assertEqual(0, calculator.min ([4,0]))
		self.assertEqual(-1, calculator.min ([4,-1]))
		self.assertEqual(-2, calculator.min ([-2,2]))
		
	def testIs_even(self):
		
		self.assertEqual([2], calculator.is_even ([2,3]))
		self.assertEqual([2], calculator.is_even ([3,2]))
		self.assertEqual([4,2], calculator.is_even ([4,2]))
		self.assertEqual([0], calculator.is_even ([3,0]))
		self.assertEqual([4], calculator.is_even ([4,-1]))
		self.assertEqual([-2], calculator.is_even ([-2,1]))

	def testIsOdd(self):
	
		#self.assertEqual([],calculator.is_odd ([2,2]))
		#self.assertEqual([], calculator.is_odd ([2,4]))
		self.assertEqual([3], calculator.is_odd ([4,3]))
		self.assertEqual([3], calculator.is_odd([3,4]))
		self.assertEqual([-1], calculator.is_odd ([4,-1]))
				
#	# checks modulo of positive, negative and fractions
	def testModulo(self):
		
		self.assertEqual([0,0,1,2,-1], calculator.modulo([0,2,1.0,6,5],[1,1,2.0,4,-6]))


		

if __name__== '__main__':
	unittest.main()