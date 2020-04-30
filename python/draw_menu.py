import os

class Draw_menu:

    def __init__(self,Menu):
        self.menu=Menu
        #self.navigator=self.machine.navigator
        self.pointer_setting=0
        self.pointer_setting_display=0
        self.origin_setting=0
        self.max_setting=4
        self.list_setting=[]
        self.set_draw_setting()

    def set_draw_setting(self):
        self.set_pointer_setting()
        self.set_list_setting()

    def set_max_setting(self):
        if self.menu.name=="tracks" or self.menu.name=="notes":
            self.max_setting=1
        else:
            self.max_setting=4
        if len(self.menu.list_setting)<self.max_setting:
            self.max_setting=len(self.menu.list_setting)

    def set_list_setting(self):
        self.set_max_setting()
        self.list_setting=[]

        if self.menu.name=="tracks" or self.menu.name=="notes":
            if len(self.menu.list_setting)>0:
                self.list_setting.append(self.menu.list_setting[self.menu.pointer_setting])

        else:
            i=self.origin_setting

            while i<self.origin_setting+self.max_setting:
                to=self.menu.list_setting[i]
                if self.menu.name=="browser" and os.path.isdir(self.menu.path+to)==True:
                    to=">"+to
                self.list_setting.append(to)
                i+=1

    def set_pointer_setting(self):# set pointer & origin

        if self.menu.pointer_setting==0: # if 'min'
            self.origin_setting=0
            self.pointer_setting_display=0

        elif self.menu.pointer_setting==len(self.menu.list_setting)-1: # if 'max'
            self.pointer_setting_display=self.max_setting-1
            self.origin_setting=len(self.menu.list_setting)-self.max_setting

        elif self.menu.pointer_setting>self.pointer_setting:# if '+'
            if self.pointer_setting<self.max_setting-1:
                self.pointer_setting_display+=1
            elif self.pointer_setting_display==self.max_setting-1:
                self.origin_setting+=1

        elif self.menu.pointer_setting<self.pointer_setting:# if '-'
            if self.pointer_setting_display>0:
                self.pointer_setting_display-=1
            elif self.pointer_setting_display==0:
                self.origin_setting-=1

        print("pointer_setting",self.pointer_setting,self.menu.pointer_setting,self.origin_setting,self.pointer_setting_display)
        self.pointer_setting=self.menu.pointer_setting

