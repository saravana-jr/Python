from tkinter import *
from tkinter import ttk

class Covidapp:
    
    def __init__(self,master):
        
        self.Label=ttk.Label(master,text="Stay Home")
        self.Label.grid(row=0,column=0,columnspan=2)

        ttk.Button(master,text="India",command=self.India_case).grid(row=1,column=0)

        ttk.Button(master,text="America",command=self.America_case).grid(row=1,column=1)

    def India_case(self):
        self.Label.config(text="2.5lakh cases")

    def America_case(self):
        self.Label.config(text="10 lakh cases")

        

def main():
    
    root=Tk()
    app=Covidapp(root)
    root.mainloop()

if __name__=="__main__": main()
    
