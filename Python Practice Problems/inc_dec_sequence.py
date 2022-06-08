import sys
n = eval(input())
isAscending=True
isDescending=True
prev = sys.maxsize

for i in range(n):
	curr = eval(input())
	if(isDescending):
		if(prev<=curr):
			isDescending = False
	else:
		if(prev>=curr):
			isAscending = False
	prev = curr

if(isAscending):
	print("true")
else:
	print("false")