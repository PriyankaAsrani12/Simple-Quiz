import json
from tkinter import *
from tkinter import messagebox
import random
from DbHelper import *
import bargraph

class HomePage:
    def __init__(self,root):
        self.root=root
        self.frame = Frame(self.root, height=600, width=600, bg="#078ca3")
        self.frame.pack(padx=5,pady=5)
        self.lab = Label(self.frame, text="WELCOME\n\n\nType of login\n\nYou can login in admin account if you want to create a new user account\nYou can login in user account if you want to take the quiz",bg="#078ca3",fg="white",font=("Consolas", 10 ,"bold"))
        self.lab.grid(row=1, column=1, columnspan=3, padx=30, pady=20)
        self.admin_login_b=Button(self.frame,text="Admin login",command=lambda :self.login("admin"),bg="white",font=("Consolas", 10))
        self.admin_login_b.grid(row=2,column=1,padx=20,pady=20)
        self.user_login_b=Button(self.frame,text="User login",command=lambda :self.login("user"),bg="white",font=("Consolas", 10))
        self.user_login_b.grid(row=2,column=2,padx=20,pady=20)
        self.frame.grid_propagate(0)

    def login(self,login_type):
        self.frame.destroy()
        self.frame = Frame(self.root, height=600, width=600, bg="#078ca3")
        self.frame.pack(padx=5,pady=5)
        self.lab=Label(self.frame,width=50,text="Enter the details below to login",bg="#078ca3",fg="white",font=("Consolas", 10))
        self.lab.grid(row=0,column=1,columnspan=3,padx=10,pady=10)
        self.l1=Label(self.frame,width=20,text="Enter Username: ",bg="#078ca3",fg="white",font=("Consolas", 10))
        self.e_username=Entry(self.frame,width=30,fg='black',bg='white')
        self.l2 = Label(self.frame, width=20, text="Enter Password: ",bg="#078ca3",fg="white",font=("Consolas", 10))
        self.e_pwd = Entry(self.frame, width=30, fg='black', bg='white',show='*')
        self.l1.grid(row=1,column=1,padx=10,pady=10)
        self.l2.grid(row=2,column=1,padx=10,pady=10)
        self.e_username.grid(row=1,column=2,padx=10,pady=10)
        self.e_pwd.grid(row=2,column=2,padx=10,pady=10)
        self.b1=Button(self.frame,text="Submit",height=2,width=10,command=lambda :self.authenticate(login_type),bg="white",font=("Consolas", 10))
        self.b1.grid(row=3,column=1,padx=10,sticky='e',pady=10)
        self.b2 = Button(self.frame, text="Reset",height=2,width=10,command=lambda : self.reset(),bg="white",font=("Consolas", 10))
        self.b2.grid(row=3, column=2,padx=10,sticky='w',pady=10)
        self.frame.grid_propagate(0)

    def authenticate(self,login_type):
        user=self.e_username.get()
        pwd=self.e_pwd.get()
        params=(user,pwd)
        if login_type=="admin":
            query="Select * from practice_admin where Username='%s' and Password='%s'"
        else:
            query="Select * from practice_user where Username='%s' and Password='%s'"
        res=get_data(query,params)
        print(res)
        if(res is None or len(res)==0):
            messagebox.showwarning('Incorrect credentials','The username and password entered does not match. Please re-enter')
            self.reset()
        elif(login_type=="admin"):
            self.admin_page(user)
        else:
            self.user_page(user)

    def user_page(self,username):
        user = self.e_username.get()
        pwd = self.e_pwd.get()
        self.frame.destroy()
        self.frame = Frame(self.root, height=600, width=600)
        self.frame.pack(padx=5,pady=5)
        self.frame.grid_propagate(0)
        self.l_account = Label(self.frame, text=f"USER ACCOUNT\n")
        self.l_account.grid(row=0, column=0, pady=40)
        self.l_name = Label(self.frame, text=f"Welcome, {username}")
        self.l_name.grid(row=0, column=1, pady=20,sticky='e')
        self.frame=Frame(self.root,height=600,width=600,command=self.Quiz(user,pwd))
        self.frame.pack()
        self.frame.grid_propagate(0)
        self.frame.destroy()


    def admin_page(self,username):
        self.frame.destroy()
        self.frame = Frame(self.root, height=600, width=600,bg="#078ca3")
        self.frame.pack(padx=5,pady=5)
        self.frame.grid_propagate(0)
        self.l_account=Label(self.frame,text=f"ADMIN ACCOUNT\n",bg="#078ca3",fg="white",font=("Consolas", 15))
        self.l_account.grid(row=0,column=0,pady=20)
        self.l_name=Label(self.frame,text=f"\nWelcome, {username}",bg="#078ca3",fg="white",font=("Consolas", 12))
        self.l_name.grid(row=0,column=1,pady=20)
        self.lab=Label(self.frame,width=50,text="Enter below details to create a new user account",bg="#078ca3",fg="white",font=("Consolas", 10))
        self.lab.grid(row=1,column=0,columnspan=3,padx=10,pady=10)
        self.l1=Label(self.frame,width=20,text="Enter username: ",bg="#078ca3",fg="white",font=("Consolas", 10))
        self.e_username=Entry(self.frame,width=30,fg='black',bg='white')
        self.l2 = Label(self.frame, width=20, text="Enter password: ",bg="#078ca3",fg="white",font=("Consolas", 10))
        self.e_pwd = Entry(self.frame, width=30, fg='black', bg='white',show='*')
        self.l1.grid(row=2,column=1,padx=10,pady=10)
        self.l2.grid(row=3,column=1,padx=10,pady=10)
        self.e_username.grid(row=2,column=2,padx=10,pady=10)
        self.e_pwd.grid(row=3,column=2,padx=10,pady=10)
        self.b1=Button(self.frame,text="Create user",height=2,width=12,bg="white",font=("Consolas", 10),command=lambda :self.create_user())
        self.b1.grid(row=4,column=1,columnspan=2,padx=10)

    def create_user(self):
        user=self.e_username.get()
        pwd=self.e_pwd.get()
        query="Insert into practice_user(Username,Password) Values('%s','%s')"
        params=(user,pwd)
        execute_query(query,params)
        messagebox.showinfo('Success!',f'User with username {user} created successfully. Redirecting you to login screen')
        self.login("user")


    def reset(self):
        print("Reset called")
        self.e_username.delete(0,END)
        self.e_pwd.delete(0, END)
        self.l3.destroy()
        self.l4.destroy()

    def Quiz(self,user,pwd):
        self.frame.destroy()

        u=user
        def dbresult(score):
            query="SELECT r.* FROM practice_user pu JOIN result r ON pu.AdminId=r.AdminId"
            params=None
            execute_query(query,params)
            query1 = "SELECT AdminId FROM practice_user WHERE Username='%s'"
            params1 = u
            admindata=get_data(query1, params1)
            for i in admindata:
                admindata=i
            query2 = "INSERT INTO result(Score,Test_date,AdminId) VALUES('%d','2020-04-05','%d')"
            params2 = (score,admindata)
            execute_query(query2,params2)

        global questions
        global answers_choice


        with open('C:\\Users\\Vikrant\\PycharmProjects\\CollegeProjectQuiz\\data.json', encoding="utf8") as f:
            data = json.load(f)


        questions = [v for v in data[0].values()]
        answers_choice = [v for v in data[1].values()]
        global answers
        answers = [1, 1, 3, 1, 3, 1, 2, 1, 3, 3, 2, 1, 3, 2]

        global user_answer
        user_answer = []
        global indexes
        indexes = []


        def gen():
            global indexes
            while (len(indexes) < 10):
                x = random.randint(0, 9)
                if x in indexes:
                    continue
                else:
                    indexes.append(x)

        def showresult(score):
            lblquestion.destroy()
            r1.destroy()
            r2.destroy()
            r3.destroy()
            r4.destroy()
            labelimage = Label(root, background="white", border=0)
            labelimage.pack(pady=0)
            labelresulttext = Label(root, font=("Consolas", 20), background="white")
            labelresulttext.pack(pady=0)
            graph = Button(root,height=2,text="Show Progress",width=15,bg="white",font=("Consolas", 10),command=bargraph.showgraph)
            graph.pack(pady=10)
            if score >= 80:
                img = PhotoImage(file="C:\\Users\\Vikrant\\PycharmProjects\\CollegeProjectQuiz\\great.png")
                labelimage.configure(image=img,pady=0)
                labelimage.image = img
                labelresulttext.configure(text=f"You are Excellent!!\nYour score is {score}",pady=0)
            elif (score >= 40 and score < 80):
                img = PhotoImage(file="C:\\Users\\Vikrant\\PycharmProjects\\CollegeProjectQuiz\\ok.png")
                labelimage.configure(image=img,pady=0)
                labelimage.image = img
                labelresulttext.configure(text=f"You can do better!\nYour score is {score}",pady=0)
            else:
                img = PhotoImage(file="C:\\Users\\Vikrant\\PycharmProjects\\CollegeProjectQuiz\\bad.png")
                labelimage.configure(image=img,pady=0)
                labelimage.image = img
                labelresulttext.configure(text=f"You have to work hard!!\nYour score is {score}",pady=0)
            dbresult(score)



        def calc():
            global indexes, user_answer, answers, score
            x = 0
            score = 0
            for i in indexes:
                if (user_answer[x] == answers[i]):
                    score += 10
                x += 1
            print(score)
            showresult(score)


        global ques
        ques = 1

        def selected():
            global radiovar, user_answer
            global lblquestion, r1, r2, r3, r4
            global ques
            x = radiovar.get()
            user_answer.append(x)
            radiovar.set(-1)
            if ques < 10:
                lblquestion.config(text=questions[indexes[ques]])
                r1["text"] = answers_choice[indexes[ques]][0]
                r2["text"] = answers_choice[indexes[ques]][1]
                r3["text"] = answers_choice[indexes[ques]][2]
                r4["text"] = answers_choice[indexes[ques]][3]
                ques += 1
            else:
                print(indexes)
                print(user_answer)
                calc()

        def startquiz():
            global lblquestion, r1, r2, r3, r4
            lblquestion = Label(root, text=questions[indexes[0]], font=("Consolas", 16), width=600, justify="center",
                                wraplength=500, background="#078ca3",fg="white")
            lblquestion.pack(pady=50)
            global radiovar
            radiovar = IntVar()
            radiovar.set(-1)
            r1 = Radiobutton(root, text=answers_choice[indexes[0]][0], font=("Times", 12), value=0, variable=radiovar,
                             command=selected, background="white")
            r1.pack(pady=2)
            r2 = Radiobutton(root, text=answers_choice[indexes[0]][1], font=("Times", 12), value=1, variable=radiovar,
                             command=selected, background="white")
            r2.pack(pady=2)
            r3 = Radiobutton(root, text=answers_choice[indexes[0]][2], font=("Times", 12), value=2, variable=radiovar,
                             command=selected, background="white")
            r3.pack(pady=2)
            r4 = Radiobutton(root, text=answers_choice[indexes[0]][3], font=("Times", 12), value=3, variable=radiovar,
                             command=selected, background="white")
            r4.pack(pady=2)

        def startIsPressed():
            labeltext.destroy()
            labelinstruction.destroy()
            labelrules.destroy()
            labelimage.destroy()
            btnStart.destroy()
            gen()
            startquiz()

        img1 = PhotoImage(file="C:\\Users\\Vikrant\\PycharmProjects\\CollegeProjectQuiz\\quiz.png")
        labelimage = Label(root, image=img1, bg="white")
        labelimage.image = img1
        labelimage.pack(pady=(0, 0))

        labeltext=Label(root,text="QUIZ",font=("Comic sans MS",24,"bold"),background="white")
        labeltext.pack(pady=(20,50))

        labelinstruction=Label(root,text="Read the Rules and\nClick Start Once You are raedy",background="white",font=("Consolas",14),justify="center")
        labelinstruction.pack(pady=(10,5))

        labelrules=Label(root,text="This quiz contains 10 questions and there is no time limit\nOnce you select a radio button that will be a final choice\nHence think before you select\nYou’ll get 10 point for each correct answer\nAt the end of the quiz, you’ll receive a total score\nThe maximum score is 100\nGood luck!",width=100,font=("Times",14),background="#078ca3",foreground="white")
        labelrules.pack()

        btnStart = Button(root, height=2, width=7, bg="lightgray", fg="black", font=("Consolas", 10), text="Start >>",command=startIsPressed)
        btnStart.pack(pady=(10, 10))

root=Tk()
root.title("QUIZ")
root.geometry("800x800")
root.config(background="white")
root.resizable(0,0)
HomePage(root)
root.mainloop()