def genParantheses(openB, closeB, n, s=[]):
	# base case
	if(closeB == n):
		print(''.join(s))
		return

	else:
		if(openB > closeB):
			# you can definitely put one closing bracket
			s.append(')')
			genParantheses(openB, closeB+1, n, s)
			s.pop()
		if(openB<n):
			s.append('(')
			genParantheses(openB+1, closeB, n, s)
			s.pop()
		return

n = eval(input())
genParantheses(0,0,n)