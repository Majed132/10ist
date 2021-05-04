# program to calculate area of square




# import librairies

import math

#define functions

def areaofsquare(L):
    area = L * L
    print("returning area to main program")
    return(area)

# main program

length = float(input("what is the length of the square in cm? "))
print("Radius is ", length, "cm")
print("area is equal to",areaofsquare(length), "cm2")
