def edit(cmd,setting):

	value=setting[1]
	
	if type(value)==bool:
		if cmd=="-":
			return False
		elif cmd=="+":
			return True
		elif cmd=="*":
			return not value

	elif type(value)==int or type(value)==float:
		min=setting[2]
		max=setting[3]
		inc=setting[4]
		if cmd=="-":
			value-=inc
		elif cmd=="+":
			value+=inc
		if value>max:
			value=max
		elif value<min:
			value=min
		return round(value,2)

def move(cmd,arg,pointer,grid):
	inc=1			
	if cmd=="y":
		inc*=grid["x"][0]*grid["x"][1]
	if arg=="-":
		inc*=-1	
		
	pointer+=inc
	# attention il faut calculre le vide a partir du reste"
	if pointer>=grid["max"]:
		if pointer>=grid["max"]+grid["reste"]:
			pointer-=grid["max"]+grid["reste"]
		else:
			pointer-=grid["max"]
	elif pointer<0:
		pointer+=grid["max"]
	return pointer
	
def set_fork(pointer,fork,cmd):
	if cmd=="+":
		fork[0]=int(pointer)
	if cmd=="stop":
		fork[1]=int(pointer)
		if fork[0]>fork[1]:
			to=int(fork[0])
			fork[0]=int(fork[1])
			fork[1]=to
	return fork
	
def set_selecter(fork,selecter):
	i=fork[0]
	while i<=fork[1]:
		exist=False
		for element in selecter:
			if element==i:
				exist=True
		if exist==False:
			selecter.append(i)
		i+=1
	return selecter
		
