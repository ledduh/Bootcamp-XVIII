#A class BinarySearch is defined 
class BinarySearch(list):

  def __init__(self, a, b):
    self.a = a
    self.b = b
    lst = [x for x in range (b, a+1, b)]
    self.length = len(lst)
  '''
  A function search checks for items in a list.
  '''  
  def search(self,x):
    mylist = self.lst
    first = 0
    last = self.length -1
    mydictionary = {}
    count =0
    while first<last:
      count = count+1
      '''
      if the first is equal to the last value it returns -1
      '''
      if first == last:
        return -1
      middle =(first+last)//2
      middle_item = mylist[middle]
      '''
      if there is a middle value it is updated to the list
      '''
      if middle_item == x:
        mydictionary ['count'] = count
        mydictionary ['index'] = middle
        return mydictionary
      else:  
        if middle_item < x:
          first = middle + 1
        else:
          last = middle 

