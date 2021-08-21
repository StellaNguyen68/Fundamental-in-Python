a=29.11
print(a)
print(type(a))
#take decimal from libraby
from decimal import*
getcontext().prec=3 #take max 30 number behind ,
print(Decimal(10)/Decimal(3))
print(type(Decimal(10)/Decimal(3)))

#Fraction
from fractions import*
frac=Fraction(6,9)
print(frac)
print(type(frac))
print(frac+2/3)

#Complex
c=complex(2,5)
print(c.real)
print(c.imag)
print(10/3)
print(10//3)
print(10%3) #10/3 = 3*3+"1"
print(10**3) #10^3

#String
a = '''stella'''
print(a)
b=a.capitalize() #capitalize the first letter of string
b=a.upper() #capitalize all letters of string
b=a.lower() 
b=a.swapcase() #switch from capitalizing to 
b=a.title()
b=a.center(5)
print(b)
print(a+"\n"+b)
c=a*5
print(c)

strA = "Nguyen"
strB="Stella"
strC = strB in strA # check if strB is included in strA => FALSE
print(strC)

#refer an object in string
print(strA[-1]) #refer 3rd element in strA, string index should not be out of range,
print(strA[len(strA)-1]) # refer the last element in strA
print(strA[1:len(strA)])
print(strA[1:None])
print(strA[None:None])
print(strA[None:None:2])

strD= strA[None:1] + "0" +strA[2:None]
print(strD)

from time import sleep
your_name = "Stella"
greeting="Hello! My name is "
for c in   greeting+your_name:
	print(c,end="",flush=True)
	sleep(0.05)
print()