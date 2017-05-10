#Function words is defined
def words(sentence):
  '''
  myword_list is given the value sentence.split which splits the sentence
  '''
  myword_list = sentence.split()
  newlist=[]
  mywords={}
  for word in myword_list:
  
    if word.isdigit():
      word = int(word)
      newlist.append(word)
    else:
      '''
      if the input is not an integer the input is still updated to the list as it is.
      '''
      newlist.append(word)
  
  for word in newlist:
    '''
    for all the words in the newlist it updates the words in the list 
    if there is any addition but if not it returns the current lust
    '''
    if word in mywords:
      mywords[word]=mywords[word]+1
    else:
      mywords[word]=1
  return  mywords
