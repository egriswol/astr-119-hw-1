try:
	print(a)		#this gives an exception because a is not defined
except:
	print("a is not defined!")
	
#there are specific errors to hep with cases
try: 
	print(a)		#gives an exception
except NameError:
	print("a is still not defined!")	
except:
	print("Something else went wrong")
	
#breaks program since a is not defined
print(a)
