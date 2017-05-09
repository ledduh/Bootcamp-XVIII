def data_type(data):
	#condition checks to see in the instance given is a string
	if isinstance (data, str):  
	#it returns the lenght of the given input
		return len(data) 
    #if the instance given is a bool it returns the data 
	elif isinstance (data, bool): 
		return data
	#if the value of x is none it returns no value
	elif data is None: 
		return 'no value'
	'''
	if the instance given is an integer and the value is less than 100 it returns less than 100
	'''
	elif isinstance (data, int): 
		if data<100:
			return 'less than 100'
	# if the value is 100 it returns equal to 100
		elif data==100: 
			return 'equal to 100'
		else:
			return 'more than 100'
	'''
	if the instance given is a list and the list is less than 3 it returns none
	'''
	elif isinstance (data, list): 
		if len(data)<3:
			return None
		else:

			return data[2]
			
print(data_type([1,2]))