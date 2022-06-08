n = eval(input())
for i in range(n):
	for j in range(1,n+1-i):
		print (j, end = " ")
	k = 2*i + 1
	while(k>2):
		print("*", end = " ")
		k -= 1
	print("\n", end = "")