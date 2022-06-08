import math
n = eval(input())
x = math.floor(math.sqrt(n)) + 1
for i in range(2, x):
	if (n % i == 0):
		print("Not Prime")
		quit()
	
print("Prime")