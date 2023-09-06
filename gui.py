from tkinter import *
class Calculator:
    def __init__(self):
        #window creation and configuration
        self.window=Tk()
        self.window.title("Calculator")
        self.window.geometry("500x500")
        self.expression=""# default value in display
        #label heading
        self.label=Label(self.window,text="CALCULATOR",font=('Arial',25,'bold'),fg="red")
        self.label.pack()
        #two frames one for number display one for buttons
        self.display_frame=Frame(self.window,height=221)
        self.button_frame=Frame(self.window,bg="#9cffee")
        self.display_frame.pack(expand=True,fill="both")
        self.button_frame.pack(expand=True,fill="both")
        for x in range(1,5):
            self.button_frame.rowconfigure(x,weight=1)
            self.button_frame.columnconfigure(x,weight=1)
        #display label as 0 in default in display frame
        self.display_label=Label(self.display_frame,text=self.expression,anchor=E,bg="#F5F5F5",padx=24,font=('Arial',40,"bold"))
        self.display_label.pack(expand=True,fill="both")
        #dict for numericals
        self.buttons= {
            7:(1,1),8:(1,2),9:(1,3),
            4:(2,1),5:(2,2),6:(2,3),
            1:(3,1),2:(3,2),3:(3,3),
            '.':(4,1),0:(4,2)
        }
        #dict for operators
        self.operations= {
            "+":"+","-":"-","/":"\u00F7","*":"\u00D7"
        }
        #called functions for creating buttons
        self.create_button()
        self.create_operator()
        self.create_C()
        self.create_eq()
        self.bind_keyBoard()
        self.window.mainloop()
    
    #function to create button for numbers
    def create_button(self):
        for digit,grids in self.buttons.items():
            button=Button(self.button_frame,text=str(digit),bg="#342D7E",fg="#FFF9E3",font=('Arial',24,'bold'),width=4,command=lambda x=digit: self.update_value(x)).grid(row=grids[0],column=grids[1],sticky=NSEW)
    #function to create operator buttons
    def create_operator(self):
        i=1
        for operator, symbol in self.operations.items():
            op_button=Button(self.button_frame,text=symbol,font=('Arial',22),bg="#C32148",fg="#FFF9E3",command=lambda x=operator:self.update_operator(x))
            op_button.grid(row=i,column=4,sticky=NSEW)
            i+=1
    #function to create clear button
    def create_C(self):
        button=Button(self.button_frame,text="C",bg="#FD1C03",fg="#FFF9E3",font=('Arial',24,'bold'),width=4,command= self.update_C).grid(row=4,column=3,sticky=NSEW)
    #function to create equalto button
    def create_eq(self):
        button=Button(self.button_frame,text="=",bg="#16F529",fg="#FFF9E3",font=('Arial',22,'bold'),width=4,command=self.evaluate).grid(row=1,column=5,rowspan=4,sticky=NSEW)
    #enables us to use keyboard to type values
    def bind_keyBoard(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.buttons:
            self.window.bind(key,lambda event, digit=key: self.update_value(digit))
        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.update_operator(operator))
    #set numerical values in label when button clicked
    def update_value(self,value):
        self.expression=self.expression+str(value)
        self.display_label.config(text=self.expression)
    #set operator in label when clicked
    def update_operator(self,operator):
        self.expression+=operator
        self.display_label.config(text=self.expression)
    #clear values when C clicked
    def update_C(self):
        self.expression=""
        self.display_label.config(text=self.expression)
    #to perform arithemetic operations
    def evaluate(self):
        try:
            self.res=str(eval(self.expression))
        except:
            self.res="Error"
        self.display_label.config(text=self.res[:10])
 #object created for class calculator       
calculator=Calculator()


