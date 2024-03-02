import customtkinter as ctk
import sqlite3
import time
from test3 import hh



class Test:

    def __init__(self):
        
        self.win_login = ctk.CTk()
        self.win_login.geometry("800x400")
        self.win_login.resizable(False,False)


        self.label2 = ctk.CTkLabel(self.win_login,text="login to your todo list",font=("Arail",20))
        self.label2.pack()


        # en1 =ctk.StringVar()

        self.ent1 = ctk.CTkEntry(self.win_login,placeholder_text="user name")
        self.ent1.pack(pady =20)

        # en2= ctk.StringVar()
        self.ent2 = ctk.CTkEntry(self.win_login,placeholder_text="password")
        self.ent2.pack()

        self.label = ctk.CTkLabel(self.win_login,text=".....")
        self.label.pack(pady=15)

        ctk.CTkButton(self.win_login,text="login",command=self.log_in).pack(pady =10)
        ctk.CTkButton(self.win_login,text="Register",command=self.register).pack(pady=10)
        self.count = 0
        self.win_login.mainloop()


    
    def databas(self):
        self.conn = sqlite3.connect("m_information.db")
        self.c=self.conn.cursor()
        print("database is opened")
    
    
    def cls(self):
        self.conn.commit()
        self.conn.close()
        print("database closed")




    def log_in(self):
        
        self.databas()
        # time.sleep(1)
        
        # get user_name and password from user
        user_name = self.ent1.get().strip()
        password = self.ent2.get().strip()
        
        if user_name:
            self.c.execute(f"select user_name from information where user_name = '{user_name}'")
            data=self.c.fetchall()
            if data:
                
                if password:
                    self.c.execute(f"select password from information where user_name = '{user_name}'")
                    data2 = self.c.fetchone()
                    print("this passwords in user-name ",data2)
                    for pas in data2:
                        if password == pas: 
                        
                            # for pas in data :
                            #     if password in pas:
                            time.sleep(0.5)
                            
                            self.label.configure(text="successful login!")
                            
                            time.sleep(0.5)
                            time.sleep(0.5)
                            time.sleep(0.5)
                            self.cls()
                            print("from logging")
                            self.logging()
                            
                            break
                            
                        else:
                            self.label.configure(text="incorrect password!\n\n type the write password",text_color="red")
                            self.cls()
                            
                            break
                else:
                    self.cls()
                    
                    self.label.configure(text= "" )
                    time.sleep(0.25)
                    self.label.configure(text= "input you're password!" )
                    self.count+=1
                    
                    if self.count ==3:
                        self.label.configure(text= "please input you're password to get in \n\n one more and i will close the app" )
                    elif self.count==4:
                        self.label.configure(text= "ok by, you don't want to get in  " )
                        time.sleep(1)
                        self.win_login.destroy()
            
            
            else:
                self.label.configure(text="no such user name write it correct \n\n or register",text_color="red")
                self.cls()

                
        else:
                self.label.configure(text= "input your user_name" )
                self.cls()




    # where user_name = '{user_name}'
    def register(self):
        #open database
        self.databas()
        
        user_name= self.ent1.get()
        password= self.ent2.get()
        self.c.execute(f"select user_name, password from information where user_name = '{user_name}' ")
        data=self.c.fetchall()
        # loop on data
        if user_name and password:
            if not data:
                self.c.execute(f"insert into information(user_name,password) values('{user_name}','{password}')")
                #close database
                self.cls()

                self.label.configure(text="you're now registerd to to do list ",text_color= 'green')
                
                time.sleep(2)
                self.label.configure(text="logging",text_color= 'green')
                time.sleep(2)
                self.logging()
            
                
                
            else:
                #close database
                self.cls()
                time.sleep(1)
                self.label.configure(text="click login button",text_color= 'white')
                time.sleep(1)
                
                self.label.configure(text="you're already register login",text_color= 'white')
                

        else:
            self.cls()
            self.label.configure(text="please input you're user name and password to register",text_color= 'white')
            
            


    def logging(self):
        # time.sleep(1)
        self.label.configure(text= "logging to you're todo list")
        time.sleep(2)
        self.win_login.destroy()
        # time.sleep(3)
        hh()







# class To_dolist:
#     def __init__(self) -> None:


        
#         self.win = ctk.CTk()
#         self.win.geometry("400x600")
#         self.win.title("to do list")
#         self.win.resizable(False,False)
        
#         self.label = ctk.CTkLabel(self.win,text=f"hi {Test.user_name}",font=("Arail",20))
#         self.label.pack()
        
#         self.entry = ctk.StringVar()
#         self.entry1 = ctk.CTkEntry(self.win,textvariable=self.entry)
#         self.entry1.pack()

#         self.entry1.get
#         self.b = ctk.CTkButton(self.win,text="sdf")
#         self.b.pack()

#         self.win.mainloop()


        



if __name__ == "__main__":
    

    Test()
