import numpy as np		

#integers

i = 10					
print(type(i))			

a_i = np.zeros(i,dtype=int)		#declare array
print(type(a_i))				#return ndarray
print(type(a_i[0]))				#return int64

#floats

x = 119.0				
print(type(x))		

y = 1.19e2				#float in sci notation
print(type(y))			#print data type

z = np.zeros(i,dtype=float)		#declare array of floats
print(type(z))					#return nd array
print(type(z[0]))				#return float64
