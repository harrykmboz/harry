from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from tkinter import messagebox
from connect import conn , cursor
class Cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1127x535+230+220")
        # ================= title ====================
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman", 18, "bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1125, height=50)     
        
        
         # ================ logo img ====================
        
        
        img2=Image.open(r"./hotel images/download.png")
        img2=img2.resize((100,40))
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)
        
        
        
        # ============= lable frame =============
        lableframeleft= LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("arial",12,"bold"),padx=2,)
        lableframeleft.place(x=5,y=50,width=425,height=475)
        
        # ============= Labels and Entrys======================
        # CustRef
        lblcust_ref=Label(lableframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
        lblcust_ref.grid(row=0,column=0,sticky=W)
        def randomNumber():
            randomValue =  int((random.randint(1000 , 9999)))
            return randomValue
        entry_ref=ttk.Entry(lableframeleft,width=29,font=("arial",12,"bold"),)
        entry_ref.delete(0 , END)
        entry_ref.insert(0 , randomNumber()) 
        entry_ref.config(state="readonly")
        entry_ref.grid(row=0,column=1)
        
         # cust name
        lblcust_name=Label(lableframeleft,text="Customer Name",font=("arial",12,"bold"),padx=2,pady=6)
        lblcust_name.grid(row=1,column=0,sticky=W)
        
        entry_name=ttk.Entry(lableframeleft,width=29,font=("arial",12,"bold"))
        entry_name.grid(row=1,column=1)
        
         # father name
        lblcust_father=Label(lableframeleft,text="Father Name",font=("arial",12,"bold"),padx=2,pady=6)
        lblcust_father.grid(row=2,column=0,sticky=W)
        
        entry_father=ttk.Entry(lableframeleft,width=29,font=("arial",12,"bold"))
        entry_father.grid(row=2,column=1) 
        
         # mother name
        lblcust_mother=Label(lableframeleft,text="Mother Name",font=("arial",12,"bold"),padx=2,pady=6)
        lblcust_mother.grid(row=3,column=0,sticky=W)
        
        entry_mother=ttk.Entry(lableframeleft,width=29,font=("arial",12,"bold"))
        entry_mother.grid(row=3,column=1)  
        
         # gender combobox
        lblcust_gender=Label(lableframeleft,text="Gender",font=("arial",12,"bold"),padx=2,pady=6)
        lblcust_gender.grid(row=4,column=0,sticky=W)
        
        combo_gender=ttk.Combobox(lableframeleft,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=4, column=1)
        
        # post code
        lblcust_post=Label(lableframeleft,text="Post Code",font=("arial",12,"bold"),padx=2,pady=6)
        lblcust_post.grid(row=5,column=0,sticky=W)
        
        entry_post=ttk.Entry(lableframeleft,width=29,font=("arial",12,"bold"))
        entry_post.grid(row=5,column=1)    
        
         # mobile no.
        lblcust_mobile=Label(lableframeleft,text="Mobile No.",font=("arial",12,"bold"),padx=2,pady=6)
        lblcust_mobile.grid(row=6,column=0,sticky=W)
        
        entry_mobile=ttk.Entry(lableframeleft,width=29,font=("arial",12,"bold"))
        entry_mobile.grid(row=6,column=1)  
        
         # email
        lblcust_email=Label(lableframeleft,text="Email",font=("arial",12,"bold"),padx=2,pady=6)
        lblcust_email.grid(row=7,column=0,sticky=W)
        
        entry_email=ttk.Entry(lableframeleft,width=29,font=("arial",12,"bold"))
        entry_email.grid(row=7,column=1)
        
         # nationality
        lblcust_nationality=Label(lableframeleft,text="Nationality",font=("arial",12,"bold"),padx=2,pady=6)
        lblcust_nationality.grid(row=8,column=0,sticky=W)
        
        combo_nationality=ttk.Combobox(lableframeleft,font=("arial",12,"bold"),width=27,state="readonly")
        combo_nationality["value"]=("Indian", "American", "Canadian", "British")
        combo_nationality.current(0)
        combo_nationality.grid(row=8, column=1)
        
         # id type combobox
        lblcust_id_type=Label(lableframeleft,text="Id Proof Type",font=("arial",12,"bold"),padx=2,pady=6)
        lblcust_id_type.grid(row=9,column=0,sticky=W)
        
        combo_id_type=ttk.Combobox(lableframeleft,font=("arial",12,"bold"),width=27,state="readonly")
        combo_id_type["value"]=("AdharCard","Driving Licence", "Passport",)
        combo_id_type.current(0)
        combo_id_type.grid(row=9, column=1)
        
         # id number
        lblcust_id_number=Label(lableframeleft,text="Id Number",font=("arial",12,"bold"),padx=2,pady=6)
        lblcust_id_number.grid(row=10,column=0,sticky=W)
        
        entry_id_number=ttk.Entry(lableframeleft,width=29,font=("arial",12,"bold"))
        entry_id_number.grid(row=10,column=1) 
        
         # address
        lblcust_address=Label(lableframeleft,text="Address",font=("arial",12,"bold"),padx=2,pady=6)
        lblcust_address.grid(row=11,column=0,sticky=W)
        
        entry_address=ttk.Entry(lableframeleft,width=29,font=("arial",12,"bold"))
        entry_address.grid(row=11,column=1)    
        
        # ===============btns====================
        btn_frame=Frame(lableframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=415,width=415,height=40)

        def addData():
            ref =  entry_ref.get()
            name = entry_name.get()
            father= entry_father.get()
            mother = entry_mother.get()
            gender = combo_gender.get()
            post = entry_post.get()
            mobile = entry_mobile.get()
            email = entry_email.get()
            nationality = combo_nationality.get()
            comboidtype = combo_id_type.get()
            Idnumber = entry_id_number.get()
            address = entry_address.get()
            
            if (name == "" or email==""): 
                messagebox.showerror('error', "All fields are required!")
                return 
            data = (ref , name ,father ,mother , gender ,post,mobile,email,nationality,comboidtype,Idnumber,address)
            try:
                q = "insert into customers(ref ,name ,father ,mother ,gender ,post ,mobile ,email ,nationality ,comboidtype ,Idnumber ,address ) values(?,?,?,?,?,?,?,?,?,?,?,?)"
                cursor.execute(q,data)
                conn.commit()
                viewData()
                messagebox.showinfo('info' , 'data save !')
            except Exception as e :
                if str(e) == "UNIQUE constraint failed: customers.ref":
                    messagebox.showerror("error" , " Number already exist! ")
                else:
                    messagebox.showerror('error' , f'error {str(e)}')
            
        btn_add=Button(btn_frame,text="ADD",font=("arial",12,"bold"),bg="black",fg="gold",width=9 , command=addData)
        btn_add.grid(row=0,column=0,padx=1)
        def updateData():
            select  =  self.Cust_details_table.selection()
            if not select :
                messagebox.showinfo("info" , "Select to update")
                return 
            val =  self.Cust_details_table.item(select , 'values')
            idx = val[0]
            ref =  entry_ref.get()
            name = entry_name.get()
            father= entry_father.get()
            mother = entry_mother.get()
            gender = combo_gender.get()
            post = entry_post.get()
            mobile = entry_mobile.get()
            email = entry_email.get()
            nationality = combo_nationality.get()
            comboidtype = combo_id_type.get()
            Idnumber = entry_id_number.get()
            address = entry_address.get()
            data = (ref , name ,father ,mother , gender ,post,mobile,email,nationality,comboidtype,Idnumber,address,idx)
            try :
                q = "update customers set ref=? ,name=? ,father=? ,mother=? ,gender=? ,post=? ,mobile=? ,email=? ,nationality=? ,comboidtype=? ,Idnumber=? ,address=? where id=?  "
                cursor.execute(q , data)
                conn.commit()
                messagebox.showinfo("info" , "Customer details has been update sucessfully")
                viewData()
            except Exception as e:
                print(e)
                messagebox.showerror("error" , "server Error !")
                 
        btnupdate=Button(btn_frame,text="UPDATE",font=("arial",12,"bold"),bg="black",fg="gold",width=9 , command=updateData)
        btnupdate.grid(row=0,column=1,padx=1)
        def deleteData():
            select  =  self.Cust_details_table.selection()
            if select :
                val =  self.Cust_details_table.item(select , 'values')
                idx = val[0]
                q = "delete from customers where id = ?"
                cursor.execute(q , (idx,))
                conn.commit()
                self.Cust_details_table.delete(select)
            else:
                messagebox.showwarning("warning" , "select data to delete")

        btndelete=Button(btn_frame,text="DELETE",font=("arial",12,"bold"),bg="black",fg="gold",width=9 ,command=deleteData)
        btndelete.grid(row=0,column=2,padx=1)
        def resetFrom():
            entry_ref.config(state="normal")
            entry_ref.delete(0 , END)
            entry_ref.insert(0 , randomNumber()) 
            entry_ref.config(state="readonly")
            entry_name.delete(0 , END)
            entry_father.delete(0 , END)
            entry_mother.delete(0 , END)
            combo_gender.set(0 , END)
            entry_post.delete(0 , END)
            entry_mobile.delete(0 , END)
            entry_email.delete(0 , END)
            combo_nationality.set(0 , END)
            combo_id_type.set(0 , END)
            entry_id_number.delete(0 , END)
            entry_address.delete(0 , END)
            
        btnreset=Button(btn_frame,text="RESET",font=("arial",12,"bold"),bg="black",fg="gold",width=9 , command=resetFrom)
        btnreset.grid(row=0,column=3,padx=1)
        
        
        # ============table frame ===============
        table_frame= LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",12,"bold"),padx=2,)
        table_frame.place(x=435,y=50,width=690,height=470)
        
        lblsearchby=Label(table_frame,text="Search By:",bg="red",fg="white",font=("arial",12,"bold"),padx=2,pady=6)
        lblsearchby.grid(row=0,column=0,sticky=W,padx=2)
        
        combo_search=ttk.Combobox(table_frame,font=("arial",12,"bold"),width=20,state="readonly")
        combo_search["value"]=("Mobile","Ref")
        combo_search.current(0)
        combo_search.grid(row=0, column=1,padx=2)
        
        entry_search=ttk.Entry(table_frame,width=20,font=("arial",12,"bold"))
        entry_search.grid(row=0,column=2,padx=2)
        
        def searchData():
            searchBy =  combo_search.get().lower()
            searchEntry =  entry_search.get()
            if searchEntry == "" :
                messagebox.showwarning("warning" , f" Enter {searchBy} number !")
                return
            try :
                
                q = f"select * from customers where {searchBy} = ?"
                cursor.execute(q , (searchEntry ,))
                searchList =  cursor.fetchall()
                if len(searchList) == 0 :
                    messagebox.showwarning("warning" , "Data  not Found !")
                    return 
                
                childs =  self.Cust_details_table.get_children()
                for child in childs:
                    self.Cust_details_table.delete(child)
                for j  in searchList :
                 self.Cust_details_table.insert("",END ,values=j)
                
            except Exception as e :
                messagebox.showerror('error' , f'error {str(e)}')
                print(e)
        btnrsearch=Button(table_frame,text="Search",font=("arial",12,"bold"),bg="black",fg="gold",width=8, command=searchData)
        btnrsearch.grid(row=0,column=3,padx=1)
        
        
        
        # ===================== show data table ============
        details_frame=Frame(table_frame,bd=2,relief=RIDGE)
        details_frame.place(x=0,y=50,width=660,height=350)
        
        scroll_x=ttk.Scrollbar(details_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_frame,orient=VERTICAL)
        
        self.Cust_details_table=ttk.Treeview(details_frame,columns=("id" ,"ref" ,"name" ,"father" ,"mother" ,"gender" ,"post" ,"mobile" ,"email" ,"nationality" ,"idproof" ,"idnumber" ,"address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.Cust_details_table.xview)
        scroll_y.config(command=self.Cust_details_table.yview)
        
        self.Cust_details_table.heading("id",text="S.no.")
        self.Cust_details_table.heading("ref",text="Refer No")
        self.Cust_details_table.heading("name",text="Customer Name")
        self.Cust_details_table.heading("father",text="Father Name")
        self.Cust_details_table.heading("mother",text="Mother Name")
        self.Cust_details_table.heading("gender",text="Gender")
        self.Cust_details_table.heading("post",text="PostCode")
        self.Cust_details_table.heading("mobile",text="Mobile")
        self.Cust_details_table.heading("email",text="Email")
        self.Cust_details_table.heading("nationality",text="Nationality")
        self.Cust_details_table.heading("idproof",text="Idproof")
        self.Cust_details_table.heading("idnumber",text="Idnumber")
        self.Cust_details_table.heading("address",text="Address")
        
        self.Cust_details_table["show"]="headings"
        
        self.Cust_details_table.column("id",width=100)
        self.Cust_details_table.column("ref",width=100)
        self.Cust_details_table.column("name",width=200)
        self.Cust_details_table.column("father",width=200)
        self.Cust_details_table.column("mother",width=200)
        self.Cust_details_table.column("gender",width=100)
        self.Cust_details_table.column("post",width=100)
        self.Cust_details_table.column("mobile",width=200)
        self.Cust_details_table.column("email",width=300)
        self.Cust_details_table.column("nationality",width=150)
        self.Cust_details_table.column("idproof",width=100)
        self.Cust_details_table.column("idnumber",width=200)
        self.Cust_details_table.column("address",width=300)

        
        self.Cust_details_table.pack(fill=BOTH,expand=1)
        def viewData():
            childs =  self.Cust_details_table.get_children()
            for child in childs:
                self.Cust_details_table.delete(child)
            q = "select * from customers"
            res =  cursor.execute(q)
            data =  res.fetchall()
            for j  in data :
                self.Cust_details_table.insert("",END ,values=j)
        viewData()
        btnrshowall=Button(table_frame,text="Show All",font=("arial",12,"bold"),bg="black",fg="gold",width=8, command=viewData)
        btnrshowall.grid(row=0,column=4,padx=1)
        def onClickTree(event):
            select =  self.Cust_details_table.focus()
            if select :
                val =  self.Cust_details_table.item(select , 'values')
                entry_ref.config(state="normal")
                entry_ref.delete(0,END)
                entry_ref.insert(0, val[1])
                entry_ref.config(state="readonly")
                entry_name.delete(0 , END)
                entry_name.insert(0 , val[2])
                entry_father.delete(0 , END)
                entry_father.insert(0 , val[3])
                entry_mother.delete(0 , END)
                entry_mother.insert(0 , val[4])
                combo_gender.delete(0 , END)
                combo_gender.set(val[5])
                entry_post.delete(0 , END)
                entry_post.insert(0 , val[6])
                entry_mobile.delete(0 , END)
                entry_mobile.insert(0 , val[7])
                entry_email.delete(0 , END)
                entry_email.insert(0 , val[8])
                combo_nationality.delete(0 , END)
                combo_nationality.set(0,val[9])
                combo_id_type.delete(0 , END)
                combo_id_type.set(0,val[10])
                entry_id_number.delete(0 , END)
                entry_id_number.insert(0 , val[11])
                entry_address.delete(0 , END)
                entry_address.insert(0 , val[12])
        self.Cust_details_table.bind("<<TreeviewSelect>>" , onClickTree)

        

        
        
        
        
    
if __name__=="__main__":
    root=Tk()
    ojt=Cust_win(root)
    root.mainloop()                    