def decToBinary(n):
	if(n==1):
		return "1"
	elif(n==0):
		return "0"
	else:	
		return decToBinary(int(n/2)) + str(n%2)


num = int(input("Enter decimal number to convert to binary - "))
print("Binary equivalent of", num, "is equal to " + decToBinary(num))
