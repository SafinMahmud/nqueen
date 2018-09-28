import random

n = int(input("Enter a number: "))

a = [[0] * n for i in range(n)]
qpos = [0]*n

# putting '.' characters in nxn cells
for i in range(n):
	for j in range(n):
		a[i][j] = '.'

# putting randomly n number of queens in n coloumns
# so there is one queen in every row. 
# but there can be multiple queens in one row. becasue the row is chosen randomly
# and then stored the row number where queen exits in qpos[] list 
for j in range(n):
	i = random.randint(0,n-1)
	a[i][j] = 'X'
	qpos[j] = i     # the row number of every col of queen position

# this function will count and the return the no of violation of the rth row and cth coloumn queen.
# by violation I mean how many queen are this queen attacking from that rth row and cth coloumn position.
def violations(r,c):
	count = -1
	leftDiagonal = r+c
	rightDiagonal = r-c
	for i in range(n):
		for j in range(n):
			if ((i+j) == leftDiagonal or (i-j) == rightDiagonal or i == r or j==c) and (a[i][j]=='X'):
				count = count + 1
	return count


sum = 1
# first i am finding which coloumn's queen is attacking maximum number of queen
# then i am changing that queen's row position in that coloumn
# to where it is attacking less number of queen from it's previous position
# and in every iteration i am calculating the sum of all the violations(number of queens the queen is attacking) of every queen.
# until that sum is zero meaning no queen is attacking any other queen the loop will continue
while sum != 0:
	sum = 0
	maxViolation = 0
	col = 0 
	row = 0
	# here I a looping through every coloumn to find out 
	# Queen of which coloumn is attacking maximum number of queen from it's current position.

	for j in range(n):
		temp = violations(qpos[j],j)
		sum = sum + temp 
		if temp > maxViolation:
			maxViolation = temp
			col = j  #Queen of which coloumn has the max violations

		# if more than one queen is attacking maximum no of queens then i am choosing one of them randomly  
		t = random.randint(0,2)
		if temp == maxViolation and t == 0:
			maxViolation = temp
			col = j 

	a[qpos[col]][col] = '.' 
	
	# now i am changing that queen's row position in that coloumn to minimize the violations
	minViolation = n+1
	for i in range(n):
		a[i][col] = 'X'
		temp = violations(i,col)
		if temp < minViolation:
			minViolation = temp
			row = i
		# again if the queen is attacking same minimum no of queens from different row position 
		# then i am choosing one of the row randomly
		t1 = random.randint(0,2)
		if temp == minViolation and t1 == 0:
			minViolation = temp
			row = i
		a[i][col] = '.'

	qpos[col] = row

	# here i am changing the queen position to a row 
	# where it is attacking less number of queen from it's previous position
	a[row][col] = 'X'

# printing the queen's position in chess board where no queen is attacking each other.

for i in range(0,n):
	for j in range(0,n):
		print(" ",a[i][j],end='')
	print()
