def Car(self):
	def __init__( self, name='General', model = 'GM', car_type= None, speed = 0):#function is initialized
		self.name=name
		self.model = model
		self.speed = speed
		self.Car_type = Car_type

		if self.name == 'Toyota' or self.name=='Rover': #if the  car name is toyota or rover it has 2 doors
			self.num_of_doors = 2
		else:
			self.num_of_doors = 4 #Other cars have four doors

			if self.car_type =='trailer': #if the car type is a trailer it has 8 wheels
				self.num_of_wheels = 8
			else:
				self.num_of_wheels = 4 #other car types have 4 wheels

				def is_saloon(self): #A function is defined to check whether it is a trailer or a saloon
					if self.car_type != 'trailer':
						self.car_type == 'saloon'
						return True
					else:
						return False

						def drive (self,moving_speed): # A function is defined to check if a car is a trailer it should be moving at a speed of 77
							if self.car_type =='trailer':
								self.speed = 77
							else:
								pass

								if self.name=='Mercedes':
									self.speed = 10**moving_speed
								else:
									pass
									return self