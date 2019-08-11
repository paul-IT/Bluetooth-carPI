#!/usr/bin/python -*- coding: iso-8859-1 -*-
import Tkinter 
import os
import time
from Tkinter import *
from PIL import ImageTk, Image

class simpleapp_tk(Tkinter.Tk):
    def changesong(self):
        res = os.popen("sudo ./titlesong.sh").read()
	self.song.configure(text=res,font=("Courier", 20))
	self.after(5000,self.changesong)  
    #def temp(self):
	#temp= os.popen("vcgencmd measure_temp").read()
	#self.tempOK.configure(text=temp,font=("Courier", 10))
	#self.after(10000,self.temp)
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
	self.attributes('-fullscreen',True)
	quit_btn = Tkinter.Button(self, text='Exit :(', bg="black", fg="white", command=self.quit,height=2,width=10)
	quit_btn.pack(side=BOTTOM, padx=(325,1))
	load = Image.open("./images/pi.png")
        render = ImageTk.PhotoImage(load)
        self.img = Label(self, image=render)
        self.img.image = render
        #self.img.place(relwidth=1, relheight=1)
	self.img.pack(side=TOP,pady=(15,1),padx=(25,1)) #side=TOP, expand=True)
	self.configure(background='black')
	res = os.popen("sudo ./titlesong.sh").read()
        self.song = Tkinter.Label(self,text=res,bg="black",fg="red")
        self.song.pack(side=RIGHT,padx=(1,75),pady=(15,1))
	self.song.configure(text=res,font=("Courier", 20))
    	self.after(5000,self.changesong)
	#temp= os.popen("vcgencmd measure_temp").read()
        #self.tempOK = Tkinter.Label(self,text=temp,bg="black",fg="green")
        #self.tempOK.pack()
        #self.tempOK.configure(text=temp,font=("Courier", 10))
        #self.after(10000,self.temp)		    
    def initialize(self):
        self.grid()
  	res = os.popen("sudo ./bluetooth.sh").read()      
	#button = Tkinter.Button(self,text=u"Musique",
        #                        command=self.OnButtonClickSEE,bg="#DF013A", fg="red", height = 5, width = 30)
#        button2 = Tkinter.Button(self,text=u"BT",
#                                command=self.OnButtonClickSEE, bg="#0080FF", fg="black", height = 1, width = 10)
        button3 = Tkinter.Button(self,text=u"Pause",
                                command=self.OnButtonClickPause, bg="#B40431", fg="black", height = 2, width = 11)
 	button4 = Tkinter.Button(self,text=u"Next", #image=photo,compound="top",
                                command=self.OnButtonClickNext, bg="#B40431", fg="black", height = 2, width = 11)       
	#button3 = Tkinter.Button(self,text=u"Pause",
        #                        command=self.OnButtonClickPause, bg="white", fg="black", height = 2, width = 15)
	
	button5 = Tkinter.Button(self,text=u"Previous",
                                command=self.OnButtonClickPrevious, bg="#B40431", fg="black", height = 2, width = 11)
	button5.pack(side = LEFT,pady=(300,1),expand=True) #,padx=(150,1),pady=(400, 1)) # expand=True)
        button3.pack(side= LEFT,pady=(300,1),expand=True)
        button4.pack(side= LEFT,pady=(300,1),expand=True) #,padx=(150,1), pady=(400, 1)) #, expand=True)

	#temp= os.popen("vcgencmd measure_temp").read()
	#tempOK = Tkinter.Label(self,text=res,bg="black",fg="green")
        #self.tempOK.pack(side=BOTTOM)
        #temp= os.popen("vcgencmd measure_temp").read()
        #tempOK = Tkinter.Label(self,text=temp,bg="black",fg="green")
        #tempOK.pack(side=TOP)
        #tempOK.configure(text=temp,font=("Courier", 10))
	#self.after(50000,self.temp)
	#self.tempOK.configure(text=res,font=("Courier", 20))
    def BT1(self):
	os.system("sudo ./deviceBT1.sh")
    def BT2(self):
	os.system("sudo ./deviceBT2.sh")
    def OnButtonClickPause(self):
	os.system("sudo ./playpause.sh")
    def OnButtonClickPrevious(self):
        os.system("sudo ./Previous.sh")
    def OnButtonClickNext(self):
	os.system("sudo ./Next.sh")
    
if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('carPI')
    app.mainloop()   


