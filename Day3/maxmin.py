'''
Function find_max_min  is defined to find the maximum and minimum numbers in a list
'''
def find_max_min(numbers):
	my_maximum_and_minimum=[]
	maximum_number= max(numbers)
	mininumu_number = min(numbers)
	'''
    if the maximum numbers are equal to the minimum numbers
    updates the length of the numbers 
	'''
	if maximum_numbers==minimum_numbers:
		my_maximum_and_mininim.append(len(numbers))
  	else:
  	
  	#if the maximum and minimum numbers are nnot equal it updates
	#list with the maximum and minimum number then returns the updated list.
	
    

  		my_maximum_and_minimum.append(minimum_number)
  		my_maximum_and_minimum.append(maximum_number)
  	return my_maximum_and_minimum
