x=int(input("inter a solar year:"))
if x<=0:
 print("you intered a wrong date")
else:
 print("Gregorian year is equal to:",x+621)
 b=int(input("Do you want to convert a Gregorian year to solar year? 0.No  1.yes   "))
 if b==1:
  z=int(input("inter a Gregorian year:"))
  if z<=621:
   print("you intered a wrong date")
  else:
   print("Solar year is equal to:",z-621)
 if b==0:
   print("Goodbye") 
 if b>1 or b<0: 
  print("you intered a wrong response")

