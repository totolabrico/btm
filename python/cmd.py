def edit(cmd,setting):
	print ("edit: ",cmd,setting)
	value=setting[1]

	if type(value)==bool:
		if cmd=="-":
			value=False
		elif cmd=="+":
			value=True
		elif cmd=="++":
			value=not value

	elif type(value)==int or type(value)==float:
		min=setting[2]
		max=setting[3]
		inc=setting[4]
		if cmd=="-":
			value-=inc
		elif cmd=="--":
			value-=inc*10
		elif cmd=="+":
			value+=inc
		elif cmd=="++":
			value+=inc*10
		else:
			value=cmd
			
		if value>max:
			value=max
		elif value<min:
			value=min
		value=round(value,2)

	elif type(value)==str:
		if arg=="+" or arg=="-":
			pass
		else:
			print("yea : ",arg)
			value=arg

	setting[1]=value
	return setting

def move(Cmd,Arg,Tools,Length):
	w,h=Tools["grid"]
	x,y=Tools["pointer"]
	o=Tools["origin"]
	l=Length
	r=l%w
	hmax=l/w
	if int(hmax)!=hmax:
		hmax=int(hmax+1)
	if hmax<h:
		h=hmax
	# Ajout des valeurs x ou y au pointer
	if Cmd=="x":
		if Arg=="+":
			x+=1
		else:
			x-=1

	if Cmd=="y":
		if Arg=="+":
			y+=1
		else:
			y-=1
			
	# Correction des valeurs x ou y du pointer si elles sortent de la grille
	if x<0:
		x=w-1
		y-=1
	if x==w:
		x=0
		y+=1

	if y<0:
		y=hmax-1
	if y==hmax:
		y=0

	# Correction des valeurs x ou y du pointer si on est dans le vide
	if r!=0 and y==hmax-1 and x>=r:
		if Cmd=="x":
			if Arg=="+":
				x=0
				y=0
			else:
				x=w-1-r
				y=hmax-1

		if Cmd=="y":
			if Arg=="+":
				y=0
			else:
				y=hmax-2
				o=y-(h-2) #origin
				
	# Correction de l'origine de y
	if y==0:
		o=0
	elif y==hmax-1:
		o=int(hmax-h)
	else:
		if y-o==h:
			o+=1
		if y<o:
			o-=1

	Tools["pointer"]=[x,y]
	Tools["origin"]=o

	return Tools

def get_key(Dico,Index):
	for key,value in Dico.items():
		#print(key,value)
		if (value[0]==Index):
			return key

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

def check_wav(txt):
	if txt[len(txt)-4:]==".wav" or txt[len(txt)-4:]==".WAV":
		return True
	else:
		return False	

def get_name(name):
	
	if name!="empty":
		name=name.split("/")
		name=name[len(name)-1]
		name=name.split(".")[0]
	
	return name

def set_txt_size(Txt,Size):
    if check_wav(Txt)==True:
        Txt=Txt[:-4]
    if len(Txt)>Size:
        dif=len(Txt)-Size
        Txt=Txt[dif:]
    return Txt
    
def get_loop_length(Begin,End,Nbnote):
	if Begin==End:
		return 1
	if Begin<End:
		return End-Begin
	else:
		return Nbnote-(Begin-End)
