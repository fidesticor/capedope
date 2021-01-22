from addTwoFractions import addTwoFractions
from subTwoFractions import subTwoFractions
from mulTwoFractions import mulTwoFractions
from divTwoFractions import divTwoFractions
from getFractionFromNatNum import getFractionFromNatNum
import re
str=input()
m=re.search('([^/]+)/([0-9]+)([-+*/])([(0-9]+)/([0-9]+)',str)
#print(m.group(0))
#print(m.group(1))
#print(m.group(2))
#print(m.group(3))
#print(m.group(4))
#print(m.group(5))
if(m.group(3)=="+"):
    print(addTwoFractions(int(m.group(1)),int(m.group(2)),int(m.group(4)),int(m.group(5))))
elif(m.group(3)=="-"):
    print(subTwoFractions(int(m.group(1)),int(m.group(2)),int(m.group(4)),int(m.group(5))))
elif(m.group(3)=="*"):
    print(mulTwoFractions(int(m.group(1)),int(m.group(2)),int(m.group(4)),int(m.group(5))))
elif(m.group(3)=="/"):
    print(divTwoFractions(int(m.group(1)),int(m.group(2)),int(m.group(4)),int(m.group(5))))
