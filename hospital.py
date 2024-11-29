from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEffect=StringVar()
        self.FutherInformation=StringVar()
        self.BloodPressure=StringVar()
        self.StorageAdvice=StringVar()
        self.Medication=StringVar()
        self.DrivinUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()


        #   # Canvas and Scrollable Frame
        # self.main_canvas = Canvas(self.root, borderwidth=0)
        # self.scroll_y = ttk.Scrollbar(self.root, orient=VERTICAL, command=self.main_canvas.yview)
        # self.scroll_x = ttk.Scrollbar(self.root, orient=HORIZONTAL, command=self.main_canvas.xview)

        # # Configure scrollbars
        # self.scroll_y.pack(side=RIGHT, fill=Y)
        # self.scroll_x.pack(side=BOTTOM, fill=X)

        # self.main_frame = Frame(self.main_canvas)
        # self.main_canvas.create_window((0, 0), window=self.main_frame, anchor="nw")

        # self.main_canvas.configure(yscrollcommand=self.scroll_y.set, xscrollcommand=self.scroll_x.set)
        # self.main_canvas.pack(side=LEFT, fill=BOTH, expand=True)

    

        # Title Label
        lbltitle = Label(
            self.root,
            bd=10,
            relief=RIDGE,
            text="HOSPITAL MANAGEMENT SYSTEM",
            fg="red",
            bg="pink",
            font=("times new roman", 30, "bold"),
            padx=20,
            pady=20,
        )
        lbltitle.pack(side=TOP, fill=X)

        # Data Frame
        DataFrame = Frame(self.root, bd=15, padx=20, relief=RIDGE)
        DataFrame.place(x=0, y=130, width=1500, height=600)

        self.DataFrameLeft = LabelFrame(
            DataFrame,
            bd=15,
            relief=RIDGE,
            padx=15,
            font=("arial", 12, "bold"),
            text="Patient Information",
        )
        self.DataFrameLeft.place(x=0, y=2, width=1200, height=350)

        self.DataFrameRight = LabelFrame(
            DataFrame,
            bd=15,
            relief=RIDGE,
            padx=15,
            font=("arial", 12, "bold"),
            text="Prescription",
        )
        self.DataFrameRight.place(x=900, y=2, width=500, height=350)

        # Buttons Frame
        ButtonFrame = Frame(self.root, bd=15, padx=20, relief=RIDGE)
        ButtonFrame.place(x=0, y=530, width=1500, height=70)

        # Details Frame
        DetailsFrame = Frame(self.root, bd=15, padx=20, relief=RIDGE)
        DetailsFrame.place(x=0, y=600, width=1500, height=190)

        # DataFrame Left Labels and Entries
        textvariable=self.Nameoftablets
        textvariable=self.ref
        textvariable=self.Dose
        textvariable=self.NumberofTablets
        textvariable=self.Lot
        textvariable=self.Issuedate
        textvariable=self.ExpDate
        textvariable=self.DailyDose
        textvariable=self.sideEffect
        textvariable=self.FutherInformation
        textvariable=self.BloodPressure
        textvariable=self.StorageAdvice
        textvariable=self.Medication
        textvariable=self.PatientId
        textvariable=self.nhsNumber
        textvariable=self.PatientName
        textvariable=self.DateOfBirth
        textvariable=self.PatientAddress

        labels = [
            "Name of Tablets", "Reference No:", "Dose:", "No of Tablets:", "Lot:",
            "Issue Date:", "Exp Date:", "Daily Dose:", "Side Effect:",
            "Further Information:", "Blood Pressure:", "Storage Advice:",
            "Medication:", "Patient ID:", "NHS Number:", "Patient Name:",
            "Date of Birth:", "Patient Address:"
        ]

        self.entries = {}
        for i, label in enumerate(labels):
            lbl = Label(
                self.DataFrameLeft,
                text=label,
                font=("arial", 12, "bold"),
                padx=2,
                pady=6,
            )
            lbl.grid(row=i, column=0, sticky=W)
            self.entries[label] = Entry(
                self.DataFrameLeft, font=("arial", 13, "bold"), width=35
            )
            self.entries[label].grid(row=i, column=1)

        # Dropdown for "Name of Tablet"
        self.entries["Name of Tablets"] = ttk.Combobox(
            self.DataFrameLeft,
            font=("times new roman", 12, "bold"),
            width=33,
            state="readonly",
        )
        self.entries["Name of Tablets"]["values"] = (
            "Nice",
            "Corona vaccine",
            "Acetaminophen",
            "Adderall",
            "Amlodipine",
            "Ativan",
        )
        self.entries["Name of Tablets"].grid(row=0, column=1)

        # DataFrame Right Text Box
        self.txtPrescription = Text(
            self.DataFrameRight, font=("arial", 12, "bold"), width=45, height=16, padx=2
        )
        self.txtPrescription.grid(row=0, column=0)

        # Buttons in Button Frame
        self.create_buttons(ButtonFrame)

    def create_buttons(self, frame):
        buttons = [
            ("Prescription", self.prescription),
            ("Prescription Data", self.prescription_data),
            ("Update", self.update),
            ("Delete", self.delete),
            ("Clear", self.clear),
            ("Exit", self.exit),
        ]
        for i, (text, command) in enumerate(buttons):
            btn = Button(
                frame,
                text=text,
                bg="green",
                fg="white",
                font=("arial", 12, "bold"),
                width=18,
                command=command,
            )
            btn.grid(row=0, column=i, padx=10)

    # Button methods
    def prescription(self):
        self.txtPrescription.insert(
            END, f"Prescription: \n{'-'*30}\n"
        )
        for key, entry in self.entries.items():
            self.txtPrescription.insert(
                END, f"{key}: {entry.get()}\n"
            )

    def prescription_data(self):
        messagebox.showinfo("Info", "Prescription Data Functionality")
        pass

    def update(self):
        messagebox.showinfo("Info", "Update Functionality")
        pass

    def delete(self):
        for entry in self.entries.values():
            entry.delete(0, END)
        self.txtPrescription.delete(1.0, END)
        pass

    def clear(self):
        self.delete()

        def fetch_data(self):
            pass

    def exit(self):
        self.root.destroy()


# ========================Table================
# ========================Scrollbar================
        # Details Frame
        self.DetailsFrame = Frame(self.root, bd=20, padx=20, relief=RIDGE)
        self.DetailsFrame.place(x=0, y=600, width=1500, height=190)

        # Scrollbars and Treeview
        scroll_x = ttk.Scrollbar(self.DetailsFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.DetailsFrame, orient=VERTICAL)

        self.hospital_table = ttk.Treeview(
            self.DetailsFrame,
            column=("nameoftable", "ref", "dose", "nooftablets", "lot", "issuedate", "expdate", 
                    "dailydose", "storage", "nhsnumber", "pname", "dob", "address"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftables", text="Name of Tables")
        self.hospital_table.heading("ref", text="Reference No.")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablets", text="Number of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text="Address")

        self.hospital_table["show"] = "headings"
      

        self.hospital_table.column("nameoftables",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftables",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)




        self.fetch_data()

        # =================Functinality declration============
        def iprescriptionData(self):
            if self.Nameoftablets.get()=="" or self.ref.get()=="":
             messagebox.showerror("error","All fields are required")
            else:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="Hospital")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,,%s,,%s,,%s)",(
                    self.Nameoftablets.get(),
                     self.ref.get(),
                      self.Dose.get(),
                       self.Numberoftablets.get(),
                        self.Lot.get(),
                         self.Issuedate.get(),
                          self.Expdate.get(),
                           self.DailyDose.get(),
                            self.StorageAdvice.get(),
                             self.nhsNumber.get(),
                              self.PatientName.get(),
                               self.DateOfBirth.get(),
                                self.PatientAddress.get(),
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Record has been inserted")
                def update(self):
                    conn=mysql.connector.connect(host="localhsot",username="root",password="root",database="Hospital")
                my_cursor=conn.cursor()
                my_cursor.execute("update hospital set Nameoftablets=%s,Dose=%s,NumberofTablets=%s,Lot=%s,Issuedate=%s,ExpDate=%s,DailyDose=%s,StorageAdvice=%s,nhsNumber=%s,PatientName=%s,DateOfBirth=%s,PatientAddress=%s where Reference_No=%s")








                def fetch_data(self):
                    conn=mysql.connector.connect(host="localhost",username="root",password="root",database="Hospital")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from hospital")
                rows=my_cursor.fatchall()
                if len(rows)!=0:
                    self.hospital_table.delete(*self.hospital_table.get_children())
                    for i in rows:
                        self.hospital_table.insert("",END,values=i)
                        conn.commit()
                        conn.close()

                        def get_cursor(self,event=""):
                            cursor_row=self.hospital_table.focus()
                            content=self.hospital_table.item(cursor_row)
                            row=content["values"]
                            self.Nameoftablets.set(row[0])
                            self.ref.set(row[1])
                            self.Dose.set(row[2])
                            self.NumberofTablets.set(row[3])
                            self.Lot.set(row[4])
                            self.Issuedate.set(row[5])
                            self.ExpDate.set(row[6])
                            self.DailyDose.set(row[7])
                            self.StorageAdvice.set(row[8])
                            self.nhsNumber.set(row[9])
                            self.PatientName.set(row[10])
                            self.DateOfBirth.set(row[11])
                            self.PatientAddress.set(row[12])


                            def iPrectiontion(self):
                                self.txtPrescription.insert(END,"name of Tablets:\t\t\t"+self.NameOftablets.get()+"\n")
                                self.txtPrescription.insert(END,"Reference No:\t\t\t"+self.ref.get()+"\n")
                                self.txtPrescription.insert(END,"Dose:\t\t\t"+self.Dose.get()+"\n")
                                self.txtPrescription.insert(END,"number of Tablets:\t\t\t"+self.NumberOftablets.get()+"\n")
                                self.txtPrescription.insert(END,"Lot:\t\t\t"+self.Lot.get()+"\n")
                                self.txtPrescription.insert(END,"Issue date:\t\t\t"+self.Issuedate.get()+"\n")
                                self.txtPrescription.insert(END,"Exp date:\t\t\t"+self.ExpDate.get()+"\n")
                                self.txtPrescription.insert(END,"daily Dose:\t\t\t"+self.DailyDose.get()+"\n")
                                self.txtPrescription.insert(END,"Side Effect:\t\t\t"+self.sideEffect.get()+"\n")
                                self.txtPrescription.insert(END,"Futher Information:\t\t\t"+self.FutherInformation.get()+"\n")
                                self.txtPrescription.insert(END,"StorageAdvice:\t\t\t"+self.StorageAdvice.get()+"\n")
                                self.txtPrescription.insert(END,"DrivinUsingMachine:\t\t\t"+self.DrivinUsingMachine.get()+"\n")
                                self.txtPrescription.insert(END,"PatientId:\t\t\t"+self.PatientID.get()+"\n")
                                self.txtPrescription.insert(END,"NHSNUmber:\t\t\t"+self.nhsNumber.get()+"\n")
                                self.txtPrescription.insert(END,"Patientname:\t\t\t"+self.PatientName.get()+"\n")
                                self.txtPrescription.insert(END,"DateOfBirth:\t\t\t"+self.DateOfBirth.get()+"\n")
                                self.txtPrescription.insert(END,"PatientAddress:\t\t\t"+self.PatientAddress.get()+"\n")

                                def idelete(self):
                                    conn=mysql.connector.connect(host="localhost",username="root",password="root",database="Hospital")
                my_cursor=conn.cursor()
                query="delete from hospital where Reference_No=%s"
                value=(self.ref.get(),)
                my_cursor.execute(query,value)
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("delete","patient has been deleted successfully ")


                def clear(self):
                    self.Nameoftablets.set("")
                    self.ref.set("")
                    self.Dose.set("")
                    self.NumberofTablets.set("")
                    self.Lot.set("")
                    self.Issuedate.set("")
                    self.ExpDate.set("")
                    self.DailyDose.set("")
                    self.sideEffect.set("")
                    self.FurtherInformation.set("")
                    self.StorageAdvice.set("")
                    self.DrivingUsingMachine.set("")
                    self.HowToUseMedication.set("")
                    self.PatientId.set("")
                    self.nhsNumber.set("")
                    self.PatientName.set("")
                    self.DateOfBirth.set("")
                    self.PatientAddress.set("")
                    self.txtPrescription.set("")

                    def IExit(self):
                        iExit=messagebox.askyesno("Hospital Management System","Confirm you want to exit")
                        if IExit>0:
                            root.destroy()
                            return
                        

                        


if __name__ == "__main__":
    root = Tk()
    ob = Hospital(root)
    root.mainloop()
