from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
from connect import conn, cursor
from tkcalendar import DateEntry
from datetime import datetime
import sqlite3  # ADDED - Missing import

class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1127x535+230+220")

        # ================= title ====================
        lbl_title = Label(self.root, text="ROOM BOOKING DETAILS", font=("title new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1125, height=50)

        # ================ logo img ====================
        try:
            img3 = Image.open(r"./hotel images/download.png")
            img3 = img3.resize((90, 40))
            self.photoimg3 = ImageTk.PhotoImage(img3)

            lblimg1 = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
            lblimg1.place(x=5, y=2, width=90, height=40)
        except Exception as e:
            print(f"Logo image error: {e}")

        # ============= lable frame =============
        lableframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room Booking Details", font=("arial", 12, "bold"), padx=2)
        lableframeleft.place(x=5, y=50, width=450, height=475)

        # ============= Variables ======================
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()

        # ============= Labels and Entrys======================
        lblcust_contect = Label(lableframeleft, text="Customer Contact", font=("arial", 12, "bold"), padx=2, pady=6)
        lblcust_contect.grid(row=0, column=0, sticky=W)

        entry_contect = ttk.Entry(lableframeleft, textvariable=self.var_contact, width=19, font=("arial", 12, "bold"))
        entry_contect.grid(row=0, column=1, sticky=W)

        # ================== featch data btn ====================
        btnFatchData = Button(lableframeleft, command=self.Fetch_contact, text="Fatch Data", font=("arial", 8, "bold"), bg="black", fg="gold", width=9, height=1)
        btnFatchData.place(x=330, y=4)

        # check_in date
        check_in_date = Label(lableframeleft, text="Check_in Date", font=("arial", 12, "bold"), padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)

        txtcheck_in_date = DateEntry(lableframeleft, width=40, date_pattern="dd/mm/yyyy")
        txtcheck_in_date.grid(row=1, column=1, sticky=W)

        # check_out date
        label_check_out = Label(lableframeleft, text="Check_out Date", font=("arial", 12, "bold"), padx=2, pady=6)
        label_check_out.grid(row=2, column=0, sticky=W)

        textcheck_out_date = DateEntry(lableframeleft, width=40, date_pattern="dd/mm/yyyy")
        textcheck_out_date.grid(row=2, column=1, sticky=W)

        # FIX: Add txtNoOfDays declaration BEFORE getDate function
        lblNoOfDays = Label(lableframeleft, text="No Of Days", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNoOfDays.grid(row=6, column=0, sticky=W)

        txtNoOfDays = ttk.Entry(lableframeleft, textvariable=self.var_noofdays, width=29, font=("arial", 12, "bold"))
        txtNoOfDays.grid(row=6, column=1)

        def getDate(event):
            try:
                checkOutDate = textcheck_out_date.get_date()
                checkInDate = txtcheck_in_date.get_date()
                noOfDay = checkOutDate - checkInDate

                txtNoOfDays.config(state="normal")
                txtNoOfDays.delete(0, END)
                txtNoOfDays.insert(0, noOfDay.days)
                txtNoOfDays.config(state="readonly")
                if combo_avilable_room.get() == "":
                    pass
                else:
                    totalAmount("")
            except Exception as e:
                messagebox.showerror("Error", f"Date calculation error: {e}")

        textcheck_out_date.bind("<<DateEntrySelected>>", getDate)

        # room type
        lbl_roomtype = Label(lableframeleft, text="Room Type", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_roomtype.grid(row=3, column=0, sticky=W)

        combo_roomtype = ttk.Combobox(lableframeleft, textvariable=self.var_roomtype, width=27, font=("arial", 12, "bold"), state="readonly")
        try:
            q = "SELECT DISTINCT roomType FROM rooms"
            res = cursor.execute(q)
            data = res.fetchall()
            x = []
            for i in data:
                x.append(i[0])
            se = tuple(set(x))
            combo_roomtype["value"] = se
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load room types: {e}")

        combo_roomtype.grid(row=3, column=1)

        def getRoomNumber(event):
            val = combo_roomtype.get()
            try:
                q = "SELECT roomNumber FROM rooms WHERE roomType=?"
                cursor.execute(q, (val,))
                data = cursor.fetchall()
                x = []
                for i in data:
                    x.append(i[0])
                se = tuple(set(x))
                combo_avilable_room["value"] = se
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load rooms: {e}")

        combo_roomtype.bind("<<ComboboxSelected>>", getRoomNumber)

        # available room
        lbl_available_room = Label(lableframeleft, text="Available Room:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_available_room.grid(row=4, column=0, sticky=W)

        combo_avilable_room = ttk.Combobox(lableframeleft, textvariable=self.var_roomavailable, width=27, font=("arial", 12, "bold"), state="readonly")

        # FIX: Add txtRoomRent declaration BEFORE totalAmount function
        lblSubTotal = Label(lableframeleft, text="Room Rent :", font=("arial", 12, "bold"), padx=2, pady=6)
        lblSubTotal.grid(row=8, column=0, sticky=W)

        txtRoomRent = ttk.Entry(lableframeleft, textvariable=self.var_actualtotal, width=29, font=("arial", 12, "bold"))
        txtRoomRent.grid(row=8, column=1)

        def totalAmount(event):
            selectRoom = combo_avilable_room.get()
            try:
                q = "SELECT roomRent FROM rooms WHERE roomNumber=?"
                cursor.execute(q, (selectRoom,))
                data = cursor.fetchone()

                if data:
                    days = txtNoOfDays.get()
                    if days:
                        n = data[0] * int(days)

                        txtRoomRent.config(state="normal")
                        txtRoomRent.delete(0, END)
                        txtRoomRent.insert(0, n)
                        txtRoomRent.config(state="readonly")
                        mealCost("")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to calculate room rent: {e}")

        combo_avilable_room.bind("<<ComboboxSelected>>", totalAmount)
        combo_avilable_room.grid(row=4, column=1)

        # Meal
        lblmeal = Label(lableframeleft, text="Meal", font=("arial", 12, "bold"), padx=2, pady=6)
        lblmeal.grid(row=5, column=0, sticky=W)

        combo_meal = ttk.Combobox(lableframeleft, textvariable=self.var_meal, width=27, font=("arial", 12, "bold"), state="readonly")
        combo_meal["value"] = ("yes", "no")
        combo_meal.grid(row=5, column=1)

        # FIX: Add txtmealCost and txtTotalCost declarations BEFORE mealCost function
        mealCostLab = Label(lableframeleft, text="meal Cost", font=("arial", 12, "bold"), padx=2, pady=6)
        mealCostLab.grid(row=9, column=0, sticky=W)

        txtmealCost = ttk.Entry(lableframeleft, width=29, font=("arial", 12, "bold"))
        txtmealCost.grid(row=9, column=1)

        lblIdNumber = Label(lableframeleft, text="Total Cost", font=("arial", 12, "bold"), padx=2, pady=6)
        lblIdNumber.grid(row=10, column=0, sticky=W)

        txtTotalCost = ttk.Entry(lableframeleft, textvariable=self.var_total, width=20, font=("arial", 12, "bold"))
        txtTotalCost.grid(row=10, column=1, sticky=W)

        def mealCost(event):
            selectMeal = combo_meal.get()
            try:
                if selectMeal == "yes":
                    txtmealCost.config(state="normal")
                    txtmealCost.delete(0, END)
                    txtmealCost.insert(0, 500)
                    txtmealCost.config(state="readonly")
                else:
                    txtmealCost.config(state="normal")
                    txtmealCost.delete(0, END)
                    txtmealCost.insert(0, 0)
                    txtmealCost.config(state="readonly")

                roomRent = txtRoomRent.get()
                mealCostVal = txtmealCost.get()

                if roomRent and mealCostVal:
                    totalCost = int(roomRent) + int(mealCostVal)
                    q = "SELECT taxValue FROM tax WHERE id=?"
                    cursor.execute(q, (1,))
                    d = cursor.fetchone()

                    if d:
                        result = int(totalCost) * int(d[0]) / 100
                        txtTotalCost.config(state="normal")
                        txtTotalCost.delete(0, END)
                        txtTotalCost.insert(0, result + totalCost)
                        txtTotalCost.config(state="readonly")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to calculate cost: {e}")

        combo_meal.bind("<<ComboboxSelected>>", mealCost)

        # Piad Tax.
        lblPaidTax = Label(lableframeleft, text="Paid Tax in %:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPaidTax.grid(row=7, column=0, sticky=W)

        txtPaidTax = ttk.Entry(lableframeleft, textvariable=self.var_paidtax, width=29, font=("arial", 12, "bold"))
        txtPaidTax.grid(row=7, column=1)

        def fetchTax():
            try:
                q = "SELECT taxValue FROM tax WHERE id=?"
                cursor.execute(q, (1,))
                d = cursor.fetchone()
                if d:
                    txtPaidTax.delete(0, END)
                    txtPaidTax.insert(0, d[0])
                    txtPaidTax.config(state="readonly")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load tax: {e}")

        fetchTax()

        def fetchMeal():
            try:
                q = "SELECT rate FROM MealRate WHERE id=?"
                cursor.execute(q, (1,))
                d = cursor.fetchone()
                if d:
                    txtmealCost.delete(0, END)
                    txtmealCost.insert(0, d[0])
                    txtmealCost.config(state="readonly")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load meal rate: {e}")

        fetchMeal()

        # ============= bill btn ==================
        # btn_bill = Button(lableframeleft, text="Bill", font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        # btn_bill.grid(row=10,column=1)

        # # ===============btns====================
        btn_frame = Frame(lableframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=415, height=40)

        def addData():
            contact = entry_contect.get().strip()
            checkInDate = txtcheck_in_date.get()
            checkOutDate = textcheck_out_date.get()
            roomType = combo_roomtype.get()
            avilableRoom = combo_avilable_room.get()
            meal = combo_meal.get()
            noOfDays = txtNoOfDays.get()
            paidTax = txtPaidTax.get()
            roomRent = txtRoomRent.get()
            totalCost = txtTotalCost.get()
            mealCost = txtmealCost.get()

            # FIX: Better validation
            if not contact or not totalCost or not roomType or not avilableRoom:
                messagebox.showerror('error', "All fields are required!")
                return

            # Validate contact is numeric
            if not contact.isdigit():
                messagebox.showerror('error', "Contact must be a number!")
                return

            data = (contact, checkInDate, checkOutDate, roomType, avilableRoom, meal, noOfDays, paidTax, roomRent, mealCost, totalCost)
            try:
                q = "INSERT INTO booking(contact, checkInDate, checkOutDate, roomType, avilableRoom, meal, noOfDays, paidTax, roomRent, mealCost, totalCost) VALUES(?,?,?,?,?,?,?,?,?,?,?)"
                cursor.execute(q, data)
                conn.commit()
                messagebox.showinfo('info', 'Booking saved successfully!')
                viewData()
                reset()  # FIX: Add reset after successful booking
            except sqlite3.IntegrityError:
                messagebox.showerror("error", "Room is already booked!")
            except Exception as e:
                messagebox.showerror('error', f'Error: {str(e)}')

        btn_add = Button(btn_frame, text="ADD", font=("arial", 12, "bold"), bg="black", fg="gold", width=9, command=addData)
        btn_add.grid(row=0, column=0, padx=1)

        def updateData():
            idx = self.room_table.focus()
            if not idx:
                messagebox.showinfo("info", "Select to update")
                return
            contact = entry_contect.get().strip()
            checkInDate = txtcheck_in_date.get()
            checkOutDate = textcheck_out_date.get()
            roomType = combo_roomtype.get()
            avilableRoom = combo_avilable_room.get()
            meal = combo_meal.get()
            noOfDays = txtNoOfDays.get()
            paidTax = txtPaidTax.get()
            roomRent = txtRoomRent.get()
            totalCost = txtTotalCost.get()
            mealCost = txtmealCost.get()

            # Validate contact is numeric
            if not contact.isdigit():
                messagebox.showerror('error', "Contact must be a number!")
                return

            data = (contact, checkInDate, checkOutDate, roomType, avilableRoom, meal, noOfDays, paidTax, roomRent, mealCost, totalCost, idx)

            try:
                q = "UPDATE booking SET contact=?, checkInDate=?, checkOutDate=?, roomType=?, avilableRoom=?, meal=?, noOfDays=?, paidTax=?, roomRent=?, mealCost=?, totalCost=? WHERE id=?"
                cursor.execute(q, data)
                conn.commit()
                messagebox.showinfo("info", "Booking details updated successfully")
                viewData()
            except Exception as e:
                print(e)
                messagebox.showerror("error", "Error: " + str(e))

        btnupdate = Button(btn_frame, text="UPDATE", font=("arial", 12, "bold"), bg="black", fg="gold", width=9, command=updateData)
        btnupdate.grid(row=0, column=1, padx=1)

        def deleteData():
            idx = self.room_table.focus()
            if idx:
                try:
                    q = "DELETE FROM booking WHERE id = ?"
                    cursor.execute(q, (idx,))
                    conn.commit()
                    self.room_table.delete(idx)
                    messagebox.showinfo("info", "Booking deleted!")
                except Exception as e:
                    messagebox.showerror("error", f"Error: {e}")
            else:
                messagebox.showwarning("warning", "select data to delete")

        btndelete = Button(btn_frame, text="DELETE", font=("arial", 12, "bold"), bg="black", fg="gold", width=9, command=deleteData)
        btndelete.grid(row=0, column=2, padx=1)

        def reset():
            entry_contect.delete(0, END)
            txtNoOfDays.config(state="normal")
            txtNoOfDays.delete(0, END)
            txtPaidTax.config(state="normal")
            txtPaidTax.delete(0, END)
            txtRoomRent.config(state="normal")
            txtRoomRent.delete(0, END)
            txtmealCost.config(state="normal")
            txtmealCost.delete(0, END)
            txtTotalCost.config(state="normal")
            txtTotalCost.delete(0, END)

        btnreset = Button(btn_frame, text="RESET", font=("arial", 12, "bold"), bg="black", fg="gold", width=9, command=reset)
        btnreset.grid(row=0, column=3, padx=1)

        # ==============rightside image ===============================
        try:
            img3 = Image.open(r"./hotel images/bed.jpg")
            img3 = img3.resize((370, 200))
            self.photoimg2 = ImageTk.PhotoImage(img3)

            lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
            lblimg.place(x=750, y=55, width=370, height=200)
        except Exception as e:
            print(f"Image load error: {e}")

        # ============table frame ===============
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System", font=("arial", 12, "bold"), padx=2)
        table_frame.place(x=460, y=250, width=690, height=470)

        lblsearchby = Label(table_frame, text="Search By:", bg="red", fg="white", font=("arial", 12, "bold"), padx=2, pady=6)
        lblsearchby.grid(row=0, column=0, sticky=W, padx=2)

        combo_search = ttk.Combobox(table_frame, font=("arial", 12, "bold"), width=17, state="readonly")
        combo_search["value"] = ("Contact", "Room No.")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        entry_search = ttk.Entry(table_frame, width=20, font=("arial", 12, "bold"))
        entry_search.grid(row=0, column=2, padx=2)

        def searchData():
            searchBy = combo_search.get().lower()
            if searchBy == "room no.":
                searchBy = "avilableRoom"
            else:
                searchBy = "contact"  # FIX: Default to contact
            searchEntry = entry_search.get().strip()

            if searchEntry == "":
                messagebox.showwarning("warning", f"Enter {searchBy} to search!")
                return

            try:
                q = f"SELECT * FROM booking WHERE {searchBy} = ?"
                cursor.execute(q, (searchEntry,))
                searchList = cursor.fetchall()
                if len(searchList) == 0:
                    messagebox.showwarning("warning", "Data not found!")
                    return

                childs = self.room_table.get_children()
                for child in childs:
                    self.room_table.delete(child)

                for j in searchList:
                    self.room_table.insert("", END, values=j)

            except Exception as e:
                messagebox.showerror('error', f'Error: {str(e)}')
                print(e)

        btnrsearch = Button(table_frame, text="Search", font=("arial", 12, "bold"), bg="black", fg="gold", width=8, command=searchData)
        btnrsearch.grid(row=0, column=3, padx=1)

        # ===================== show data table ============
        details_frame = Frame(table_frame, bd=2, relief=RIDGE)
        details_frame.place(x=0, y=50, width=660, height=180)

        scroll_x = ttk.Scrollbar(details_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_frame, orient=VERTICAL)

        self.room_table = ttk.Treeview(details_frame, columns=("srNo", "contact", "checkin", "checkout", "roomtype", "roomavailable", "meal", "noOfdays", "paidTax", "roomRent", "mealCost", "totalCost", "id"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("srNo", text="Sr.No")
        self.room_table.heading("contact", text="Mobile No.")
        self.room_table.heading("checkin", text="check-in")
        self.room_table.heading("checkout", text="Check-out")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("roomavailable", text="Room No")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noOfdays", text="NoOfDays")
        self.room_table.heading("paidTax", text="Tax %")
        self.room_table.heading("roomRent", text="Room Rent")
        self.room_table.heading("mealCost", text="Meal Cost")
        self.room_table.heading("totalCost", text="Total Cost")
        self.room_table.heading("id", text="id")

        self.room_table["show"] = "headings"
        self.room_table.column("srNo", width=100, anchor="center")
        self.room_table.column("contact", width=100, anchor="center")
        self.room_table.column("checkin", width=100, anchor="center")
        self.room_table.column("checkout", width=100, anchor="center")
        self.room_table.column("roomtype", width=100, anchor="center")
        self.room_table.column("roomavailable", width=100, anchor="center")
        self.room_table.column("meal", width=100, anchor="center")
        self.room_table.column("noOfdays", width=100, anchor="center")
        self.room_table.column("paidTax", width=100, anchor="center")
        self.room_table.column("roomRent", width=100, anchor="center")
        self.room_table.column("mealCost", width=100, anchor="center")
        self.room_table.column("totalCost", width=100, anchor="center")
        self.room_table.column("id", width=0, stretch=False)

        self.room_table.pack(fill=BOTH, expand=1)

        def viewData():
            try:
                childs = self.room_table.get_children()
                for child in childs:
                    self.room_table.delete(child)
                q = "SELECT * FROM booking"
                res = cursor.execute(q)
                data = res.fetchall()
                n = 1
                for j in data:
                    l = list(j)
                    l[0] = n
                    n = n + 1
                    k = tuple(l)
                    self.room_table.insert("", END, iid=j[0], values=k)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load data: {e}")

        viewData()

        btnrshowall = Button(table_frame, text="Show All", font=("arial", 12, "bold"), bg="black", fg="gold", width=8, command=viewData)
        btnrshowall.grid(row=0, column=4, padx=1)

        def onClickTree(event):
            try:
                select = self.room_table.focus()
                if select:
                    val = self.room_table.item(select, 'values')
                    entry_contect.delete(0, END)
                    entry_contect.insert(0, val[1])

                    txtcheck_in_date.delete(0, END)
                    txtcheck_in_date.insert(0, val[2])
                    textcheck_out_date.delete(0, END)
                    textcheck_out_date.insert(0, val[3])
                    combo_roomtype.set(val[4])
                    combo_avilable_room.set(val[5])
                    combo_meal.set(val[6])
                    txtNoOfDays.config(state="normal")
                    txtNoOfDays.delete(0, END)
                    txtNoOfDays.insert(0, val[7])
                    txtPaidTax.config(state="normal")
                    txtPaidTax.delete(0, END)
                    txtPaidTax.insert(0, val[8])
                    txtRoomRent.config(state="normal")
                    txtRoomRent.delete(0, END)
                    txtRoomRent.insert(0, val[9])
                    txtmealCost.config(state="normal")
                    txtmealCost.delete(0, END)
                    txtmealCost.insert(0, val[10])
                    txtTotalCost.config(state="normal")
                    txtTotalCost.delete(0, END)
                    txtTotalCost.insert(0, val[11])
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load booking details: {e}")

        self.room_table.bind("<<TreeviewSelect>>", onClickTree)

    # ===================== ALL Data Fetch ================
    def Fetch_contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter Contact Number", parent=self.root)
        else:
            try:
                contact = self.var_contact.get().strip()
                if not contact.isdigit():
                    messagebox.showerror("Error", "Contact must be numeric", parent=self.root)
                    return

                q = ("SELECT Name FROM customers WHERE mobile=?")
                cursor.execute(q, (contact,))
                row = cursor.fetchone()

                if row == None:
                    messagebox.showerror("Error", "This number not found", parent=self.root)
                else:
                    showDataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                    showDataframe.place(x=455, y=55, width=280, height=180)

                    lblName = Label(showDataframe, text="Name", font=("arial", 12, "bold"))
                    lblName.place(x=0, y=0)

                    lbl = Label(showDataframe, text=row[0], font=("arial", 12, "bold"))
                    lbl.place(x=100, y=0)

                    q = ("SELECT Gender FROM customers WHERE mobile=?")
                    cursor.execute(q, (contact,))
                    row = cursor.fetchone()

                    if row != None:
                        lblName = Label(showDataframe, text="Gender", font=("arial", 12, "bold"))
                        lblName.place(x=0, y=30)

                        lbl = Label(showDataframe, text=row[0], font=("arial", 12, "bold"))
                        lbl.place(x=100, y=30)

                        q = ("SELECT Email FROM customers WHERE mobile=?")
                        cursor.execute(q, (contact,))
                        row = cursor.fetchone()

                        if row != None:
                            lblName = Label(showDataframe, text="Email", font=("arial", 12, "bold"))
                            lblName.place(x=0, y=60)

                            lbl = Label(showDataframe, text=row[0], font=("arial", 12, "bold"))
                            lbl.place(x=100, y=60)

                            q = ("SELECT Nationality FROM customers WHERE mobile=?")
                            cursor.execute(q, (contact,))
                            row = cursor.fetchone()

                            if row != None:
                                lblName = Label(showDataframe, text="Nationality", font=("arial", 12, "bold"))
                                lblName.place(x=0, y=90)

                                lbl = Label(showDataframe, text=row[0], font=("arial", 12, "bold"))
                                lbl.place(x=100, y=90)

                                q = ("SELECT Address FROM customers WHERE mobile=?")
                                cursor.execute(q, (contact,))
                                row = cursor.fetchone()

                                if row != None:
                                    lblName = Label(showDataframe, text="Address", font=("arial", 12, "bold"))
                                    lblName.place(x=0, y=120)

                                    lbl = Label(showDataframe, text=row[0], font=("arial", 12, "bold"))
                                    lbl.place(x=100, y=120)

                    conn.commit()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to fetch contact: {e}")


if __name__ == "__main__":
    root = Tk()
    ojt = Roombooking(root)
    root.mainloop()