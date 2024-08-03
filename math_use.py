import math
from random import *

def degToRadian(deg):
    return (deg * math.pi)/180

print("Square root ", math.sqrt(9))
print("Cos 90 degree ",math.cos(degToRadian(90)))

print("Log ",math.log(9))

for i in range(0,11):
    r = random()
    #print("Random ", r)
    #print("Random int ",randint(1,11))
    #print("Uniform random ",uniform(1,11)) #getting float value
    #print("Random range ", randrange(1,15,2)) #generate only odd numbers till 15
    
