#Prob4
#finding the volume of a cone

import math 
def cone_vol(radius, height):
    return (1/3)* math.pi*(radius ** 2) * height 

radius = float(input("enter the radius of the cone: "))
height = float(input("enter the height of the cone: "))

volume = cone_vol(radius, height)
print(f"The volume of the cone is: {volume:.2f} cubic units")