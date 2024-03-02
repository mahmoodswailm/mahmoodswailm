import customtkinter as ctk

class hh:
    def __init__(self):
        self.win = ctk.CTk()
        self.win.geometry("400x600")
        self.win.title("to do list")
        self.label = ctk.CTkLabel(self.win,text="hi\nTodays goals",font=("Arail",15))
        self.label.pack()

        # self.lable = ctk.CTkLabel(self.win,text='hi').grid(row=1,column =1)
        
        
        

        self.win.mainloop()





