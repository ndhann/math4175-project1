def gcd(a, b):
	u1 = 1  	#
	v1 = 0  	#
	u2 = 0  	#
	v2 = 1  	#
	if a > b:   #
    	u3 = a  #  Gets the initial values of our variables
    	v3 = b  #
	else:   	#
    	u3 = b  #
    	v3 = a  #
	q = 0   	#
	largest_length = len(str(u3)) # Used for formatting purposes
    
	# Table construction
	table = "| {:>{width}} | {:>{width}} | {:>{width}} | {:>{width}} | {:>{width}} | {:>{width}} | {:>{width}} |\n".format('u1', 'v1', 'u2', 'v2', 'u3', 'v3', 'q', width = largest_length + 1)
    
	# Adds initial values to the table
	table += "| {:>{width}} | {:>{width}} | {:>{width}} | {:>{width}} | {:>{width}} | {:>{width}} | {:>{width}} |\n".format(u1, v1, u2, v2, u3, v3, q, width = largest_length + 1)

	while v3 != 0:  # Loops until v3 is 0 updating each variable every iteration
    	q = u3//v3
    	oldu1 = u1
    	oldu2 = u2
    	oldu3 = u3
    
    	u1 = v1
    	u2 = v2
    	u3 = v3
    
    	v1 = oldu1 - (q*v1)
    	v2 = oldu2 - (q*v2)
    	v3 = oldu3 - (q*v3)
   	 
    	# Adds the new values to our table with special format specifiers
    	table += "| {:>{width}} | {:>{width}} | {:>{width}} | {:>{width}} | {:>{width}} | {:>{width}} | {:>{width}} |\n".format(u1, v1, u2, v2, u3, v3, q, width = largest_length + 1)
    
	eq = ""
	if a > b:
    	eq += str(a) + "x + " + str(b) + "y = "
	else:
    	eq += str(b) + "x + " + str(a) + "y = "
   	 
	# Returns our table with the GCD
	return "Table:\n" + table + "\nGCD(" + str(a) + ", " + str(b) + ")" + " = " + eq + str(u3) + "\nx = " + str(u1) + "\ny = " + str(u2)
print(gcd(8,13))
