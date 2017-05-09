def fizz_buzz(number): #A function fizz_buzz is defined which has a parameter of a number
	if number%5==0 and number%3==0: #A condition is set if the number is divisible by both 5 & 3 it should return FizzBuzz
		return 'FizzBuzz'
	elif number%3==0 and number%5!=0: #if the number is divisible by 3 and not 5 it returns Fizz
		return 'Fizz'
	elif number%5==0 and number%3 !=0: #If the number is divisible by 5 and not 3 it returns buzz
		return 'Buzz'
	else:
		return number #The function should return the number if it does not meet any of the conditions
