class Car(object):

    #function is initialized
	def __init__( self, name='General', model = 'GM', car_type='saloon', speed = 0):
		self.name=name
		self.model = model
		self.speed = speed
		self.car_type = car_type
        
        #if the  car name is toyota or rover it has 2 doors
		if self.name == 'Porsche' or self.name=='Koenigsegg': 
			self.num_of_doors = 2
		else:
			self.num_of_doors = 4 #Other cars have four doors
		#if the car type is a trailer it has 8 wheels
			
		if self.car_type =='trailer': 
			self.num_of_wheels = 8
		else:
			#other car types have 4 wheels
			self.num_of_wheels = 4 

	#A function is defined to check whether it is a trailer or a saloon
	def is_saloon(self): 
		if self.car_type is not 'trailer':
			self.car_type == 'saloon'
			return True
		else:
			return False

	def drive (self,speed):
		'''
		 A function is defined to check if a car is a trailer it should be moving at a speed of 77
		 '''
		if self.car_type =='trailer':
			return 77
		else:
			return 10 * speed
			