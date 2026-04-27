from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
from connect import conn , cursor

class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1127x535+230+220")


        # ================= title ====================
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("title new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1125, height=50)     
        
        
         # ================ logo img ====================
        
        
        img3=Image.open(r"./hotel images/download.png")
        img3=img3.resize((90,40))
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lblimg1=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg1.place(x=5, y=2, width=90, height=40)
        
         # ============= lable frame =============
        lableframeleft= LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("arial",12,"bold"),padx=2,)
        lableframeleft.place(x=5,y=50,width=520,height=350)

         # ============= Labels and Entrys======================
        # Floor
        lbl_floor=Label(lableframeleft,text="Price",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)
        
        entry_floor=ttk.Entry(lableframeleft,width=19,font=("arial",12,"bold"))
        entry_floor.grid(row=0,column=1,sticky=W)

        # Room No.
        lbl_RoomNo=Label(lableframeleft,text="Room No",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)
        
        entry_RoomNo=ttk.Entry(lableframeleft,width=19,font=("arial",12,"bold"))
        entry_RoomNo.grid(row=1,column=1,sticky=W)

        # Room Type
        lbl_RoomType=Label(lableframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W)
        
        entry_RoomType=ttk.Entry(lableframeleft,width=19,font=("arial",12,"bold"))
        entry_RoomType.grid(row=2,column=1,sticky=W)
         #Change Tax
        lbl_tax=Label(lableframeleft,text="Change tax",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_tax.grid(row=3,column=0,sticky=W)
        entry_RoomTax=ttk.Entry(lableframeleft,width=19,font=("arial",12,"bold"))
        entry_RoomTax.grid(row=3,column=1,sticky=W)

        lbl_changeMeal=Label(lableframeleft,text="Change MealRate",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_changeMeal.grid(row=4,column=0,sticky=W)

        entry_changeMeal=ttk.Entry(lableframeleft,width=19,font=("arial",12,"bold"))
        entry_changeMeal.grid(row=4,column=1,sticky=W)

        
        def fetchMeal():
            q  = "select * from MealRate "
            cursor.execute(q)
            d =  cursor.fetchall()
            entry_changeMeal.delete(0 ,END)
            entry_changeMeal.insert(0 , d[0][1])
        fetchMeal()
        def setMeal():
            
            try:
                meal =  entry_changeMeal.get()
                q= "update  MealRate set rate=? where id=?"
                cursor.execute(q, (meal,1))
                conn.commit()
                
                messagebox.showinfo("info",  "meal Rate Updated !")
            except Exception as e :
                print(e)
                messagebox.showerror("error" , "Server Error !")

        changeMeal=Button(lableframeleft,text="Set Meal",font=("arial",12,"bold"),bg="black",fg="gold",width=12 , command=setMeal)
        changeMeal.grid(row=4,column=3,padx=1)

        def fetchTax():
            q  = "select * from tax "
            cursor.execute(q)
            d =  cursor.fetchall()
            entry_RoomTax.delete(0 ,END)
            entry_RoomTax.insert(0 , d[0][1])
        fetchTax()

        def changeTaxData():
            val =  entry_RoomTax.get()
            q  = "update tax set taxValue=? where id=?"
            data = (val , 1,)
            cursor.execute( q,data)
            conn.commit()
            messagebox.showinfo("info" , "tax is Update !")
            fetchTax()
        changeTax=Button(lableframeleft,text="Set Tax",font=("arial",12,"bold"),bg="black",fg="gold",width=12 ,command=changeTaxData)
        changeTax.grid(row=3,column=3,padx=1)

      

        # ===============btns====================
        btn_frame=Frame(lableframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=250,width=415,height=40)
          
        def addRoom():
            price =  entry_floor.get()
            roomNo =  entry_RoomNo.get()
            roomType =  entry_RoomType.get()
            try:
                if price == "" and roomNo =="" and roomType =="" :
                   messagebox.showwarning("warning" , "Enter all Fields ! ")
                   return 
                q  = "insert into rooms(roomType , roomNumber , roomRent) values( ? , ? , ?)"
                cursor.execute(q , (roomType , roomNo , price))
                conn.commit()
                messagebox.showinfo("info" , " Room Data save ! ")
                showRoom()
            except Exception as e : 
                messagebox.showerror("error" , f"server Error {str(e)}")
                print(e)

        def deleteData():
            select  =  self.room_table.selection()
            if select :
                val =  self.room_table.item(select , 'values')
                idx = val[0]
                q = "delete from rooms where id = ?"
                cursor.execute(q , (idx,))
                conn.commit()
                self.room_table.delete(select)
                messagebox.showinfo("info","Data delete")
            else:
                messagebox.showwarning("warning" , "select data to delete")   

        def updateData():
            select  =  self.room_table.selection()
            if not select :
                messagebox.showinfo("info" , "Select to update")
                return 
            val =  self.room_table.item(select , 'values')
            idx = val[0]
            RoomType = entry_RoomType.get()
            roomNo =  entry_RoomNo.get()
            roomRent =  entry_floor.get()
            showRoom()
            data = (RoomType , roomRent,roomNo , idx)
            try :
                q = "update rooms set roomType=? ,roomRent=? ,roomNumber=?  where id=?  "
                cursor.execute(q , data)
                conn.commit()
                messagebox.showinfo("info" , "Room details has been update sucessfully")
              
            except Exception as e:
                print(e)
                messagebox.showerror("error" , "server Error !")             

            
        btn_add=Button(btn_frame,text="ADD",font=("arial",12,"bold"),bg="black",fg="gold",width=9 ,command= addRoom )
        btn_add.grid(row=0,column=0,padx=1)
        
        btnupdate=Button(btn_frame,text="UPDATE",font=("arial",12,"bold"),bg="black",fg="gold",width=9,command=updateData)
        btnupdate.grid(row=0,column=1,padx=1)
        
        btndelete=Button(btn_frame,text="DELETE",font=("arial",12,"bold"),bg="black",fg="gold",width=9 , command=deleteData)
        btndelete.grid(row=0,column=2,padx=1)
        
        # btnreset=Button(btn_frame,text="RESET",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        # btnreset.grid(row=0,column=3,padx=1)

        #  =================table frame search system ====================

        table_frame= LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("arial",12,"bold"),padx=2,)
        table_frame.place(x=550,y=50,width=520,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.room_table=ttk.Treeview(table_frame,columns=("ID","roomno" ,"price","roomtype" ),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("ID",text="ID")
        self.room_table.heading("roomno",text="Room No.")
        self.room_table.heading("price",text="Price")
        self.room_table.heading("roomtype",text="Room Type")
        
        
        self.room_table["show"]="headings"
        
        self.room_table.column("ID",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("price",width=100)
        self.room_table.column("roomtype",width=100)

        
        self.room_table.pack(fill=BOTH,expand=1)
        def showRoom():
            childs =  self.room_table.get_children()
            for child in childs:
                self.room_table.delete(child)
            try:
                q  = "select * from rooms"
                cursor.execute(q)
                roomList =  cursor.fetchall()
                for room in roomList :
                    self.room_table.insert("" ,END ,  values=room)
                    pass 
            except Exception as e :
                messagebox.showerror("error" , f"server Error {str(e)}")
                print(e)
        showRoom()

        def onClickTree(event):
            select =  self.room_table.focus()
            if select :
                val =  self.room_table.item(select , 'values')
                entry_RoomNo.delete(0,END)
                entry_RoomNo.insert(0, val[1])
                entry_floor.delete(0 , END)
                entry_floor.insert(0 , val[2])
                entry_RoomType.delete(0 , END)
                entry_RoomType.insert(0 , val[3])
        self.room_table.bind("<<TreeviewSelect>>" , onClickTree)
        
        
        
        def DetailsRoom(self):
         self.new_window=Toplevel(self.root)
         self.app=DetailsRoom(self.new_window)
                


if __name__=="__main__":
    root=Tk()
    ojt=DetailsRoom(root)
    root.mainloop()         