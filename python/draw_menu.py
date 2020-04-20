
class Draw_menu:
    
    def __init__(self,Menu):
        self.menu=Menu
        #self.navigator=self.machine.navigator
        self.pointer=0
        self.pointer_line=0
        self.origin_line=0
        self.max_line=4
        self.display_list=[]
        self.set_draw()

    def set_draw(self):
        self.set_pointer()
        self.set_list()

    def set_list(self):
        self.set_max_line()
        self.display_list=[]
        i=self.origin_line 
        while i<self.origin_line+self.max_line:
            self.display_list.append(self.menu.List[i])
            i+=1
   
    def set_max_line(self):
        self.max_line=4
        if len(self.menu.List)<self.max_line:
            self.max_line=len(self.menu.List)
                 
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
                

            
