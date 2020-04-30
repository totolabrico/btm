import os

class Draw_menu_editor(Draw_menu):

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

    def set_list(self):
        self.list=[[],[]]
        self.origin=int(self.menu.element/(self.menu.element_per_line*2))*(self.menu.element_per_line*2)
        max=self.origin+self.menu.element_per_line*2
        if max>self.menu.nb:
            max=self.menu.nb

        self.set_pointer(self.origin)
        value=self.origin
        i=0
        j=0
        while value<max:
            self.list[j].append(self.menu.list[value])
            value+=1
            i+=1
            if i!=0 and i%self.menu.element_per_line==0:
                i=0
                j+=1
        print("pointer",self.pointer)

    def set_pointer(self,Min):
        pointer_display=self.menu.element-Min
        if pointer<self.menu.element_per_line:
            j=0
        else:
            j=1
            pointer-=self.menu.element_per_line
        self.pointer=[pointer,j]
