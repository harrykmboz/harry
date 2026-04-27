from tkinter import *
from tkinter import ttk
import sqlite3

class ReportWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Report")
        self.root.geometry("1127x535+230+220")
        self.root.config(bg="white")

        # =============== Title ===============
        title = Label(self.root, text="BOOKING REPORT", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        title.pack(side=TOP, fill=X)

        # ============== Table Frame ============
        table_frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=50, width=1120, height=465)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.report_table = ttk.Treeview(table_frame, columns=("id", "name", "room", "date", "status"),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.report_table.xview)
        scroll_y.config(command=self.report_table.yview)

        # Configure the '#0' column (default first column)
        self.report_table.column("#0", width=0, stretch=NO)
        
        self.report_table.heading("#0", text="")
        self.report_table.heading("id", text="Booking ID")
        self.report_table.heading("name", text="Customer Name")
        self.report_table.heading("room", text="Room No")
        self.report_table.heading("date", text="Booking Date")
        self.report_table.heading("status", text="Status")

        self.report_table['show'] = 'headings'

        self.report_table.column("id", width=100)
        self.report_table.column("name", width=200)
        self.report_table.column("room", width=100)
        self.report_table.column("date", width=150)
        self.report_table.column("status", width=100)

        self.report_table.pack(fill=BOTH, expand=1)

        self.fetch_data()

    def fetch_data(self):
        try:
            conn = sqlite3.connect("hotel.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM booking")
            rows = cursor.fetchall()
            
            # Clear existing data
            self.report_table.delete(*self.report_table.get_children())
            
            # Insert new data
            if rows:
                for row in rows:
                    self.report_table.insert("", END, values=row)
            else:
                print("No booking records found.")
                
            conn.close()
        except sqlite3.OperationalError as e:
            print("Database error:", e)
        except Exception as e:
            print("Error fetching data:", e)

            
if __name__ == "__main__":
    root = Tk()
    ojt = ReportWindow(root)
    root.mainloop()