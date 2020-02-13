def multiplicationTable(a,b,c,d):
  width = len(str(d)) 
  
  for i in range(0,b-a+2):
    w1 = len(str(a+i-1))
    w2 = len(str(d * (a+i-1))) + 1
    all_wi = w2-w1
    if i == 0:
      print(" "*width,end="")
    elif (i == (b-a+1)):
      print(" "*all_wi+'{}'.format(a+i-1))
    else:
      print(" "*all_wi+'{}'.format(a+i-1),end="")

  
  for i in range(0,d-c+1):
    for j in range(0,b-a+1):
      w = len(str(d * (a+j)))+1
      if (j == 0):
        print('{:{}}'.format(c+i,len(str(c+1))),end="")
      if (j == b-a):
        print('{:{}}'.format((c+i)*b,w))
      else:
        print('{:{}}'.format((c+i)*(a+j),w),end="")

if __name__ == "__main__":
   multiplicationTable(1,10,11,20)
   print()
   multiplicationTable(101,110,921,930)
