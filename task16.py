basic=float(input("Enter your basic salary: "))
benefits=float(input("Enter your benefits: "))
gross=basic+benefits
if (gross<18000):
    nssf=0.06*gross
    print(nssf)
else:
    nssf=1080
    print(nssf)
nssf1=nssf*2
print(nssf1)