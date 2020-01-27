from sys import argv
from random import randint
from sys import exit
script,file_name1,file_name2=argv
# the text file stores the input of the user
text1=open(file_name1)
text2=open(file_name2)
# this matrix stores the states of the cells on the grid
# there are three states 
""" 1.Unknown-0
	2.Miss-1
	3.Hit-2
"""
matrix=[[0 for i in range(0,10)]for i in range(0,10)]
# this matrix will store the position of the ships as provided by the user.currently all states are set to zero
ship_matrix=[[0 for i in range(0,10)]for i in range(0,10)]
# we are doing this so that we can check our program as we progress
for i in range(0,10):
	for j in range(0,10):
		matrix[i][j]=text1.read(1)
		char=text1.read(1)

for i in range(0,10):
	for j in range(0,10):
		print "%c "%matrix[i][j],
	print "\n"	

print "\n\n"		
# this is to take the input from the user about the location of ships
for i in range(0,10):
	for j in range(0,10):
		ship_matrix[i][j]=text2.read(1)
		char=text2.read(1)

for i in range(0,10):
	for j in range(0,10):
		print "%c "%ship_matrix[i][j],
	print "\n"			
# making a list for storing the states of the five ships and a list to store their lenghts
"""   name         index    symbol   size

	  Carrier		0		C   	5  
	  Battleship	1 		B   	4
	  Cruiser	    2   	R   	3
	  Submarine     3   	S   	3
	  Destroyer     4   	D   	2
"""
shipstate=[1,1,1,1,1]   #stores the states of ship, destroyed-0 alive-1
ship_size=[5,4,3,3,2]   #size of ships
count=[0,0,0,0]         #stores the count of no. of possibilities of the four neighbours once a cell is hit

#checks whether a given cell within the grid and not already tried
def is_valid(i,j):
	if i>-1 and i<10 and j>-1 and j<10 and matrix[i][j]!='M':
		return True
	else:
		return False

# finds the maximum of four values 
def maximum():
	print count
	max_value=count[0]
	max_index=0
	for i in range(1,4):
		if count[i]>max_value:
			max_index=i
			max_value=count[i]

	return max_index		
# the main function which is called once a cell which contains a ship is hit
def target_mode(i,j,char):
	print "(%d,%d)" %(i,j)
	ship_matrix[i][j]='X'
	probability[i][j]=0
	global count
	count=[0,0,0,0]
	# to count the possible options for the four neighbours once a cell is hit
	count_horizontal(i,j-1,0)
	count_vertical(i,j-1,0)
	count_horizontal(i-1,j,1)
	count_vertical(i-1,j,1)
	count_horizontal(i,j+1,2)
	count_vertical(i,j+1,2)
	count_horizontal(i+1,j,3)
	count_vertical(i+1,j,3)
	max_index=maximum()
	# deciding the next target
	if max_index==0:
		next_target=[i,j-1]
	elif max_index==1:
		next_target=[i-1,j]
	elif max_index==2:
		next_target=[i,j+1]
	else:
		next_target=[i+1,j]
	print "(%d,%d)" %(next_target[0],next_target[1])
	# if the next target turns a miss recursivevly call the function again
	if ship_matrix[next_target[0]][next_target[1]]=='0':
		print "Missed"
		matrix[next_target[0]][next_target[1]]='M'
		target_mode(i,j,char)
	else:
		print "Hit"
		# update the values of the matrix
		ship_matrix[next_target[0]][next_target[1]]='X'
		matrix[i][j]='M'
		matrix[next_target[0]][next_target[1]]='M'
		probability[next_target[0]][next_target[1]]=0
		# decide the direction
		direction=""
		if max_index==0:
			direction="left"
		elif max_index==1:
			direction="up"
		elif max_index==2:
			direction="right"
		else:
			direction="down"
		print direction
		# call the function to completely destroy the ship
		destroy_ship(direction,next_target[0],next_target[1],i,j,char,0)
		update_shipstate(char)
		print matrix
		print ship_matrix

def hunt():
		char=ship_matrix[1][2]
		target_mode(1,2,char)		

# checks whether there are any live ships left	
def all_destroyed():
	flag=1
	for i in shipstate:
		if(i==1):
			flag=0

	if flag==1:
		return True
	else:
		return False

# updates the state of the ships	
def update_shipstate(char):
	if char=='C':
		shipstate[0]=0
	elif char=='B':
		shipstate[1]=0
	elif char=='R':
		shipstate[2]=0
	elif char=='S':
		shipstate[3]=0
	elif char=='D':
		shipstate[4]=0
# to destroy the rest of the ship			
def destroy_ship(direction,i,j,start_i,start_j,char,flag):  # the flag helps us to deal the case of adjacent ships
	if direction=="up":
		if(is_valid(i-1,j)):
			if try_cell(i-1,j)==True:
				print "(%d,%d)"%(i-1,j)
				ship_matrix[i-1][j]='X'
				matrix[i-1][j]='M'
				probability[i-1][j]=0
				if ship_destroyed(start_i,start_j,char)==False:
					destroy_ship("up",i-1,j,start_i,start_j,char,flag)
				else:
					print "the ship is completely destroyed"
					return 	
			else:
				print "reverse direction-down"
				destroy_ship("down",start_i,start_j,start_i,start_j,char,1)
		else:
			flag=1
			print "reverse direction-down"
			destroy_ship("down",start_i,start_j,start_i,start_j,char,1)
	elif direction=="left":
		if(is_valid(i,j-1)):
			if try_cell(i,j-1)==True:
				print "(%d,%d)" %(i,j-1)
				ship_matrix[i][j-1]='X'
				matrix[i][j-1]='M'
				probability[i][j-1]=0
				if ship_destroyed(start_i,start_j,char)==False:
					destroy_ship("left",i,j-1,start_i,start_j,char,flag)
				else:
					print "the ship is completely destroyed"
					return
			else:
				flag=1
				print "reverse direction-right"
				destroy_ship("right",start_i,start_j,start_i,start_j,char,1)
		else:
			flag=1
			print "reverse direction-right"
			destroy_ship("right",start_i,start_j,start_i,start_j,char,1)
	elif direction=="down":
		if(is_valid(i+1,j)):
			if try_cell(i+1,j)==True:
				print "(%d,%d)" %(i+1,j)
				ship_matrix[i+1][j]='X'
				matrix[i+1][j]='M'
				probability[i+1][j]=0
				if ship_destroyed(start_i,start_j,char)==False:
					destroy_ship("down",i+1,j,start_i,start_j,char,flag)
				else:
					print "the ship is completely destroyed"
					return	
			else:
				flag=1
				print "reverse direction-up"
				destroy_ship("up",start_i,start_j,start_i,start_j,char,1)
		else:
			flag=1
			print "reverse direction-up"
			destroy_ship("right",start_i,start_j,start_i,start_j,char,1)
			
	else:
		if(is_valid(i,j+1)):
			if try_cell(i,j+1)==True:
				print "(%d,%d)" %(i,j+1)
				ship_matrix[i][j+1]='X'
				matrix[i][j+1]='M'
				probability[i][j+1]=0
				print ship_destroyed(start_i,start_j,char)
				if ship_destroyed(start_i,start_j,char)==False:
					destroy_ship("right",i,j+1,start_i,start_j,char,flag)
				else:
					print "the ship is completely destroyed"
					return	
			else:
				flag=1
				print "reverse direction-left"
				destroy_ship("left",start_i,start_j,start_i,start_j,char,1)
		else:
			flag=1
			print "reverse direction-left"
			destroy_ship("left",start_i,start_j,start_i,start_j,char,1)
# checks whether a cell contains a ship or not
# can use a parameter char to check for a particular ship
def try_cell(i,j):
	if ship_matrix[i][j]!='0':  # check this
		return True
	else:
		return False	
# checks whether the ship has been completely destroyed
def ship_destroyed(i,j,char):
	flag=1
	for k in range(0,10):
		if ship_matrix[i][k]==char:
			flag=0

	for k in range(0,10):
		if ship_matrix[k][j]==char:
			flag=0

	if flag==0:
		return False
	else:
		return True					


# counts the number of ways to place all(alive) ships horizontally such that they pass through (i,j)
def count_horizontal(i,j,index):
	idx=0
	for size in ship_size:
		if shipstate[idx]==0:
			idx+=1
			continue

		if is_valid(i,j)==True:
			for k in range(j-(size-1),j+1):
				if is_valid(i,k)==True:
					for m in range(0,size):
						flag=1
						if(is_valid(i,k+m)==False):
							flag=0
							break

					if flag==1:
						count[index]+=1
	idx+=1
			
# counts the number of ways to place all(alive) ships vertically such that they pass through (i,j)
def count_vertical(i,j,index):
	idx=0
	for size in ship_size:
		if shipstate[idx]==0:
			idx+=1
			continue

		if is_valid(i,j)==True:
			for k in range(i-(size-1),i+1):
				if is_valid(k,j):
					for m in range(0,size):
						flag=1
						if(is_valid(k+m,j)==False):
							flag=0
							break

					if flag==1:
						count[index]+=1
	idx+=1						
hunt()