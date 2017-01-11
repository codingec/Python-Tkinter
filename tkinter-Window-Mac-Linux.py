from Tkinter import *
import sqlite3


class Main():
    def __init__(self, master):
        frame=Frame(master, width=400,height=700)
        frame.pack()
        self.text=Label(frame, text="        ")
        self.text.pack()
        self.text.grid(row=0,sticky=W)
        self.text["text"]= "Product Bill"
        self.clientname=Entry(frame, text="ClientName", width=45)
        self.clientname.insert(0,"Client Name")
        self.clientname.pack()
        self.clientname.grid(row=1)
        self.clientname.bind("<FocusIn>",self.clearClientName)
        self.clientnumber=Entry(frame, text="ClientNumber", width=45)
        self.clientnumber.insert(0,"Client Number")
        self.clientnumber.pack()
        self.clientnumber.grid(row=2)
        self.clientnumber.bind("<FocusIn>",self.clearClientNumber)
        self.clientdir=Entry(frame, text="ClientDir", width=45)
        self.clientdir.insert(0,"Client address")
        self.clientdir.pack()
        self.clientdir.grid(row=3)
        self.clientdir.bind("<FocusIn>",self.clearClientDir)
        self.product=Entry(frame, text="Product", width=45)
        self.product.insert(0,"Product Name")
        self.product.pack()
        self.product.grid(row=4)
        self.product.bind("<FocusIn>",self.clearProduct)
        self.productNumber=Entry(frame, text="ProductNumber",width=45)
        self.productNumber.insert(0,"Product number")
        self.productNumber.pack()
        self.productNumber.grid(row=5)
        self.productNumber.bind("<FocusIn>",self.clearProductNumber)
        self.productPrice=Entry(frame, text="ProductPrice",width=45)
        self.productPrice.insert(0,"Product price")
        self.productPrice.pack()
        self.productPrice.grid(row=6)
        self.productPrice.bind("<FocusIn>",self.clearProductPrice)
        self.productHowMany=Entry(frame, text="Product_HowMany",width=45)
        self.productHowMany.insert(0,"How many Product?")
        self.productHowMany.pack()
        self.productHowMany.grid(row=7)
        self.productHowMany.bind("<FocusIn>",self.clearProductHowMany)
        self.btn=Button(frame, text="Bill", command=self.Bill)
        self.btn.pack()
        self.btn.grid(row=10,rowspan=1,sticky="w")
        self.delbtn=Button(frame,text="Delete",command=self.Delete)
        self.delbtn.pack()
        self.delbtn.grid(row=10,rowspan=1,sticky="e")
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.content=Listbox(master,width=100)
        self.content.pack()
        self.content.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.content.yview)
        self.conec=sqlite3.connect('productBill.db')
        cur = self.conec.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS products("
                         "id INTEGER PRIMARY KEY AUTOINCREMENT ,"
                         "Client_Name TEXT NOT NULL,"
                         "Client_Number TEXT NOT NULL,"
                         "Client_dir TEXT NOT NULL,"
                         "Phone_number  TEXT NOT NULL,"
                         "Product_Name TEXT NOT NULL,"
                         "Product_Price TEXT NOT NULL,"
                         "Product_HowMany TEXT NOT NULL,"
                         "Product_Total TEXT NOT NULL)")
        self.conec.commit()
        selectAll=cur.execute("SELECT * FROM products")
        self.conec.commit()
        
        for i in selectAll:
            self.content.insert(END,'Client Name:', i[1],' ','Client Number:', i[2],' ','Client Addres:', i[3],' ','Phone number:', i[4],' ','Phone name:', i[5],' ','Phone price:', i[6],' ','How many:', i[7],' ','Total Price:', i[8])
            
        cur.close()
        
        
    def clearClientName(self,event):
        self.clientname.delete(0,END)

    def clearClientNumber(self,event):
        self.clientnumber.delete(0,END)
        
    def clearClientDir(self,event):
        self.clientdir.delete(0,END)
        
    def clearProduct(self,event):
        self.product.delete(0,END)
        
    def clearProductNumber(self,event):
        self.productNumber.delete(0,END)
        
    def clearProductPrice(self,event):
        self.productPrice.delete(0,END)
    
    def clearProductHowMany(self,event):
        self.productHowMany.delete(0,END)
        
    def clearProductTotal(self,event):
        self.productTotal.delete(0,END)
        
    def Bill(self):
        if self.clientname.get() =="":
            self.text["text"]="Product Bill"
        else:
            itemName = self.clientname.get()
            itemNumber = self.clientnumber.get()
            itemDir = self.clientdir.get()
            itemProduct = self.product.get()
            itemPnumber = self.productNumber.get()
            itemPprice = self.productPrice.get()
            itemPmany = self.productHowMany.get()
            manier = int(itemPprice)
            Pricise = int(itemPmany)
            sumPro = manier * Pricise
            self.clientname.delete(0,END)
            self.clientnumber.delete(0,END)
            self.clientdir.delete(0,END)
            self.product.delete(0,END)
            self.productNumber.delete(0,END)
            self.productPrice.delete(0,END)
            self.productHowMany.delete(0,END)
            cur = self.conec.cursor()
            cur.execute("INSERT INTO products(Client_Name,Client_Number,Client_dir,Phone_number,Product_Name,Product_Price,Product_HowMany,Product_Total) VALUES (?,?,?,?,?,?,?,?)",(itemName,itemNumber,itemDir,itemProduct,itemPnumber,itemPprice,itemPmany,sumPro))
            self.conec.commit()
            cur.close()
            self.content.insert(END,(itemName,itemNumber,itemDir,itemProduct,itemPnumber,itemPprice,itemPmany,sumPro))

    def Delete(self):
        whats = self.content.get(ACTIVE)
        contextEd = whats[0]
        cur=self.conec.cursor()
        cur.execute("DELETE FROM products WHERE Product_Name=(?)",(contextEd,))
        self.conec.commit()
        cur.close()
        self.content.delete(ANCHOR)


    def __del__(self):
        
        self.conec.close()


app = Tk()
app.title("BILL")
Main(app)
app.mainloop()
