#importing lib

import tkinter as tk
import random
from tkinter import messagebox
import time
from tkinter import font
from tkinter import ttk
from PIL import Image , ImageTk
import  customtkinter as ctk





# Definiting Funtions

def reverse():
      Current_container.destroy() 
      home_screen()

def load_bg():
    global image
    global home_image
    global image_canva
    image=Image.open("CalcSmart\White_numbers.jpg").resize((800,400))
    home_image=ImageTk.PhotoImage(image)
    image_canva= Current_container.create_image(400,200, image=home_image)

def submit_back():
    global submit_tk

    submit_image=Image.open("CalcSmart\Submit.png").resize((25,25))
    submit_tk=ImageTk.PhotoImage(submit_image)

    global submit
    global submit_canva

    Submit=tk.Button(Current_container, text= " SUBMIT ", width=89, height=24,
                     font=15, border=5, image=submit_tk, compound="right" , 
                     command= answer_checker, background="white")
    submit_canva= Current_container.create_window(340,190, window=Submit)

    global Back_tk

    Back_image=Image.open("CalcSmart\Back.png").resize((25,25))
    Back_tk=ImageTk.PhotoImage(Back_image)

    global Back
    global Back_canva

    Back=tk.Button(Current_container, border=5, image=Back_tk, 
                     command= operator_type, background="white")
    Back_canva= Current_container.create_window(450,190, window=Back)



def ans_clear(event):
    ans_input.delete(0,tk.END)
    ans_input.config(fg="black")

def quo_clear(event):
    ans_quo.delete(0,tk.END)
    ans_quo.config(fg="black")

def rem_clear(event):
    ans_rem.delete(0,tk.END)
    ans_rem.config(fg="black")


def no_tab():

    continue_container. destroy()
    
    global no_container

    global Current_container
    no_container=tk.Canvas(root)
    no_container.pack(fill="both", expand=True)
    Current_container = no_container
    load_bg()

    

    result=tk.Label(no_container, text="Your Evaluation", font=("Georgia", 20))
    result.place(x=265, y=100)

    t_que=tk.Label(no_container, text="Total Number of questions asked:", font=10 )
    t_que.place(x=265,y=150)

    t_sco=tk.Label(no_container, text=t_score, font=10 )
    t_sco.place(x= 565,y=150)

    o_que=tk.Label(no_container, text="Total Number of questions answered:", font=10 )
    o_que.place(x=265,y=180)

    o_sco=tk.Label(no_container, text=o_score, font=10 )
    o_sco.place(x=597,y=180)

    s_line=tk.Label(no_container, text="***************************************************", font=10)
    s_line.place(x=240, y=210)





def  continue_exit():
    global continue_container

    continue_container=tk.Canvas(root)
    continue_container.pack(fill="both", expand=True)

    global Current_container
    Current_container=continue_container
    load_bg()


    yes_no=tk.Label(continue_container, text="Do you want to continue?", font=("Georgia", 20))
    yes_no.place(x=265, y=100)

    yes=tk.Button(continue_container, text="Yes", font=10, width=5, border=3, command=operator_type)
    yes.place(x=325,y=165)

    no=tk.Button(continue_container, text="No", font=10, width=5, border=3, command=no_tab )
    no.place(x=445, y=165)

    



def next_question():
        if i<count:
            Current_definition()
        else:
            Current_container.destroy()
            continue_exit()

def answer_checker():

    global t_score
    t_score+=1

    global o_score
    if Current_definition==generate_question_div:
        global ans_quo
        global ans_rem
        try:
            ans_quo=int(ans_quo.get())

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")
            ans_quo.delete(0,tk.END)
            ans_quo.focus()

        try:
            ans_rem=int(ans_rem.get())

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")
            ans_rem.delete(0,tk.END)
            ans_rem.focus()

        #Checks whether the answer is correct or not
        if ans_quo==correct_quo and ans_rem==correct_rem:
            o_score+=1
            messagebox.showinfo(" Corrct!", "                                  ")
            next_question()
        else:
            messagebox. showinfo("Incorrect!")
            messagebox. showinfo("IQuotient is", correct_quo)
            messagebox. showinfo("Remainder is", correct_rem)
            next_question()

    else:    
        #Checks whether the answer enetered by user is a int() or not
        global ans
        try:
            ans=int(ans_input.get())

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")
            ans_input.delete(0,tk.END)
            ans_input.focus()

        #Checks whether the answer is correct or not
        if ans==correct_ans:
            o_score+=1
            messagebox.showinfo(" Corrct  answer!")
            next_question()
        else:
            messagebox. showinfo("Incorrect!", correct_ans)
            next_question()

#Fuction to generate questions of Addition
def generate_question_add():

    Add_container.update()

    global i
    i+=1

    num1=random.randint(10000,100000)
    num2= random.randint(10000,100000)

    global correct_ans
    correct_ans= num1+num2

    blank_line=tk.Label(Add_container, text='', font=20)
    # blank_line.place(row=0 ,sticky='w', pady=50)
    # Back.grid(row=4, column=1, sticky='snew', padx=20)
    #Question
    question= tk.Label( Add_container, text= (num1,"+",num2), font= 50)
    question.place( x=320, y=100)

    #Answer
    global ans_input
    ans_input=tk.Entry(Add_container, width=32, border=5)
    ans_input.insert(0,"Answer")
    ans_input.config(fg="grey")
    ans_input.place(x=284, y=135)

    ans_input.bind("<FocusIn>", ans_clear)

    blank_line1=tk.Label(Add_container, text='', font=10)
    # blank_line1.grid(row=3 ,columnspan=2,sticky='snew', pady=5)

    global Current_definition
    Current_definition= generate_question_add
    
    submit_back()



#Function to generate questions of Subtractions
def generate_question_sub():
    Sub_container.update()

    global i

    num1=random.randint(10000,100000)
    num2= random.randint(10000,100000)
    if num1<num2:
        temp=num1
        num1=num2
        num2=temp

    i+=1
    question= tk.Label(Sub_container, text= (num1,"-",num2), font= 50)
    question.place( x=320, y=100)

    #Answer
    global ans_input
    ans_input=tk.Entry(Sub_container, width=32, border=5)
    ans_input.insert(0,"Answer")
    ans_input.config(fg="grey")
    ans_input.place(x=284, y=135)

    ans_input.bind("<FocusIn>", ans_clear)

    global correct_ans
    correct_ans= num1-num2

    global Current_definition
    Current_definition= generate_question_sub

    submit_back()


#Fuction to generate questions of Multiplication
def generate_question_pro():

    Pro_container.update()

    global i
    i+=1

    num1=random.randint(10,1000)
    num2= random.randint(10,1000)

    global correct_ans
    correct_ans= num1*num2

    question= tk.Label( Pro_container, text= (num1,"X",num2), font= 50)
    question.place( x=320, y=100)

    #Answer
    global ans_input
    ans_input=tk.Entry(Pro_container, width=32, border=5)
    ans_input.insert(0,"Answer")
    ans_input.config(fg="grey")
    ans_input.place(x=284, y=135)

    ans_input.bind("<FocusIn>", ans_clear)
    

    global Current_definition
    Current_definition= generate_question_pro

    submit_back()


#Fuction to generate questions of Division
def generate_question_div():

    Div_container.update()

    global i
    i+=1

    num1=random.randint(10000,100000)
    num2= random.randint(10,99)

    global correct_quo
    correct_quo= num1//num2

    global correct_rem
    correct_rem= num1%num2

    question= tk.Label(Div_container, text= (num1,"/",num2), font= 50)
    question.place( x=320, y=100)

    #Answer
    global ans_quo
    ans_quo=tk.Entry(Div_container, width=14, border=5)
    ans_quo.insert(0,"Quotient")
    ans_quo.config(fg="grey")
    ans_quo.place(x=284, y=135)

    ans_quo.bind("<FocusIn>", quo_clear)
    

    global ans_rem
    ans_rem=tk.Entry(Div_container, width=14, border=5)
    ans_rem.insert(0,"Remainder")
    ans_rem.config(fg="grey")
    ans_rem.place( x=400, y=135)

    ans_rem.bind("<FocusIn>", rem_clear)
    

    global Current_definition
    Current_definition= generate_question_div

    submit_back()


    
def Addition():
    
    
    #Creating new container for displaying problems of addition
    
    

    
    global Add_container
    Add_container=tk.Canvas(root)
    Add_container.pack(fill="both", expand=True)

    global Current_container
    Current_container=  Add_container

    load_bg()
    
    global i
    i=0

    

    Add_container.after(2000, count_checker)

    generate_question_add()

    

            


def Subtraction():
        
    #Creating new container for displaying problems of substraction


    global Sub_container
    Sub_container=tk.Canvas(root)
    Sub_container.pack(fill="both", expand=True)
    
    global Current_container

    global i
    i=0


    Current_container=  Sub_container
    load_bg()
        
    generate_question_sub()

 


def Product():

    #Creating new container for displaying problems of addition

    global Pro_container
    Pro_container=tk.Canvas(root)
    Pro_container.pack(fill="both", expand=True)
    
    global Current_container

    global i
    i=0

    Current_container= Pro_container
    load_bg()

    generate_question_pro()



def Division():

    global Div_container
    Div_container=tk.Canvas(root)
    Div_container.pack(fill="both", expand=True)
    
    global Current_container

    global i
    i=0

    Current_container= Div_container
    load_bg()

    generate_question_div()



def count_checker():

    #Checks whether the number entered by the user is a number or not
    global count
    global count_input

    if count_input=='':
        messagebox.showerror("Invalid Input", "Please enter a valid integer.")
        count_input.focus_force()
    
    else:

        try:
            count= int(count_input.get())
            Current_container.destroy()
            current_function()
            
            
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")
            count_input.delete(0,tk.END)
            count_input.focus_force()



def add_operator():   
    global current_function
    current_function=Addition
    count_checker()

def sub_operator():   
    global current_function
    current_function=Subtraction
    count_checker()

def pro_operator():   
    global current_function
    current_function=Product
    count_checker()

def div_operator():   
    global current_function
    current_function=Division
    count_checker()






def operator_type():
     global Current_container
     Current_container.destroy()

     global operator_container
     operator_container=tk.Canvas(root)
     operator_container.pack(fill='both', expand=True)

     Current_container=operator_container

     load_bg()

     #Operator Labels

     global op_rec
     op_rec=operator_container.create_rectangle(0,20,800,50, fill="white", width=0)

     global operator_choose
     global operator_canva

     operator_choose=ttk.Label(operator_container, text="✰ Enter the number of problems to be asked:", 
                               font=("Georgia",15), background="white", foreground="Blue")
     operator_canva=operator_container.create_window(220,35, window=operator_choose)

     global count_input
     global count_canva
     count_input=tk.Entry(operator_container, width=45, border=5)
     count_canva= operator_container.create_window(170, 63, window= count_input)

     global op_rec1
     op_rec1=operator_container.create_rectangle(0,120,800,150, fill="white", width=0)

     global question_count
     global question_canva

     question_count= tk.Label(operator_container, text="✰ Select the operator:", 
                              font=("Georgia",15), background="white", foreground="Blue")
     question_canva=operator_container.create_window(118,135, window=question_count)
     
     #Operators Buttons

     global add_sign
     global add_image
     add_sign=Image.open("CalcSmart\Add.jpg"). resize((30,30))
     add_image=ImageTk.PhotoImage(add_sign) 
    
     global Add
     global add_canva

     Add= tk.Button(operator_container, text=" ADDITION ", image=add_image, compound="right", 
                    border=5, font=("Georgia", 10), background="White", width=170, 
                      height=20, command= add_operator)
     add_canva= operator_container.create_window(113, 175, window=Add)

     global sub_sign
     global sub_image
     sub_sign=Image.open("CalcSmart\Sub.png").resize((30,30))
     sub_image=ImageTk. PhotoImage(sub_sign)

     global Subtract
     global sub_canva
     Subtract= tk.Button(operator_container, text=" SUBTRACTION ", image=sub_image, compound="right", 
                    border=5, font=("Georgia", 10), background="White", width=170, 
                      height=20, command= sub_operator)
     sub_canva=operator_container.create_window(113,215, window=Subtract)

     global pro_sign
     global pro_image
     pro_sign=Image.open("CalcSmart\mul.jpg").resize((30,30))
     pro_image=ImageTk. PhotoImage(pro_sign)

     global Multiply
     global pro_canva
     Multiply= tk.Button(operator_container, text=" PRODUCT ", image=pro_image, compound="right", 
                    border=5, font=("Georgia", 10), background="White", width=170, 
                      height=20, command= pro_operator)
     pro_canva=operator_container.create_window(113,255, window=Multiply)

     global div_sign
     global div_image
     div_sign=Image.open("CalcSmart\Div.png").resize((30,30))
     div_image=ImageTk. PhotoImage(div_sign)


     global Divide
     global div_canva
     Divide= tk.Button(operator_container, text=" DIVISION ", image=div_image, compound="right", 
                    border=5, font=("Georgia", 10), background="White", width=170, 
                      height=20, command=div_operator)
     div_canva=operator_container.create_window(113,295, window=Divide)

     global op_rec2
     op_rec2=operator_container.create_rectangle(20,97,500,350, width=20, outline= "white")

     global home_sign
     global home_image1
     home_sign=Image.open("CalcSmart\home.png").resize((50,50))
     home_image1=ImageTk. PhotoImage(home_sign)

     global home
     global home_canva
     home= tk.Button(operator_container, image=home_image1, 
                    border=5, command=reverse)
     home_canva=operator_container.create_window(635,330, window=home)



def home_screen():

    global Current_container

    home_container= tk.Canvas(root, width=800, height=400)
    home_container.place(x=0,y=0)

    Current_container=home_container

    load_bg()



#Defining font functions



# Labels
    global canva_rectangle
    canva_rectangle=home_container.create_rectangle(25,25,775,375, fill="Blue", width=0, stipple="gray12")

    global canva_rectangle1
    canva_rectangle1=home_container.create_rectangle(150,100,650,300, fill="White", width=1, outline="Blue")


    global intro1
    global intro2
    global intro3
    global intro4
    global intro5
    global intro_canva
    global intro_canva2
    global intro_canva3
    global intro_canva4
    global intro_canva5


    intro1= ttk.Label(home_container, text="✰ Practice Calclation at your ease.", 
                  font= ("Georgia", 13), background="White", foreground="Blue")
    intro_canva= home_container.create_window(295, 140-20, window=intro1)

    intro2= ttk.Label(home_container, text="✰ Select the arithmetic operator on your own.", 
                  font= ("Georgia", 13), background="White", foreground="Blue")
    intro_canva2= home_container.create_window(289+50, 165-20, window=intro2)


    intro3= ttk.Label(home_container, text="✰ Select the number of question on each operator.", 
                  font= ("Georgia", 13), background="White", foreground="Blue")
    intro_canva3= home_container.create_window(305+50, 170, window=intro3)

    intro4= ttk.Label(home_container, text="✰ At the end veiw the total number of questions attempted.", 
                  font= ("Georgia", 13), background="White", foreground="Blue")
    intro_canva4= home_container.create_window(339+50, 195, window=intro4)

    intro5= ttk.Label(home_container, text="✰ And number of question answered correctly.", 
                  font= ("Georgia", 13), background="White", foreground="Blue")
    intro_canva5= home_container.create_window(293+50, 220, window=intro5)


# #Buttons

    global ready_tk
    global Ready
    global Ready_canva

    ready_image=Image.open("CalcSmart\Ready.jpg").resize((42,35))
    ready_tk= ImageTk.PhotoImage(ready_image) 

    Ready= tk.Button(home_container, text=" BEGIN ", 
                 font= ("Georgia",10), image=ready_tk, compound= "left", 
                 border=5, command= operator_type, background="White", width=89, height=25 )

    Ready_canva=home_container.create_window(575,260, window= Ready)



# Initialising and assigning values to variables

global Current_container

t_score=0
o_score=0

# Graphical User Interface
root=tk.Tk()
root.geometry("800x400")
root.resizable(False,False)
root.title(" CalcSmart ")

home_screen()

root.iconbitmap("CalcSmart\Logo1.ico")






root.mainloop()
