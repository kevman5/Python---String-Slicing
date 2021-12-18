# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 19:15:54 2021

@author: kevmm
"""

import math


#phonenumber = (316)-222-3333
#              01234567891011121314
#              0      -      14
PhoneNumber = input("Enter Phone Number (Must be in (316)222-3333 Format!!): ")
firstp = PhoneNumber.index("(")
secondp = PhoneNumber.index(")")
firstdash = PhoneNumber.index("-")
print(firstp, secondp, firstdash)
StrippedPhoneNumber = PhoneNumber[firstp+1:secondp] + PhoneNumber[secondp+1:firstdash] + PhoneNumber[firstdash+1:len(PhoneNumber)]
print("The Stripped Phone Number: ", StrippedPhoneNumber)

#CSV Format = 3,5,7.2,David

CSVInput = input("Enter Your Last Name, First Name, Age, Favorite Color and Lucky Number: ")
LNcomma = CSVInput.index(",")
FNcomma = CSVInput.index(",", LNcomma + 1)
Agecomma = CSVInput.index(",", FNcomma + 1)
Colorcomma = CSVInput.index(",", Agecomma +1)

LastName = CSVInput[0:LNcomma]
FirstName = CSVInput[LNcomma+1:FNcomma]
Age = CSVInput[FNcomma+1:Agecomma]
Color = CSVInput[Agecomma+1:Colorcomma]
LuckyNumber = CSVInput[Colorcomma+1:len(CSVInput)]
print("Last Name=",LastName,", First Name=",FirstName,", Age=",Age, ", Favorite Color=",Color,", Lucky Number=",LuckyNumber)
