weight = float(input("Weight: "))
print("1-Venus")
print("2-Mars")
print("3-Jupiter")
print("4-Saturn")
print("5-Uranus")
print("6-Neptune")
planet = int(input("Choose a planet: "))
if planet == 1:
   gravity = 0.78
   weight = weight * gravity
   print("Weight: " + weight)
elif planet == 2:
   gravity = 0.39
   weight = weight * gravity
   print("Weight: " + weight )
elif planet == 3:
   gravity = 2.65
   weight = weight * gravity
   print("Weight: " + weight )
elif planet == 4:
   gravity = 1.17
   weight = weight * gravity
   print("Weight: " + weight ) 
elif planet == 5:
   gravity = 1.05
   weight = weight * gravity
   print("Weight: " + weight )
elif planet == 6:
   gravity = 1.23
   weight = weight * gravity
   print("Weight: " + weight ) 
else:
    print("This option is not avaiable")
