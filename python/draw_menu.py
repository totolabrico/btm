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
        if self.menu.name=="tracks" or self.menu.name=="notes":
            self.max=1
        else:
            self.max=4
        if len(self.menu.list)<self.max:
            self.max=len(self.menu.list)

    def set_list(self):
        self.set_max()
        self.list=[]

        if self.menu.name=="tracks" or self.menu.name=="notes":
            if len(self.menu.list)>0:
                self.list.append(self.menu.list[self.menu.pointer])

        else:
            i=self.origin

            while i<self.origin+self.max:
                to=self.menu.list[i]
                if self.menu.name=="browser" and os.path.isdir(self.menu.path+to)==True:
                    to=">"+to
                self.list.append(to)
                i+=1

    def set_pointer(self):# set pointer & origin

        if self.menu.pointer==0: # if 'min'
            self.origin=0
            self.pointer_display=0

        elif self.menu.pointer==len(self.menu.list)-1: # if 'max'
            self.pointer_display=self.max-1
            self.origin=len(self.menu.list)-self.max

        elif self.menu.pointer>self.pointer:# if '+'
            if self.pointer<self.max-1:
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
