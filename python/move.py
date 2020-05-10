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

	
	
