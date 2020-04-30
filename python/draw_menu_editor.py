import os

class Draw_menu_editor(Draw_menu):

    def __init__(self,Menu):
        self.menu=Menu
        #self.navigator=self.machine.navigator
        self.pointer_pas=0
        self.pointer_pas_display=0
        self.origin_pas=0
        self.max_pas=4
        self.list_pas=[]
        self.set_draw_pas()

    def set_draw_pas(self):
        self.set_pointer_pas()
        self.set_list_pas()

    def set_list_pas(self):
        self.list_pas=[[],[]]
        self.origin_pas=int(self.menu.pas/(self.menu.pas_per_line*2))*(self.menu.pas_per_line*2)
        max_pas=self.origin_pas+self.menu.pas_per_line*2
        if max_pas>self.menu.nb_pas:
            max_pas=self.menu.nb_pas

        self.set_pointer_pas(self.origin_pas)
        value=self.origin_pas
        i=0
        j=0
        while value<max_pas:
            self.list_pas[j].append(self.menu.list_pas[value])
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
