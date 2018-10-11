import numpy as np

def main ():
	i = 0
	n = 10
	x = 119.0
	
	# we can use numpy to quickly make arrays
	y = np.zeros(n,dtype=float) #declares 10 zeroes
	
	# we can use for loops to iterate through a variable
	
	for i in range (n):
		y[i] = 2.0 * float(i) + 1.0
		
	for y_element in y:
		print(y_element)

if __name__ == "__main__":
	main()
