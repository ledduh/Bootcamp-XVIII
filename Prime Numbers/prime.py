def prime_digit(number): #defines the function with a parameter of a number

  prime_numbers = [] 
  if isinstance (number, int): #a condition where the value being input is an integer
    if number>1: #this block sets a condition that if a number is greater than 1 for numbers in the range which begins with 2 it will be divided to find out whether it is a prime number
      for num in range (2, number+1):
        for i in range (2, num):
          if (num%i==0): 
            break #stops the loop from continuing looping infinately 
        else:
          prime_numbers.append(num) #the number is updated if it satisfies the condition
      return prime_numbers #it gives output of the prime number achieved
    else:
      raise ValueError ('Please input a positive integer') #program raises an error if the input is not a positive number
  else:
    raise TypeError ('please input an integer') #program raises and error if the input typed is not an integer
