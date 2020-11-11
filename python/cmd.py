
def move(Cmd,Arg,tools):
	pointer=tools["pointer"]
	origin=tools["origin"]
	grid=tools["grid"]
	max=len(tools["element"])-1
	
	display_max=grid[0]*grid[1]
	reste=max%grid[0]
	vide=grid[0]-reste	
	
	if Cmd=="x":
		inc=1
	elif Cmd=="y":
		inc=grid[0]
		
	if Arg=="+":
		pointer+=inc
	elif Arg=="-":
		pointer-=inc
		
	if pointer>=origin+display_max:
		origin+=grid[0]
	elif pointer<origin and max>display_max:
		origin-=grid[0]

	if pointer>max:
		if Cmd=="x":
			pointer=0
		elif Cmd=="y":
			exces=pointer-max
			if exces<vide:
				print("cas 1",exces,vide)
				pointer=exces+reste
			else:
				pointer=exces-vide
		origin=0
	
	elif pointer<0:
		if Cmd=="x":
			pointer=max
		elif Cmd=="y":
			exces=0-pointer
			if exces<vide:
				pointer=max-exces-reste
			else:
				pointer=max-exces+vide
		
		if max>display_max:# si la liste depasse la taille de l'ecran je calcule l'origin
			origin=max-display_max+vide
	
	print("move_in_settings",pointer,origin,max,grid)
	tools["pointer"]=pointer
	tools["origin"]=origin
	return tools


'''
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
'''		


def setting_to_string(setting):
    if type(setting)==float or type(setting)==int:
        return str(setting)
    elif setting==True:
        return "on"
    elif setting==False:
        return "off"
    elif type(setting)==str:
        return"+"
    else:
        return setting
