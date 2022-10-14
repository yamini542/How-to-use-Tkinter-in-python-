# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 13:03:09 2022

@author: S21147160
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 11:49:24 2022

@author: S21147160
"""

import tkinter

class BMI:
    def __init__(self):
        
        self.mw=tkinter.Tk()
        #mw is main window we can give any name here but this is for a windown to open
        
        
        self.weightlabel=tkinter.Label(self.mw,text="Weight")
        self.weightentry=tkinter.Entry(self.mw, width=15)
        self.weightlabel.pack(side="top")
        self.weightentry.pack(side="top")
        
        self.heightlabel=tkinter.Label(self.mw,text="Height")
        self.heightentry=tkinter.Entry(self.mw,width=15)
        self.heightlabel.pack(side="top")
        self.heightentry.pack(side="top")
        
        self.resultlabel=tkinter.StringVar()
        #in resultlabel where we are going to show the result dynamically
        self.answer=tkinter.Label(self.mw,textvariable=self.resultlabel)
        #that resultlabel is a label so given abpve coding
        #where we set result label to get self bmi value so given set bmi to get that value into the resultlabel
        self.answer.pack(side="top")
        #pack is for display positions and showing the window
        
        
        self.CalculateButton=tkinter.Button(self.mw,text="calculate BMI", command=self.get_bmi)
        self.CalculateButton.pack(side="top")
        
        
        tkinter.mainloop()
        #main loop is mandatory for calling the loop
                                            
    def get_bmi(self):
        self.weight=self.weightentry.get()
        self.height=self.heightentry.get()
        
        self.bmi=float(self.weight)/float(self.height)*float(self.height)
        #converting string to float because where we are taking a values from the label its a string so we can not multipy that so we need to type cast the values
        self.resultlabel.set(self.bmi)
        
BMI()
        
        





















































































































