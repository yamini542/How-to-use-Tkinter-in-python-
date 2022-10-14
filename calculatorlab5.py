# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 19:07:31 2022

@author: yamup
"""

import tkinter

class Calculator:
    
    def __init__(self):
        self.sumg=0
        self.sub=0
        self.reset=0
        #we are initializing variable equals to zero

        self.mw=tkinter.Tk()
        self.mw.title("AddandSub")
        """
        
        self.top_frame=tkinter.Frame(self.mw)
        self.mid_frame=tkinter.Frame(self.mw)
        self.bottom_frame=tkinter.Frame(self.mw)
        """
        
        self.Totallabel=tkinter.Label(self.mw,text="Total:" )
        self.Totallabel.pack(side="top")
        
        self.showresult=tkinter.StringVar()
        self.answer=tkinter.Label(self.mw,textvariable=self.showresult)
        self.answer2=tkinter.Entry(self.mw,textvariable=self.showresult,width=15)
        self.answer.pack(side="top")
        

        
        
        self.Enternumber=tkinter.Entry(self.mw,width=15, text = "0")
        self.Enternumber.pack(side="top")
        
        
        self.additionbutton=tkinter.Button(self.mw,text="+", command=self.Addition)
        self.additionbutton.pack(side="left")
        
        self.subtractionbutton=tkinter.Button(self.mw,text="-", command=self.Subtraction)
        self.subtractionbutton.pack(side="left")
        
        self.resetbutton=tkinter.Button(self.mw,text="reset",command=self.Reset)
        self.resetbutton.pack(side="left")
        self.showresult.set(0)



        tkinter.mainloop()
        
        
    def Addition(self):
        
        self.enternumber=int(self.Enternumber.get())
        self.answer21=int(self.answer2.get())
        
        if(self.answer21)==0:
            
        #while getting the number from the user it will be string but we cant do operations on string henc we need to convert that value to number either int or float
            self.sumg +=self.enternumber 
        #initially sum =0
            self.showresult.set(self.sumg)
            
            """ above condition do the addition if you enter new value """
        
        else:
            
            
            self.answer21 +=self.enternumber
            
            self.showresult.set(self.answer21)
            
            """ else condition do when the value is taken from the result if the enter value is not equal to zer o"""
        
        
        
    
    def Subtraction(self):
        
       
            
           self.enternumber=int(self.Enternumber.get())
           self.answer21=int(self.answer2.get())
           
           if(self.answer21==0):
               
               self.sub-=self.enternumber
               self.showresult.set(self.sub)
           else:
               
               self.answer21 -= self.enternumber
               self.showresult.set(self.answer21)
               
               """
               #what is the use of if and else condition here if we press only + and - it will do normally do addition
               or subtraction to the entry number if i click in between it should take the value from the 
               result and do addition or subtraciton to the entry value thats it
               
               """
                
     
            
    def Reset(self):
        
         self.showresult.set(0)
         self.Enternumber.delete(0,'end')
         
         self.sumg = 0
         self.sub=0
         
         """ 
         in reset function in result it will show zero all variable values equal to zero
         """
         
         

         
         
         #we are setting the value to zero as we are resetting it
         
         
    
        
        
Calculator()
        