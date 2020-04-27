
class Draw_menu:
    
    def __init__(self,Menu):
        self.menu=Menu
        #self.navigator=self.machine.navigator
        self.pointer=0
        self.pointer_line=0
        self.origin_line=0
        self.max_line=4
        self.origin_pas=0
        self.display_list=[]
        self.set_draw()

    def set_draw(self):
        self.set_pointer()
        self.set_list()

    def set_max_line(self):
        if self.menu.name!="notes":
            self.max_line=4
        else:
            self.max_line=1
        
        if len(self.menu.List)<self.max_line:
            self.max_line=len(self.menu.List)
            
    def set_list(self):
        self.set_max_line()
        
        if self.menu.name!="notes":
            self.display_list=[]
            i=self.origin_line 
            while i<self.origin_line+self.max_line:
                self.display_list.append(self.menu.List[i])
                i+=1
        else:
            self.set_display_list_pas()
            self.display_list=[]
            if len(self.menu.List)>0:
                self.display_list.append(self.menu.List[self.menu.pointer])
                
    def set_display_list_pas(self):
        self.display_list_pas=[[],[]]
        self.origin_pas=int(self.menu.pas/(self.menu.pas_per_line*2))*(self.menu.pas_per_line*2)
        max=self.origin_pas+self.menu.pas_per_line*2
        if max>self.menu.nb_pas:
            max =self.menu.nb_pas
    
        self.set_pointer_pas(self.origin_pas)
        value=self.origin_pas
        i=0
        j=0
        while value<max:
            self.display_list_pas[j].append(self.menu.list_pas[value])
            value+=1
            i+=1
            if i!=0 and i%self.menu.pas_per_line==0:
                i=0
                j+=1
        print("pointer_pas",self.pointer_pas)
        
    def set_pointer_pas(self,Min):
        pointer_pas=self.menu.pas-Min
        if pointer_pas<self.menu.pas_per_line:
            j=0
        else:
            j=1
            pointer_pas-=self.menu.pas_per_line
        self.pointer_pas=[pointer_pas,j]

    def set_pointer(self):# set pointer & origin

        if self.menu.pointer==0: # if 'min'
            self.origin_line=0
            self.pointer_line=0
            
        elif self.menu.pointer==len(self.menu.List)-1: # if 'max'
            self.pointer_line=self.max_line-1
            self.origin_line=len(self.menu.List)-self.max_line
            
        elif self.menu.pointer>self.pointer:# if '+'
            if self.pointer_line<self.max_line-1:
                self.pointer_line+=1
            elif self.pointer_line==self.max_line-1:
                self.origin_line+=1
                
        elif self.menu.pointer<self.pointer:# if '-'
            if self.pointer_line>0:
                self.pointer_line-=1
            elif self.pointer_line==0:
                self.origin_line-=1
        
        print("pointer",self.pointer,self.menu.pointer,self.origin_line,self.pointer_line)
        self.pointer=self.menu.pointer
                

            
