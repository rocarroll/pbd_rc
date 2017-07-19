# calculator.py
#
#
## This program works as a calculator
# 10361457 student number
# Roisin Carroll

## notes: I went down the wrong path: using lambda means I don't have to do def. 
## My tests won't work with below. I think it's because it's testing against the lambda 
## When I change the test functions from add to the lambda sequence it also fails: too many variables
## if I write it with only lambda, no function, I can't reference it for tests...lost

import string

class Calculator(object):
		
	
	def add(self,first, second):    
		return map(lambda x,y: x+y, first, second)

	def subtract(self,first,second):
		return map(lambda x,y: x-y, first, second)
		
	def divide(self,first,second):
		return map(lambda x,y: float(x)/float(y), first, second)
		
	def square(self,first):	
		return map(lambda x: x**2, first)
		
	def sum(self,first):
		return reduce(lambda x,y: (x+y), first)

	def max(self,first):
		return reduce(lambda a,b: a if (a>b) else b, first) 

	def min(self,first):
		return reduce(lambda a,b: a if (a<b) else b, first) 

	def is_even(self,first):
		return filter(lambda x: x%2==0, first)
	
	def is_odd(self,first):
		return filter(lambda x: x%2, first)

	def greater_than_mean(self,first):
		mean = sum(first)/len(first)
		return filter(lambda x: x>mean, first)
	
	def modulo(self,first,second):
		return map(lambda x,y: x%y, first,second)


	

		
calculator = Calculator()
first = input("enter the first group of numbers as a list ie 1,2,3:	")
second = input("enter the second group of numbers as as list ie 2,3,4:	")

# where first and second are listed the calculation is done on both lists of numbers
# where first only is mentioned, the calculation is done on the first list of user input only. 
print "This adds two lists ",calculator.add(first,second)   
print "This subtracts first list and second", calculator.subtract(first,second)
print "This divides first list by second", calculator.divide(first,second)
print "This squares numbers in first list", calculator.square(first)
print "This sums the first list ", calculator.sum(first)
print "This gets the max of the first list ", calculator.max(first)
print "This gets the min of the first list ", calculator.min(first)
print "This gets the even in first list", calculator.is_even(first)
print "This gets the odd in first list", calculator.is_odd(first)
print "This gets the greater than mean of first list only", calculator.greater_than_mean(first)
print "This gets the modulo of the two lists", calculator.modulo(first,second)

#list comprehension:

values = [1,2,3]
print 'values are ', values

# gets the length of the list and calculates the mean
n = len(values)
mean = sum(values)/float(n)
print 'mean is: ', mean

# gets the sum of square deviations by squaring and then adding each value
ss = sum((x-float(mean))**2 for x in values)
print ' sum of square deviations of a sequence', ss

# gets the standard deviation of a population 
stdev = ss/(n**0.5)
print 'the standard deviation for a population is ', stdev

# gets the standard deviation of a sample by subtracting n-1
n = 2
print 'new n is ', n
stdevsamp = ss/(n**0.5)
print 'the standard deviation for a sample is', stdevsamp
