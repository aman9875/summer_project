from random import randint
from sys import argv
script,file = argv
matrix = [['0' for x in range(10)]for y in range(10)]
ship =""
ships = ['C','B','R','S','D']
length = [5,4,3,3,2]
txt = open(file,'w')		

def write_at_x(a,b,x,l):
	for i in range(b,b+l):
		matrix[a][i]=x

def write_at_y(a,b,x,l):
	for i in range(a,a+l):
		matrix[i][b] = x

def check(a,b,d,l):
	flag=0
	if d==0:
		if b+l>=10:
			return False
		for i in range(10):
			if matrix[a][i]=='C' or matrix[a][i]=='B' or matrix[a][i]=='R' or matrix[a][i]=='S' or matrix[a][i]=='D':
				flag=1
				break
		if flag==1:
			return False
		else:
			return True
	else:
		if a+l>=10:
			return False
		for i in range(10):
			if matrix[i][b]=='C' or matrix[i][b]=='B' or matrix[i][b]=='R' or matrix[i][b]=='S' or matrix[i][b]=='D':
				flag=1
				break
		if flag==1:
			return False
		else:
			return True
										

idx=0
for x in ships:
	while(True):
		a = randint(0,9)
		b = randint(0,9)
		direction = randint(0,1)
		if(direction==0):
			if not(check(a,b,direction,length[idx])):
				continue
			else:
				write_at_x(a,b,x,length[idx])
				break
		else:
			if not(check(a,b,direction,length[idx])):
				continue
			else:
				write_at_y(a,b,x,length[idx])
				break			
	idx=idx+1			

for i in range(10):
	for j in range(10):
		ship+=matrix[i][j]

'''for i in range(5,10):
	for j in range(10):
		ship+=matrix[i][j]'''

txt.write(ship)				