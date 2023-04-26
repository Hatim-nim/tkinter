import tkinter as tk
from tkinter import ttk
import tkinter
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import *
import customtkinter
import sqlite3
import os
import re

# creating connection from "show order" button in shipme
def show_order(shipID, shipment_id_root):
    #connect to DB
    conn = sqlite3.connect('C:/Users/Hamad/Desktop/CPIT-251/tkinter/pickbox.db')
    c = conn.cursor()

    order = c.execute("SELECT * FROM shipments WHERE shipid = ?", (shipID.get(),)).fetchall()

    print(order)
    #commit changes/save them
    conn.commit()
    conn.close()

    for widget in shipment_id_root.winfo_children():
        widget.destroy()

    # Create a frame to show the orders
    order_frame = tk.Frame(shipment_id_root)
    order_frame.pack()

    # Create a treeview to show the orders
    treeview = ttk.Treeview(order_frame)
    treeview.pack()

    treeview["columns"] = ("shipment_id", "status", "delivery_time", "locker_id", "pickboxid", "email", "storeid","storename","phone")
    treeview.column("#0", width=0, stretch=tk.NO)
    treeview.column("shipment_id", anchor=tk.CENTER, width=60)
    treeview.column("status", anchor=tk.CENTER, width=80)
    treeview.column("delivery_time", anchor=tk.CENTER, width=100)
    treeview.column("locker_id", anchor=tk.CENTER, width=40)
    treeview.column("pickboxid", anchor=tk.CENTER, width=40)
    treeview.column("email", anchor=tk.CENTER, width=120)
    treeview.column("storeid", anchor=tk.CENTER, width=50)
    treeview.column("storename", anchor=tk.CENTER, width=100)
    treeview.column("phone", anchor=tk.CENTER, width=100)
    # Set up the headings of the columns
    treeview.heading("#0", text="", anchor=tk.W)
    treeview.heading("shipment_id", text="Shipment ID", anchor=tk.CENTER)
    treeview.heading("status", text="Status", anchor=tk.CENTER)
    treeview.heading("delivery_time", text="Delivery Time", anchor=tk.CENTER)
    treeview.heading("locker_id", text="Locker ID", anchor=tk.CENTER)
    treeview.heading("pickboxid", text="PickBox ID", anchor=tk.CENTER)
    treeview.heading("email", text="Email", anchor=tk.CENTER)
    treeview.heading("storeid", text="Store ID", anchor=tk.CENTER)
    treeview.heading("storename", text="Store Name", anchor=tk.CENTER)
    treeview.heading("phone", text="Phone Number", anchor=tk.CENTER)   

    row_count = 0
    for oneorder in order:
        treeview.insert("", row_count, text="", values=oneorder)
        row_count += 1
    pass


#This method recieves a number and searches the DB for matching rows using a query with a condition of matching the number
#Basically display all orders that have the same phone number
def show_orders(Pnum, phone_number_root):

    # Connect to database
    conn = sqlite3.connect('C:/Users/Hamad/Desktop/CPIT-251/tkinter/pickbox.db')
    c = conn.cursor()
    # Get orders from database for the entered phone number
    number=Pnum.get()
    print(number)
    orders = c.execute("SELECT * FROM shipments WHERE phone = ?", (Pnum.get(),)).fetchall()
    
    print(orders)
    # Close the database connection
    conn.commit()
    conn.close()

    # Clear the existing frame, if any
    for widget in phone_number_root.winfo_children():
        widget.destroy()

    # Create a frame to show the orders
    orders_frame = tk.Frame(phone_number_root)
    orders_frame.pack()

    # Create a treeview to show the orders
    treeview = ttk.Treeview(orders_frame)
    treeview.pack()

    # Set up the columns of the treeview
    treeview["columns"] = ("shipment_id", "status", "delivery_time", "locker_id", "pickboxid", "email", "storeid","storename","phone")
    treeview.column("#0", width=0, stretch=tk.NO)
    treeview.column("shipment_id", anchor=tk.CENTER, width=60)
    treeview.column("status", anchor=tk.CENTER, width=80)
    treeview.column("delivery_time", anchor=tk.CENTER, width=100)
    treeview.column("locker_id", anchor=tk.CENTER, width=40)
    treeview.column("pickboxid", anchor=tk.CENTER, width=40)
    treeview.column("email", anchor=tk.CENTER, width=120)
    treeview.column("storeid", anchor=tk.CENTER, width=50)
    treeview.column("storename", anchor=tk.CENTER, width=100)
    treeview.column("phone", anchor=tk.CENTER, width=100)
    # Set up the headings of the columns
    treeview.heading("#0", text="", anchor=tk.W)
    treeview.heading("shipment_id", text="Shipment ID", anchor=tk.CENTER)
    treeview.heading("status", text="Status", anchor=tk.CENTER)
    treeview.heading("delivery_time", text="Delivery Time", anchor=tk.CENTER)
    treeview.heading("locker_id", text="Locker ID", anchor=tk.CENTER)
    treeview.heading("pickboxid", text="PickBox ID", anchor=tk.CENTER)
    treeview.heading("email", text="Email", anchor=tk.CENTER)
    treeview.heading("storeid", text="Store ID", anchor=tk.CENTER)
    treeview.heading("storename", text="Store Name", anchor=tk.CENTER)
    treeview.heading("phone", text="Phone Number", anchor=tk.CENTER)   
    # Insert the orders into the treeview
    row_count = 0
    for order in orders:
        treeview.insert("", row_count, text="", values=order)
        row_count += 1


def phone_number_page():
    # Create phone number page
    phone_number_root = customtkinter.CTk()
    phone_number_root.geometry("700x400")
    
    phone_number_root.title("Phone Number Page")
    phone_number_root.resizable(False, False)

    # create textboxes
    enter = customtkinter.CTkLabel(phone_number_root, text="Enter your phone number to show all your orders ", font=("Arial", 16))
    enter.pack()
    enter.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

    def validate_phone_number(new_value):
        return new_value.isdigit() or new_value == ""

    Pnum = customtkinter.CTkEntry(master=phone_number_root, width=220, validate="key", validatecommand=(phone_number_root.register(validate_phone_number), "%P"))
   
    Pnum.pack()
    Pnum.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

    show = customtkinter.CTkButton(phone_number_root, text="Show Orders", command=lambda: show_orders(Pnum, phone_number_root))
    show.pack()
    show.place(relx=0.8, rely=0.3, anchor=tkinter.CENTER)

    
    def refresh():
        phone_number_root.destroy()
        phone_number_page()

    refresh_button = customtkinter.CTkButton(phone_number_root, text="Refresh", command=refresh)
    refresh_button.pack()
    refresh_button.place(relx=0.9, rely=0.9, anchor=tkinter.CENTER)

    back_button = customtkinter.CTkButton(phone_number_root, text="Back to Main Page", command=phone_number_root.destroy)
    back_button.pack()
    back_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    phone_number_root.mainloop()

def shipment_id_page():
    # Create shipment id page
    shipment_id_root = customtkinter.CTk()
    shipment_id_root.geometry("700x400")
    
    shipment_id_root.title("Shipment ID Page")
    shipment_id_root.resizable(False, False)

    # create textboxes
    enter = customtkinter.CTkLabel(shipment_id_root, text="Enter your Shipment ID to show your shipment status ", font=("Arial", 16))
    enter.pack()
    enter.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

    def validate_shipment_id(new_value):
        return re.match(r'^[a-zA-Z0-9]*$', new_value) is not None or new_value == ""

    shipID = customtkinter.CTkEntry(master=shipment_id_root, width=220, placeholder_text="", validate="key", validatecommand=(shipment_id_root.register(validate_shipment_id), "%P"))
    shipID.pack()
    shipID.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

    show = customtkinter.CTkButton(shipment_id_root, text="Show Order", command=lambda:show_order(shipID, shipment_id_root))
    show.pack()
    show.place(relx=0.8, rely=0.3, anchor=tkinter.CENTER)

    def refresh():
        shipment_id_root.destroy()
        shipment_id_page()

    refresh_button = customtkinter.CTkButton(shipment_id_root, text="Refresh", command=refresh)
    refresh_button.pack()
    refresh_button.place(relx=0.9, rely=0.1, anchor=tkinter.CENTER)

    back_button = customtkinter.CTkButton(shipment_id_root, text="Back to Main Page", command=shipment_id_root.destroy)
    back_button.pack()
    back_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    shipment_id_root.mainloop()






# Create root window
root = customtkinter.CTk()
root.geometry("700x400")
root.title("Modern Login")
root.resizable(False,False)

# create DB
conn = sqlite3.connect('C:/Users/Hamad/Desktop/CPIT-251/tkinter/pickbox.db')
#create cursor
c= conn.cursor()

# create table
#  NOTE: 
# You SHOULD remove the following comments in first running/debugging
# THEN YOU SHOULD COMMENT THE FOLLOWING EXECUTIONS OR ELSE YOU WILL RECIEVE AN ERROR! 
# c.execute("""CREATE TABLE shipments (
#                 shipid integer,
#                 status text,
#                 deliveryTime text,
#                 lockerid integer,
#                 pickboxid integer,
#                 email text,
#                 storeid integer,
#                 storename text,
#                 phone integer
#             )""") 

# #insert initial info
# c.execute("INSERT INTO shipments (shipid, status, deliveryTime, lockerid, pickboxid, email, storeid, storename,phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?,?)",
#           (100001, 'Shipped', '2023-04-25, 11:00 AM', 1123, 1001, 'yaseer@gmail.com', 301, 'Guerlain', 966555411384))
# c.execute("INSERT INTO shipments (shipid, status, deliveryTime, lockerid, pickboxid, email, storeid, storename,phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?,?)",
#           (100002, 'Picked Up', '2023-01-2, 12:34 PM', 1124, 1001, 'Jacob@hotmail.com', 302, 'Al-Nahdi', 966555411384))
# c.execute("INSERT INTO shipments (shipid, status, deliveryTime, lockerid, pickboxid, email, storeid, storename,phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?,?)",
#           (100003, 'Cancelled', '2023-06-13, 8:20 AM', 1120, 1003, 'YousefXX@Yahoo.com', 304, 'Addidas',966580688210))
# c.execute("INSERT INTO shipments (shipid, status, deliveryTime, lockerid, pickboxid, email, storeid, storename,phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?,?)",
#           (100004, 'Out For Delivery', '2023-09-3, 6:46 PM', 1122, 1001, 'Hegazi@gmail.com', 305, 'Puma', 966580688210))
# c.execute("INSERT INTO shipments (shipid, status, deliveryTime, lockerid, pickboxid, email, storeid, storename,phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?,?)",
#           (100005, 'Out For Delivery', '2023-09-7, 6:20 PM', 1121, 1003, 'mohammed@gmail.com', 306, 'Coffee Mood', 966580688210))
# c.execute("INSERT INTO shipments (shipid, status, deliveryTime, lockerid, pickboxid, email, storeid, storename,phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?,?)",
#           (100006, 'Picked Up', '2023-09-12, 7:02 PM', 1127, 1001, 'Based@gmail.com', 301, 'Guerlain', 966555411384))
# c.execute("INSERT INTO shipments (shipid, status, deliveryTime, lockerid, pickboxid, email, storeid, storename,phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?,?)",
#           (100007, 'Picked Up', '2023-09-28, 9:09 AM', 1120, 1004, 'amjad26@gmail.com', 308, 'Tom Ford', 966507095266))
# c.execute("INSERT INTO shipments (shipid, status, deliveryTime, lockerid, pickboxid, email, storeid, storename,phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?,?)",
#           (100008, 'Picked Up', '2023-09-28, 9:12 AM', 1121, 1004, 'amjad26@gmail.com', 309, 'iHerb', 966507095266))
# c.execute("INSERT INTO shipments (shipid, status, deliveryTime, lockerid, pickboxid, email, storeid, storename,phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?,?)",
#           (100009, 'Picked Up', '2023-10-31, 9:12 AM', 1120, 1002, 'GordonsUncle@gmail.com', 309, 'iHerb', 966552495419))
# c.execute("INSERT INTO shipments (shipid, status, deliveryTime, lockerid, pickboxid, email, storeid, storename,phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?,?)",
#           (100009, 'Picked Up', '2023-10-31, 9:15 AM', 1121, 1002, 'GordonsUncle@gmail.com', 310, 'SesamBakery', 966552495419))
# c.execute("INSERT INTO shipments (shipid, status, deliveryTime, lockerid, pickboxid, email, storeid, storename,phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?,?)",
#           (100010, 'Shipped', '2023-12-1, 1:19 PM', 1122, 1002, 'GordonsUncle@gmail.com', 311, 'ArabiaOud', 966552495419))
# c.execute("INSERT INTO shipments (shipid, status, deliveryTime, lockerid, pickboxid, email, storeid, storename,phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?,?)",
#           (100011, 'Picked Up', '2023-01-6, 1:19 PM', 1120, 1009, 'Yaseen1423@gmail.com', 312, 'Macdonalds', 966554587433))

          # create textboxes


welcome_label = customtkinter.CTkLabel(root, text="Welcome to Pick Box!",  font=("Arial", 24))
welcome_label.pack()
welcome_label.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

choose_label = customtkinter.CTkLabel(root, text="Choose what suits you",  font=("Arial", 16))
choose_label.pack()
choose_label.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

phone_button = customtkinter.CTkButton(root, text="Phone Number", command=phone_number_page)
phone_button.pack()
phone_button.place(relx=0.3, rely=0.5, anchor=tkinter.CENTER)

shipment_button = customtkinter.CTkButton(root, text="Shipment ID", command=shipment_id_page)
shipment_button.pack()
shipment_button.place(relx=0.7, rely=0.5, anchor=tkinter.CENTER)



conn.commit()
conn.close()




print("Successful running!")


root.mainloop()
