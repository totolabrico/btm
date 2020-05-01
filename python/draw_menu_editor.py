import os

class Draw_menu_editor():

    def __init__(self,Menu):
        self.menu=Menu
        self.pointer=0
        self.pointer_display=0
        self.origin=0
        self.set_draw()
        
    def set_draw(self):
        self.set_origin()
        self.set_max()
        self.set_pointer()
        self.set_list()

    def set_origin(self):
        self.origin=int(self.menu.pointer_element/(self.menu.element_per_line*2))*(self.menu.element_per_line*2)

    def set_max(self):
            
        real_max=self.menu.nb_element
        theoric_max=self.origin+self.menu.element_per_line*2
        
        if theoric_max>real_max:
            self.max=real_max
        else:
            self.max=theoric_max
        print("max_element",self.menu.list_element)

    def set_list(self):
        self.list=[[],[]]
        value=self.origin
        i=0
        j=0
        print("max",self.max)
        while value<self.max:
            if self.menu.name=="tracks":
                self.list[j].append(self.menu.list_element[value])
            elif self.menu.name=="notes":
                self.list[j].append(0)
                for element in self.menu.track.notes:
                    if value==element.pas:
                        self.list[j][i]=element
                
            value+=1
            i+=1
            if i!=0 and i%self.menu.element_per_line==0:
                i=0
                j+=1
        print("draw_menu_editor-set_list",self.origin,self.max,self.pointer,self.pointer_display,self.list)

    def set_pointer(self):
        self.pointer=self.menu.pointer_element-self.origin
        if self.pointer<self.menu.element_per_line:
            j=0
        else:
            j=1
            self.pointer-=self.menu.element_per_line
        self.pointer_display=[self.pointer,j]
