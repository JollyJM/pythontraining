mynum1=float(input("Enter input one to test: "))
mynum2=float(input("Enter input two to test: "))
mynum3=float(input("Enter input three to test: "))

if (mynum1>mynum2) and (mynum1>mynum3):
    print("mynum1")
elif (mynum2>mynum1) and (mynum2>mynum3):
    print("mynum2")
elif (mynum3>mynum1) and (mynum3>mynum2):
    print("mynum3")
else:
    print("Equal")

