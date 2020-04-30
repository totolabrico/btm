import os

class Draw_menu_editor(Draw_menu):

    def __init__(self,Menu):
        self.menu=Menu
        #self.navigator=self.machine.navigator
        self.pointer_element=0
        self.pointer_element_display=0
        self.origin_element=0
        self.max_element=4
        self.list_element=[]
        self.set_draw_element()

    def set_draw_element(self):
        self.set_pointer_element()
        self.set_list_element()

    def set_list_element(self):
        self.list_element=[[],[]]
        self.origin_element=int(self.menu.element/(self.menu.element_per_line*2))*(self.menu.element_per_line*2)
        max_element=self.origin_element+self.menu.element_per_line*2
        if max_element>self.menu.nb_element:
            max_element=self.menu.nb_element

        self.set_pointer_element(self.origin_element)
        value=self.origin_element
        i=0
        j=0
        while value<max_element:
            self.list_element[j].append(self.menu.list_element[value])
            value+=1
            i+=1
            if i!=0 and i%self.menu.element_per_line==0:
                i=0
                j+=1
        print("pointer_element",self.pointer_element)

    def set_pointer_element(self,Min):
        pointer_display=self.menu.element-Min
        if pointer_element<self.menu.element_per_line:
            j=0
        else:
            j=1
            pointer_element-=self.menu.element_per_line
        self.pointer_element=[pointer_element,j]
