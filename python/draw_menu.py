import os

class Draw_menu:
    
    def __init__(self,Menu):
        self.menu=Menu
        #self.navigator=self.machine.navigator
        self.pointer=0
        self.pointer_display=0
        self.origin=0
        self.max=4
        self.list=[]
        self.set_draw()

    def set_draw(self):
        self.set_pointer()
        self.set_list()

    def set_max(self):
        if self.menu.name!="notes":
            self.max=4
        else:
            self.max=1
        
        if len(self.menu.List)<self.max:
            self.max=len(self.menu.List)
            
    def set_list(self):
        self.set_max()
        self.list=[]
                
        if self.menu.name!="notes":
            i=self.origin
            
            while i<self.origin+self.max:
                to=self.menu.List[i]
                if self.menu.name=="browser" and os.path.isdir(self.menu.path+to)==True:
                    to=">"+to
                self.list.append(to)
                i+=1            
        else:
            self.set_list()
            if len(self.menu.List)>0:
                self.display_list.append(self.menu.List[self.menu.pointer])
                
    def set_pointer(self):# set pointer & origin

        if self.menu.pointer==0: # if 'min'
            self.origin=0
            self.pointer_display=0
            
        elif self.menu.pointer==len(self.menu.List)-1: # if 'max'
            self.pointer_display=self.max-1
            self.origin=len(self.menu.List)-self.max
            
        elif self.menu.pointer>self.pointer:# if '+'
            if self.pointer_display<self.max-1:
                self.pointer_display+=1
            elif self.pointer_display==self.max-1:
                self.origin+=1
                
        elif self.menu.pointer<self.pointer:# if '-'
            if self.pointer_display>0:
                self.pointer_display-=1
            elif self.pointer_display==0:
                self.origin-=1
        
        print("pointer",self.pointer,self.menu.pointer,self.origin,self.pointer_display)
        self.pointer=self.menu.pointer
                
    def set_display_list(self):
        self.list=[[],[]]
        self.origin=int(self.menu.pas/(self.menu.pas_per_line*2))*(self.menu.pas_per_line*2)
        max=self.origin+self.menu.pas_per_line*2
        if max>self.menu.nb_pas:
            max =self.menu.nb_pas
    
        self.set_pointer_pas(self.origin)
        value=self.origin
        i=0
        j=0
        while value<max:
            self.list[j].append(self.menu.list_pas[value])
            value+=1
            i+=1
            if i!=0 and i%self.menu.pas_per_line==0:
                i=0
                j+=1
        print("pointer_pas",self.pointer_pas)
        
    def set_pointer_pas(self,Min):
        pointer_display=self.menu.pas-Min
        if pointer_pas<self.menu.pas_per_line:
            j=0
        else:
            j=1
            pointer_pas-=self.menu.pas_per_line
        self.pointer_pas=[pointer_pas,j]
