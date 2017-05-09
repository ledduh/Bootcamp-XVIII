def data_type(x):
	if isinstance (x, basestring): #condition checks to see in the instance given is a string or unicode 
		return len(x) #it returns the lenght of the given input
	elif isinstance (x, bool): #if the instance given is a bool it returns it 
		return x
	elif x is None: #if the value of x is none it returns no value
		return 'no value'
	elif isinstance (x, int): #if the instance given is an integer and the value is less than 100 it returns less than 100
		if x<100:
			return 'less than 100'
		elif x==100: # if the value is 100 it returns equal to 100
			return 'equal to 100'
		else:
			return 'more than 100'
		if isinstance (x, list): #if the instance given is a list and the list is less than 3 it returns none
			if len(x)<3:
				return None
			else:
				return x[2]
			