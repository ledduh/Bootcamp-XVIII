# A program that checks for missing numbers in a list
def find_missing(lst_a, lst_b):
  a = set(lst_a).union(set(lst_b))
  b = set(lst_a).intersection(set(lst_b))

  result = list(a-b)
  
  #The number which is missing is displayed in the list
  if result == []:
    return 0
  else:
    for num in result:
      return num