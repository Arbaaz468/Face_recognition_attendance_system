from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1330x700+0+0")
        self.root.title("Face Recognition System")
        
        #=====================variables======================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        img = Image.open((r"clg_img\university1.jpg"))
        img = img.resize((50,50),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        #bg_image
        img1 = Image.open((r"clg_img\university.jpg"))
        img1 = img1.resize((1330,700),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=0,width=1330,height=700)

        #first label
        f_lbl = Label(bg_img,image=self.photoimg)
        f_lbl.place(x=1200,y=0,width=100,height=100)

        title_lbl = Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("time new roman",20,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1330,height =50)

        main_frame = Frame(bg_img,bd=2)
        main_frame.place(x=5,y=55,width=1310,height=630)
        
        #left label frame
        
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=620,height=610)
        
        img_left = Image.open(r"clg_img\clg.jpg")
        img_left = img_left.resize((620,90),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage((img_left))
        
        f_lbl = Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=605,height=90)
        
        #Current Course Frame
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=95,width=605,height=120)
        
        
        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","CSE","ECE","Mechanical","Electrical","Civil")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)
        
        
        #Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        course_combo["values"]=("Select Course","B.Tech","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        #Year
        y_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        y_label.grid(row=1,column=0,padx=10,sticky=W)
        
        y_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        y_combo["values"]=("Select Year","1","2","3","4")
        y_combo.current(0)
        y_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        #Semester
        s_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        s_label.grid(row=1,column=2,padx=10,sticky=W)
        
        s_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly")
        s_combo["values"]=("Select Semester","Semester-I","Semester-II")
        s_combo.current(0)
        s_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        #Class Student Information
        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        class_Student_frame.place(x=5,y=220,width=605,height=350)
        
        
        #Student ID
        studentID_label=Label(class_Student_frame,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        studentID_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=17,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Student Name
        student_name_label=Label(class_Student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        student_name_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=17,font=("times new roman",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
         #Class division
        div_label=Label(class_Student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        #div_entry=ttk.Entry(class_Student_frame,textvariable=self.var_div,width=17,font=("times new roman",12,"bold"))
        #div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=15,state="readonly")
        div_combo["values"]=("Select Division","A","B","C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
          #Roll No
        R_label=Label(class_Student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        R_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        R_entry=ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=17,font=("times new roman",12,"bold"))
        R_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
          #Gender
        G_label=Label(class_Student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        G_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        #G_entry=ttk.Entry(class_Student_frame,textvariable=self.var_gender,width=17,font=("times new roman",12,"bold"))
        #G_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        g_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=15,state="readonly")
        g_combo["values"]=("Male","Female","Other")
        g_combo.current(0)
        g_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)
        
          #DOB
        dob_label=Label(class_Student_frame,text="Date of Birth:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        dob_entry=ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=17,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
         #EMAIL
        email_label=Label(class_Student_frame,text="EMAIL:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=17,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
         #Phone No
        p_no_label=Label(class_Student_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        p_no_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        p_no_entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=17,font=("times new roman",12,"bold"))
        p_no_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        #Address
        add_label=Label(class_Student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        add_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        add_entry=ttk.Entry(class_Student_frame,textvariable=self.var_address,width=17,font=("times new roman",12,"bold"))
        add_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        #Teacher Name
        t_name_label=Label(class_Student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
        t_name_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        t_name_entry=ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=17,font=("times new roman",12,"bold"))
        t_name_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        #Radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,text="Take a photo Sample",variable=self.var_radio1,value="Yes")
        radiobtn1.grid(row=5,column=0,padx=10,pady=5)
         
        
        
        radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1,padx=10,pady=5)
        
        #Button Frame
        
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=10,y=240,width=582,height=38)
        
        #Save Buttons
        
        save_btn=Button(btn_frame,command=self.add_data,text="Save",font=("times new roman",12,"bold"),bg="blue",fg="white",width=15)
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,font=("times new roman",12,"bold"),bg="blue",fg="white",width=15)
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,command=self.delete_data,text="Delete",font=("times new roman",12,"bold"),bg="blue",fg="white",width=15)
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",font=("times new roman",12,"bold"),bg="blue",fg="white",width=15)
        reset_btn.grid(row=0,column=3)
        
        
        btn2_frame=Frame(class_Student_frame,bd=2,relief=RIDGE)
        btn2_frame.place(x=10,y=290,width=582,height=38)
        
        take_photo_btn=Button(btn2_frame,command=self.generate_dataset,text="Take Photo Sample",font=("times new roman",12,"bold"),bg="blue",fg="white",width=32)
        take_photo_btn.grid(row=0,column=0)
       
        update_photo_btn=Button(btn2_frame,text="Update Photo Sample",font=("times new roman",12,"bold"),bg="blue",fg="white",width=32)
        update_photo_btn.grid(row=0,column=1)
        
        
        #right label frame
        
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text=" Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=660,y=10,width=610,height=610)
        
        img_right = Image.open(r"clg_img\di.jpg")
        img_right = img_right.resize((620,90),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage((img_right))
        
        f_lbl = Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=605,height=90)
        
        #Search System
        
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",15,"bold"))
        search_frame.place(x=5,y=100,width=590,height=70)
        
        search_label=Label(search_frame,text="Search by:",font=("times new roman",12,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=13,state="readonly")
        search_combo["values"]=("Select","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        search_name_entry=ttk.Entry(search_frame,width=15,font=("times new roman",12,"bold"))
        search_name_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        search_btn=Button(search_frame,text="Search",font=("times new roman",12,"bold"),bg="blue",fg="white",width=10)
        search_btn.grid(row=0,column=3)
        
        show_all_btn=Button(search_frame,text="Show all",font=("times new roman",12,"bold"),bg="blue",fg="white",width=10)
        show_all_btn.grid(row=0,column=4)
        
        
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=180,width=590,height=400)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","gender","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
       
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="EMAIL ID")
        self.student_table.heading("phone",text="Phone No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo Sample Status")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
 
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    
    #=================function declares=========================
    
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="9717680633",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()
                                                                                                                
                                                                                                     ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except EXCEPTION as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
            
    #=========================fetch data====================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="9717680633",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    #================get cursor=============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
        
    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="9717680633",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                        self.var_std_id.get()
                                                                                                                                                                                                    ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student details Successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
        
    #=====================delete function==================
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("ERROR","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="9717680633",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student Details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                    
        
    #reset data
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        
            
    #============================Generate data set or Take Photo Samples
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="9717680633",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                        self.var_std_id.get()==id+1
                                                                                                                                                                                                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                #Load Predefined data on face frontals from opencv
                
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                
                messagebox.showinfo("Result","Generating data sets Completed")
                
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


                               
if __name__=="__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()

