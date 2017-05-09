 #A function fizz_buzz is defined which has a parameter of a number
def fizz_buzz(number):
	#A condition is set if the number is divisible by both 5 & 3 it should return FizzBuzz
	if number%5==0 and number%3==0: 
		return 'FizzBuzz'
	#if the number is divisible by 3 it returns Fizz
	elif number%3==0: 
		return 'Fizz'
	#If the number is divisible by 5 it returns buzz
	elif number%5==0: 
		return 'Buzz'
	#The function should return the number if it does not meet any of the conditions
	else:
		return number 

