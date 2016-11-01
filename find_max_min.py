def find_max_min(mylist):
  if(isinstance(mylist,list)):
    minn=mylist[0]
    maxx=mylist[0]
    for i in mylist:
      if(isinstance(i,int) or isinstance(i,float)):
        if(i<=minn):
          minn=i
        if(i>=maxx):
          maxx=i
      else:
        raise ValueError
    if(maxx==minn):
      return [len(mylist)]
    else:
      return [minn,maxx]
  else:
    raise ValueError
