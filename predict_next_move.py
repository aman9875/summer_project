from sys import argv
from random import randint
import time
script,file = argv
txt = open(file)
matrix = [['0' for i in range(10)]for j in range(10)]
copy_matrix = [['0' for i in range(10)]for j in range(10)]
probability = [[0 for i in range(0,10)]for j in range(0,10)]
shipstate = [1,1,1,1,1]
ship_size = [5,4,3,3,2]
test_val = 10
sub_val = 3
ships = ['C','B','R','S','D']
ship_matrix = [['0' for i in range(0,10)]for j in range(0,10)]
txt2 = open('next_move.txt','a')
ans_matrix=[['0' for i in range(0,10)]for j in range(0,10)] #this matrix stores the output values
#read from file
for i in range(0,10):
	for j in range(0,10):
		matrix[i][j] = txt.read(1)
		copy_matrix[i][j]=matrix[i][j]
		char = txt.read(1)

ship_train_state=['0','0','0','0','0']
for i in range(5):
	ship_train_state[i]=txt.read(1)
#print ship_train_state
#print matrix
hits = [[0 for x in range(0,4)]for y in range(0,50)]

def is_exists(i,j):
	if (i>=0 and i<10 and j>=0 and j<10):
		return 1
	else:
		return 0	

def write_to_file():
	ship=""
	for i in range(10):
		for j in range(10):
			if j!=9:
				ship+=ship_matrix[i][j]+" "
			else:
				ship+=ship_matrix[i][j]+"\n"			
	txt2.write(ship)
	txt2.write("\n")				


def calculate_prob():
	for i in range(0,10):
		for j in range(0,10):
			probability[i][j]=0
	for x in range(5):
		if shipstate[x]==1:
			length = ship_size[x]
			for i in range(10):
				count = 0
				initial = 0
				for j in range(10):
					if not (matrix[i][j]=='M'):
						count=count+1
					if (matrix[i][j]=='M') or j==9:
						if count>=length:
							max_value = count-length+1
							if max_value>length:
								max_value=length
							value=1
							start = initial
							end = initial+count-1
							while start<=end:
								if(value>max_value):
									value = max_value
								if start!=end:
									probability[i][start]=probability[i][start]+value
									probability[i][end]=probability[i][end]+value
								else:
									probability[i][start]=probability[i][start]+value
								start+=1
								end-=1
								value+=1			

						initial = j+1
						count=0
			for i in range(10):
				count = 0
				initial = 0
				for j in range(10):
					if not (matrix[j][i]=='M'):
						count=count+1
					if (matrix[j][i]=='M') or j==9:
						if count>=length:
							max_value = count-length+1
							if max_value>length:
								max_value=length
							value=1
							start = initial
							end = initial+count-1
							while start<=end:
								if(value>max_value):
									value=max_value
								if start!=end:
									probability[start][i]=probability[start][i]+value
									probability[end][i]=probability[end][i]+value
								else:
									probability[start][i]=probability[start][i]+value	
								start+=1
								end-=1
								value+=1			
						initial = j+1
						count=0

def find_max_prob():
	maximum = 0
	maximum_index =[0,0]
	for i in range(0,10):
		for j in range(0,10):
			if probability[i][j]>maximum:
				maximum=probability[i][j]
				maximum_index=[i,j]

	print("%c %d"%(maximum_index[0]+65,maximum_index[1]+1))	
	ans_matrix[maximum_index[0]][maximum_index[1]]='1'		

def print_prob():
	for i in range(0,10):
		for j in range(0,10):
			if j==9:
				print("%d\n"%(probability[i][j])),
			else:
				print("%d "%(probability[i][j])),	

#search for positions which have hits
def search_hits():
	idx = 0
	for i in range(0,10):
		for j in range(0,10):
			if matrix[i][j]=='H':
				matrix[i][j]='0'
				length =1
				direction = -1
				if (is_exists(i+1,j)==1 and matrix[i+1][j]=='H'):
					x=i+1
					direction=1
					while x<10 and matrix[x][j]=='H':
						matrix[x][j]='0'
						length+=1
						x+=1
				elif (is_exists(i,j+1)==1 and matrix[i][j+1]=='H'):
					x=j+1
					direction=2
					while x<10 and matrix[i][x]=='H':
						matrix[i][x]='0'
						length+=1
						x+=1
				hits[idx] = [i,j,length,direction]
				idx+=1

def empty_ship_matrix():
	for i in range(10):
		for j in range(10):
			ship_matrix[i][j]='0'

def update_ship_state():
	for i in range(0,5):
		if ship_train_state[i]=='1':
			shipstate[i]=1
		else:
			shipstate[i]=0	

#generate the probability matrix by taking a large number of random configurations
def generate():
	for num in range(1000):
		empty_ship_matrix()
		update_ship_state()
		for x in hits:
			if x!= [0,0,0,0]:
				if x[3]!=-1:
					place_ships_hit_area(x[0],x[1],x[2],x[3])
				else:
					d = randint(1,2)
					place_ships_hit_area(x[0],x[1],x[2],d)
		main()
		for i in range(10):
			for j in range(10):
				if ship_matrix[i][j]=='C' or ship_matrix[i][j]=='B' or ship_matrix[i][j]=='R' or ship_matrix[i][j]=='S' or ship_matrix[i][j]=='D':
					probability[i][j]+=1
		for i in range(10):
			for j in range(10):
				if copy_matrix[i][j]=='H':
					probability[i][j]=0	

#place the ships at the hit positions
def place_ships_hit_area(x,y,length,direction):
	while(True):
		num = randint(0,4)
		if shipstate[num]==1:
			if ship_size[num]>length:
				diff = ship_size[num]-length
				while(True):
					r = randint(0,diff)
					if direction==1:
						if x-r>=0 and x-r+ship_size[num]<=9:
							for i in range(x-r,x-r+ship_size[num]):
								ship_matrix[i][y]=ships[num]
							shipstate[num]=0
							break	
					elif direction==2:
						if y-r>=0 and y-r+ship_size[num]<=9:
							for i in range(y-r,y-r+ship_size[num]):
								ship_matrix[x][i]=ships[num]
							shipstate[num]=0
							break	
				break					
#place the ship horizontally
def write_at_x(a,b,x,l):
	for i in range(b,b+l):
		ship_matrix[a][i]=x
		
#place the ship vertically
def write_at_y(a,b,x,l):
	for i in range(a,a+l):
		ship_matrix[i][b] = x

#check if the ship can be placed at the random coordinates
def check(a,b,d,l):
	flag=0
	if d==0:
		if b+l>10:
			return False
		for i in range(b,b+l):
			if ship_matrix[a][i]=='C' or ship_matrix[a][i]=='B' or ship_matrix[a][i]=='R' or ship_matrix[a][i]=='S' or ship_matrix[a][i]=='D' or matrix[a][i]=='M':
				flag=1
				break
		if flag==1:
			return False
		else:
			return True
	else:
		if a+l>10:
			return False
		for i in range(a,a+l):
			if ship_matrix[i][b]=='C' or ship_matrix[i][b]=='B' or ship_matrix[i][b]=='R' or ship_matrix[i][b]=='S' or ship_matrix[i][b]=='D' or matrix[i][b]=='M':
				flag=1
				break
		if flag==1:
			return False
		else:
			return True
										

#place all the remaining ships
def main():
	idx=0
	for x in ships:
		if shipstate[idx]==1:
			while(True):
				a = randint(0,9)
				b = randint(0,9)
				direction = randint(0,1)
				if(direction==0):
					if not(check(a,b,direction,ship_size[idx])):
						continue
					else:
						write_at_x(a,b,x,ship_size[idx])
						break
				else:
					if not(check(a,b,direction,ship_size[idx])):
						continue
					else:
						write_at_y(a,b,x,ship_size[idx])
						break
			shipstate[idx]=0						
		idx=idx+1				


#check whether to go to hunt or target mode
flag = False
for i in range(0,10):
	for j in range(0,10):
		if matrix[i][j]=='H':
			flag = True

if flag ==False:
	calculate_prob()
	print_prob()
	find_max_prob()
else:
	search_hits()
	generate()
	print_prob()
	find_max_prob()
	
s=""   # this is to write the state in a string format
for i in range(0,10):
	for j in range(0,10):
		if copy_matrix[i][j]=='0':
			s+='0\t'
		elif copy_matrix[i][j]=='M':
			s+='-1\t'
		else:
			s+='1\t'

for i in range(0,10):
	for j in range(0,10):
		s+=ans_matrix[i][j]+"\t"

txt2.write(s)
txt2.write("\n")


