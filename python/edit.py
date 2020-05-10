def edit(cmd,setting):
	
	value=setting[1]
	
	if type(value)==bool:
		if cmd=="-":
			return False
		elif cmd=="+":
			return True
		elif cmd=="toggle":
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
