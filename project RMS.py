#!/usr/bin/env python
# coding: utf-8

# In[32]:


# Virtual Coffee Shop:


class RMS:
    def __init__(self,restaurant_name,restaurant_menu):
        self.rest_name=restaurant_name
        self.menu=restaurant_menu
        self.user_order=" "
        self.no_order=0
        self.user_pay=0
        self.wlcm_msg=(f"'{self.rest_name}'")
    
    def welcome_user(self):
        self.bill=0
        #Welcome User
        print('Welcome to the',self.rest_name.title())
        print('*'*50)
        
    
    def display_menu(self): 
        #Display Menu 
        print('Menu:')
        for i in self.menu:
            print(i.title(),":","₹",self.menu[i])
        print('*'*50)
        
   
    def take_order(self):
        #Take order
        self.user_order=input('Please Place Your Order Here:').title()
        

    def prepare_order(self):
        self.no_order=int(input("How Many Number Of Order You Want:")) 
        #Preparing Order
        
        print('Preparing Your Order')
        import time
        time.sleep(0.5)
        
    
    def serve_order(self): 
        #Serve Order
        print('Your order is ready'.title())
        print('Please Enjoy Your',self.user_order)
        self.bill=self.bill+(self.menu[self.user_order]*self.no_order)
    
    
    
    def repeat_order(self):
        self.display_menu()
        self.take_order()
        if self.user_order in self.menu:
            self.prepare_order()
            self.serve_order()
        else:
            print('Invalid Order')
            self.repeat_order()
           
    
    
    def display_bill(self):
        print("---------------bill receipt---------------".title())
       #Display Bill
        print("final bill:","₹",self.bill)   
        print("--------------payment process-------------".title()) 
    
        
    
        
    def verify_payment(self): 
        #Take Payment
        self.user_pay=int(input('Please pay your bill here:₹'))
        while self.bill>self.user_pay:
            self.bill=self.bill-self.user_pay
            print('Payment Failed!')
            print('Please pay remaining amount:₹',self.bill)
            self.user_pay=int(input('Please pay your bill here:₹'))
        #if payment>bill return change
        if self.user_pay>self.bill:
            print('Here is your change:',"₹",self.user_pay-self.bill)
        else:
            pass
    
    
    
    def thank_user(self):
        #thank you
        print('Thank you for visiting our',self.rest_name.title())
        print('Please Visit Us Again')
    
    
    def order_process(self):
        self.welcome_user()
        self.display_menu()
        self.take_order()
        if self.user_order in self.menu:
            self.prepare_order()
            self.serve_order()
            want_more=input('Do you want to order anything else?:').title()
            while want_more=='Yes':
                self.repeat_order()
                want_more=input('Do you want to order anything else?:').title()    
            self.display_bill()
            self.verify_payment()
            self.thank_user()
        else:
            print('Invalid Order')
            self.order_process()

if __name__=="__main__":
    file=open('user input.txt')
    user_input=file.readlines() 
    rest_name=user_input[0].replace('\n','')
    food_name=user_input[1].replace('\n','').split(',')
    food_prices=[]
    for i in user_input[2].split(','):
        food_prices.append(int(i))
    menu=dict(zip(food_name,food_prices))
    cafe=RMS(rest_name,menu)


    
    #creating window:
    import tkinter as tk
    window=tk.Tk()
    window.geometry("500x500")
    window.title("Python Project") 
    tk.Label(window,text=cafe.wlcm_msg,font=("Helvetica",30),foreground="dark blue").place(x=70,y=70)
    tk.Label(window,text="*Please click on 'START' button for order -:",font=("Helvetica",15)).place(x=30,y=240)
    tk.Button(window,text="START",command=cafe.order_process,font=("Helvetica",20),width=18,background="green",foreground="white").place(x=100,y=310)
    window.mainloop()
        
    

   


# In[ ]:




