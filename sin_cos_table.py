from math import sin, cos, radians



DECIMALS = 3 # Precision



decimals = 10.0**float(DECIMALS)



f = open("SINE_TABLE.txt", "w")

for i in [x/decimals for x in range(360*int(decimals))]:
    f.write(str(sin(radians(i))) + "\n")

f.close()



f = open("COSINE_TABLE.txt", "w")

for i in [x/decimals for x in range(360*int(decimals))]:
    f.write(str(cos(radians(i))) + "\n")

f.close()

