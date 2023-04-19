
#Create a program called cubetask.py that takes an input the length of a cube then prints the area and also the volume.
#Have two functions called area and volume, that have the input as the argument and returns the area to be printed and the other the volume.

lgth=float(input("Enter length:  "))
def area(lgth):
    return 6*(lgth**2)


def volume(lgth):
    return lgth**3


a=area(lgth)
vol=volume(lgth)
print("The  area is:", a)
print("The volume is:", vol)


       
       
