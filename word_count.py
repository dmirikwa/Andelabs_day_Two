def words(text):
  if(isinstance(text,str)):
    word_count={}
    word=''
    for i in text:
      if(i!=' ' and i!="\n" and i!="\t"):
        word+=i
      else:
        f=word_count.get(word,0)
        word_count[word]=f+1
        word=''
    return word_count
  else:
    raise ValueError
