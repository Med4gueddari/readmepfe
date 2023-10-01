from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# import sqlite3
import mysql.connector
from tkinter import colorchooser
from configparser import ConfigParser
import pyperclip
from bs4 import BeautifulSoup

root = Tk()
root.title('Carrefour - Magasin')
# root.iconbitmap('c:/gui/codemy.ico')
root.geometry("1400x650")

# Read our config file and get colors
parser = ConfigParser()
parser.read("C:/Users/safouane.elharrak/Documents/Sujet PFE/treebase.ini")
saved_primary_color = parser.get('colors', 'primary_color')
saved_secondary_color = parser.get('colors', 'secondary_color')
saved_highlight_color = parser.get('colors', 'highlight_color')



def query_database():
    # Clear the Treeview
    for record in my_tree.get_children():
        my_tree.delete(record)
        
    # Connect to the MySQL database
    conn = mysql.connector.connect(host='localhost',
                                         database='sco_db',
                                         user='root',
                                         password='')

    # Create a cursor instance
    c = conn.cursor()

    c.execute("SELECT * FROM magasin")
    records = c.fetchall()
    
    # Add our data to the screen
    global count
    count = 0
    
    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6],record[7], record[8], record[9], record[10], record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18],record[19]), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6],record[7], record[8], record[9], record[10], record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18],record[19]), tags=('oddrow',))
        # increment counter
        count += 1

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()




def search_records():
    lookup_record = search_entry.get()
    # close the search box
    search.destroy()

    # Clear the Treeview
    for record in my_tree.get_children():
        my_tree.delete(record)

    # Connect to the MySQL database
    conn = mysql.connector.connect(host='localhost',
                                         database='sco_db',
                                         user='root',
                                         password='')

    # Create a cursor instance
    c = conn.cursor()

    c.execute("SELECT * FROM magasin WHERE Nom like %s", (f"%{lookup_record}%",))
    records = c.fetchall()

    # Add our data to the screen
    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5],record[6], record[7], record[8], record[9], record[10], record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18],record[19]), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5],record[6], record[7], record[8], record[9], record[10], record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18],record[19]), tags=('oddrow',))
        # increment counter
        count += 1

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()


def lookup_records():
	global search_entry, search

	search = Toplevel(root)
	search.title("Lookup Records")
	search.geometry("400x200")
	# search.iconbitmap('c:/gui/codemy.ico')

	# Create label frame
	search_frame = LabelFrame(search, text="Nom")
	search_frame.pack(padx=10, pady=10)

	# Add entry box
	search_entry = Entry(search_frame, font=("Helvetica", 18))
	search_entry.pack(pady=20, padx=20)

	# Add button
	search_button = Button(search, text="Search Records", command=search_records)
	search_button.pack(padx=20, pady=20)



def primary_color():
	# Pick Color
	primary_color = colorchooser.askcolor()[1]

	# Update Treeview Color
	if primary_color:
		# Create Striped Row Tags
		my_tree.tag_configure('evenrow', background=primary_color)

		# Config file
		parser = ConfigParser()
		parser.read("C:/Users/safouane.elharrak/Documents/Sujet PFE/treebase.ini")
		# Set the color change
		parser.set('colors', 'primary_color', primary_color)
		# Save the config file
		with open('C:/Users/safouane.elharrak/Documents/Sujet PFE/treebase.ini', 'w') as configfile:
			parser.write(configfile)


def secondary_color():
	# Pick Color
	secondary_color = colorchooser.askcolor()[1]
	
	# Update Treeview Color
	if secondary_color:
		# Create Striped Row Tags
		my_tree.tag_configure('oddrow', background=secondary_color)
		
		# Config file
		parser = ConfigParser()
		parser.read("C:/Users/safouane.elharrak/Documents/Sujet PFE/treebase.ini")
		# Set the color change
		parser.set('colors', 'secondary_color', secondary_color)
		# Save the config file
		with open('C:/Users/safouane.elharrak/Documents/Sujet PFE/treebase.ini', 'w') as configfile:
			parser.write(configfile)

def highlight_color():
	# Pick Color
	highlight_color = colorchooser.askcolor()[1]

	#Update Treeview Color
	# Change Selected Color
	if highlight_color:
		style.map('Treeview',
			background=[('selected', highlight_color)])

		# Config file
		parser = ConfigParser()
		parser.read("C:/Users/safouane.elharrak/Documents/Sujet PFE/treebase.ini")
		# Set the color change
		parser.set('colors', 'highlight_color', highlight_color)
		# Save the config file
		with open('C:/Users/safouane.elharrak/Documents/Sujet PFE/treebase.ini', 'w') as configfile:
			parser.write(configfile)

def reset_colors():
	# Save original colors to config file
	parser = ConfigParser()
	parser.read('C:/Users/safouane.elharrak/Documents/Sujet PFE/treebase.ini')
	parser.set('colors', 'primary_color', 'lightblue')
	parser.set('colors', 'secondary_color', 'white')
	parser.set('colors', 'highlight_color', '#347083')
	with open('C:/Users/safouane.elharrak/Documents/Sujet PFE/treebase.ini', 'w') as configfile:
			parser.write(configfile)
	# Reset the colors
	my_tree.tag_configure('oddrow', background='white')
	my_tree.tag_configure('evenrow', background='lightblue')
	style.map('Treeview',
			background=[('selected', '#347083')])

# Add Menu
my_menu = Menu(root)
root.config(menu=my_menu)



# Configure our menu
option_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Options", menu=option_menu)
# Drop down menu
option_menu.add_command(label="Primary Color", command=primary_color)
option_menu.add_command(label="Secondary Color", command=secondary_color)
option_menu.add_command(label="Highlight Color", command=highlight_color)
option_menu.add_separator()
option_menu.add_command(label="Reset Colors", command=reset_colors)
option_menu.add_separator()
option_menu.add_command(label="Exit", command=root.quit)

#Search Menu
search_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Search", menu=search_menu)
# Drop down menu
search_menu.add_command(label="Search", command=lookup_records)
search_menu.add_separator()
search_menu.add_command(label="Reset", command=query_database)

# Do some database stuff

# Create a database or connect to one that exists

# Create a connection to the database
conn = mysql.connector.connect(host='localhost',
                                         database='sco_db',
                                         user='root',
                                         password='')

# Create a cursor instance
c = conn.cursor()

# Create Table
c.execute("""CREATE TABLE if not exists magasin (
    ID int,
	Numéro int,
    Nom varchar(22),
    format varchar(5),
    Code_CARINE int,
    Profil varchar(7),
    Nom_poste varchar(14),
    Terminal int,
    Opérateur int,
    Pwd int,
    IP_poste varchar(13),
    Masque_varchar varchar(13),
    Passerelle varchar(13),
    Nom_Master varchar(14),
    IP_Master varchar(13),
    IP_Glory varchar(13),
    Balance varchar(3),
    Type_SCA varchar(8),
    Cash varchar(9),
    EAS varchar(3)
    )""")


# Add dummy data to table
'''
for record in data:
	c.execute("INSERT INTO magasin (ID,Numéro, Nom, format, Code_CARINE, Profil, Nom_poste, Terminal, Opérateur, Pwd, IP_poste, Masque, Passerelle, Nom_Master, IP_Master, IP_Glory, Balance, Type_SCA, Cash, EAS) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
		(record[0], record[1], record[2], record[3], record[4], record[5], record[6],record[7], record[8], record[9], record[10], record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18],record[19])
		)
'''

# Commit changes
conn.commit()

# Close our connection
conn.close()


# Add Some Style
style = ttk.Style()

# Pick A Theme
style.theme_use('default')

# Configure the Treeview Colors
style.configure("Treeview",
	background="#D3D3D3",
	foreground="black",
	rowheight=25,
	fieldbackground="#D3D3D3")

# Change Selected Color #347083
style.map('Treeview',
	background=[('selected', saved_highlight_color)])

# Create a Treeview Frame
tree_frame = Frame(root)
tree_frame.pack(pady=10)  ######

# Create a Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll2 = Scrollbar(tree_frame)

tree_scroll.pack(side=RIGHT, fill=Y)
tree_scroll2.pack(side=TOP, fill=X)

# Create The Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# Configure the Scrollbar
tree_scroll.config(command=my_tree.yview)
tree_scroll2.config(orient='horizontal',command=my_tree.xview)

# Define Our Columns
my_tree['columns'] = ("ID","Numéro", "Nom", "Format", "Code_Carine", "Profil", "Nom_poste", "Terminal","Opérateur","Pwd","IP_Poste","Masque","Passerelle","Nom_Master","IP_Master","IP_Glory","Balance","Type_SCA","Cash","EAS")

# Format Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("ID", anchor=W, width=140)
my_tree.column("Numéro", anchor=W, width=140)
my_tree.column("Nom", anchor=W, width=140)
my_tree.column("Format", anchor=CENTER, width=100)
my_tree.column("Code_Carine", anchor=CENTER, width=140)
my_tree.column("Profil", anchor=CENTER, width=140)
my_tree.column("Nom_poste", anchor=CENTER, width=140)
my_tree.column("Terminal", anchor=CENTER, width=140)
my_tree.column("Opérateur", anchor=CENTER, width=140)
my_tree.column("Pwd", anchor=CENTER, width=140)
my_tree.column("IP_Poste", anchor=CENTER, width=140)
my_tree.column("Masque", anchor=CENTER, width=140)
my_tree.column("Passerelle", anchor=CENTER, width=140)
my_tree.column("Nom_Master", anchor=CENTER, width=140)
my_tree.column("IP_Glory", anchor=CENTER, width=140)
my_tree.column("Balance", anchor=CENTER, width=140)
my_tree.column("Type_SCA", anchor=CENTER, width=140)
my_tree.column("Cash", anchor=CENTER, width=140)
my_tree.column("EAS", anchor=CENTER, width=140)


# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("ID", text="ID", anchor=W)
my_tree.heading("Numéro", text="Numéro", anchor=W)
my_tree.heading("Nom", text="Nom", anchor=W)
my_tree.heading("Format", text="Format", anchor=CENTER)
my_tree.heading("Code_Carine", text="Code_Carine", anchor=CENTER)
my_tree.heading("Profil", text="Profil", anchor=CENTER)
my_tree.heading("Nom_poste", text="Nom_poste", anchor=CENTER)
my_tree.heading("Terminal", text="Terminal", anchor=CENTER)
my_tree.heading("Opérateur", text="Opérateur", anchor=CENTER)
my_tree.heading("Pwd", text="Pwd", anchor=CENTER)
my_tree.heading("IP_Poste", text="IP_Poste", anchor=CENTER)
my_tree.heading("Masque", text="Masque", anchor=CENTER)
my_tree.heading("Passerelle", text="Passerelle", anchor=CENTER)
my_tree.heading("Nom_Master", text="Nom_Master", anchor=CENTER)
my_tree.heading("IP_Master", text="IP_Master", anchor=CENTER)
my_tree.heading("IP_Glory", text="IP_Glory", anchor=CENTER)
my_tree.heading("Balance", text="Balance", anchor=CENTER)
my_tree.heading("Type_SCA", text="Type_SCA", anchor=CENTER)
my_tree.heading("Cash", text="Cash", anchor=CENTER)
my_tree.heading("EAS", text="EAS", anchor=CENTER)
# Create Striped Row Tags
my_tree.tag_configure('oddrow', background=saved_secondary_color)
my_tree.tag_configure('evenrow', background=saved_primary_color)



# Add Record Entry Boxes
data_frame = LabelFrame(root, text="Record")
data_frame.pack(fill="x", expand="yes", padx=20)

id_label = Label(data_frame, text="ID")
id_label.grid(row=0, column=0, padx=10, pady=10)
id_entry = Entry(data_frame)
id_entry.grid(row=0, column=1, padx=10, pady=10)

num_label = Label(data_frame, text="Numéro")
num_label.grid(row=0, column=2, padx=10, pady=10)
num_entry = Entry(data_frame)
num_entry.grid(row=0, column=3, padx=10, pady=10)

nom_label = Label(data_frame, text="Nom")
nom_label.grid(row=0, column=4, padx=10, pady=10)
nom_entry = Entry(data_frame)
nom_entry.grid(row=0, column=5, padx=10, pady=10)

format_label = Label(data_frame, text="Format")
format_label.grid(row=0, column=6, padx=10, pady=10)
format_entry = Entry(data_frame)
format_entry.grid(row=0, column=7, padx=10, pady=10)

carine_label = Label(data_frame, text="Code_CARINE")
carine_label.grid(row=0, column=8, padx=10, pady=10)
carine_entry = Entry(data_frame)
carine_entry.grid(row=0, column=9, padx=10, pady=10)
##
profil_label = Label(data_frame, text="Profil")
profil_label.grid(row=1, column=0, padx=10, pady=10)
profil_entry = Entry(data_frame)
profil_entry.grid(row=1, column=1, padx=10, pady=10)

nomposte_label = Label(data_frame, text="Nom_poste")
nomposte_label.grid(row=1, column=2, padx=10, pady=10)
nomposte_entry = Entry(data_frame)
nomposte_entry.grid(row=1, column=3, padx=10, pady=10)

terminal_label = Label(data_frame, text="Terminal")
terminal_label.grid(row=1, column=4, padx=10, pady=10)
terminal_entry = Entry(data_frame)
terminal_entry.grid(row=1, column=5, padx=10, pady=10)

operateur_label = Label(data_frame, text="Opérateur")
operateur_label.grid(row=1, column=6, padx=10, pady=10)
operateur_entry = Entry(data_frame)
operateur_entry.grid(row=1, column=7, padx=10, pady=10)

pwd_label = Label(data_frame, text="Pwd")
pwd_label.grid(row=1, column=8, padx=5, pady=10)
pwd_entry = Entry(data_frame)
pwd_entry.grid(row=1, column=9, padx=5, pady=10)
##
ipposte_label = Label(data_frame, text="IP_poste")
ipposte_label.grid(row=2, column=0, padx=10, pady=10)
ipposte_entry = Entry(data_frame)
ipposte_entry.grid(row=2, column=1, padx=10, pady=10)

masque_label = Label(data_frame, text="Masque")
masque_label.grid(row=2, column=2, padx=10, pady=10)
masque_entry = Entry(data_frame)
masque_entry.grid(row=2, column=3, padx=10, pady=10)

passerelle_label = Label(data_frame, text="Passerelle")
passerelle_label.grid(row=2, column=4, padx=10, pady=10)
passerelle_entry = Entry(data_frame)
passerelle_entry.grid(row=2, column=5, padx=10, pady=10)

nommaster_label = Label(data_frame, text="Nom_Master")
nommaster_label.grid(row=2, column=6, padx=10, pady=10)
nommaster_entry = Entry(data_frame)
nommaster_entry.grid(row=2, column=7, padx=10, pady=10)

ipmaster_label = Label(data_frame, text="IP_Master")
ipmaster_label.grid(row=2, column=8, padx=5, pady=10)
ipmaster_entry = Entry(data_frame)
ipmaster_entry.grid(row=2, column=9, padx=5, pady=10)
##
ipglory_label = Label(data_frame, text="IP_Glory")
ipglory_label.grid(row=3, column=0, padx=5, pady=10)
ipglory_entry = Entry(data_frame)
ipglory_entry.grid(row=3, column=1, padx=5, pady=10)

balance_label = Label(data_frame, text="Balance")
balance_label.grid(row=3, column=2, padx=5, pady=10)
balance_entry = Entry(data_frame)
balance_entry.grid(row=3, column=3, padx=5, pady=10)

sca_label = Label(data_frame, text="Type_SCA")
sca_label.grid(row=3, column=4, padx=5, pady=10)
sca_entry = Entry(data_frame)
sca_entry.grid(row=3, column=5, padx=5, pady=10)

cash_label = Label(data_frame, text="Cash")
cash_label.grid(row=3, column=6, padx=5, pady=10)
cash_entry = Entry(data_frame)
cash_entry.grid(row=3, column=7, padx=5, pady=10)

eas_label = Label(data_frame, text="EAS")
eas_label.grid(row=3, column=8, padx=5, pady=10)
eas_entry = Entry(data_frame)
eas_entry.grid(row=3, column=9, padx=5, pady=10)

# Move Row Up
def up():
	rows = my_tree.selection()
	# print(my_tree.selection())
	for row in rows:
		my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)

# Move Rown Down
def down():
	rows = my_tree.selection()
	for row in reversed(rows):
		my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)

# Remove one record
def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)

    # Create a database connection
    conn = mysql.connector.connect(host='localhost',
                                         database='sco_db',
                                         user='root',
                                         password='')
    # Create a cursor instance
    c = conn.cursor()

    # Delete from database
    c.execute("DELETE FROM magasin WHERE id=%s", (id_entry.get(),))

    # Commit changes
    conn.commit()

    # Close the connection
    conn.close()

    # Clear the entry boxes
    clear_entries()

    # Add a little message box for fun
    messagebox.showinfo("Deleted!", "Your Record Has Been Deleted!")




# Remove Many records
def remove_many():
    # Add a little message box for fun
    response = messagebox.askyesno("WOAH!!!!", "This Will Delete EVERYTHING SELECTED From The Table\nAre You Sure?!")

    #Add logic for message box
    if response == 1:
        # Designate selections
        x = my_tree.selection()

        # Create List of ID's
        ids_to_delete = []
        
        # Add selections to ids_to_delete list
        for record in x:
            ids_to_delete.append(my_tree.item(record, 'values')[2])

        # Delete From Treeview
        for record in x:
            my_tree.delete(record)

        # Create a database or connect to one that exists
        conn = mysql.connector.connect(host='localhost',
                                         database='sco_db',
                                         user='root',
                                         password='')
        # Create a cursor instance
        c = conn.cursor()
        

        # Delete Everything From The Table
        for id in ids_to_delete:
            c.execute("DELETE FROM magasin WHERE id = %s", (id,))

        # Reset List
        ids_to_delete = []


        # Commit changes
        conn.commit()

        # Close our connection
        conn.close()

        # Clear entry boxes if filled
        clear_entries()

import mysql.connector
from tkinter import messagebox

# Remove all records
def remove_all():
	# Add a little message box for fun
	response = messagebox.askyesno("WOAH!!!!", "This Will Delete EVERYTHING From The Table\nAre You Sure?!")

	# Add logic for message box
	if response == 1:
		# Clear the Treeview
		for record in my_tree.get_children():
			my_tree.delete(record)

		# Create a connection to the database
		conn = mysql.connector.connect(host='localhost',
                                         database='sco_db',
                                         user='root',
                                         password='')
		# Create a cursor instance
		c = conn.cursor()

		# Delete Everything From The Table
		c.execute("DROP TABLE IF EXISTS magasin")

		# Commit changes
		conn.commit()

		# Close our connection
		conn.close()

		# Clear entry boxes if filled
		clear_entries()

		# Recreate The Table
		create_table_again()

# Clear entry boxes
def clear_entries():
	# Clear entry boxes
	id_entry.delete(0, END)
	num_entry.delete(0, END)
	nom_entry.delete(0, END)
	format_entry.delete(0, END)
	carine_entry.delete(0, END)
	profil_entry.delete(0, END)
	nomposte_entry.delete(0, END)
	terminal_entry.delete(0, END)
	operateur_entry.delete(0, END)
	pwd_entry.delete(0, END)
	ipposte_entry.delete(0, END)	
	masque_entry.delete(0, END)
	passerelle_entry.delete(0, END)
	nommaster_entry.delete(0, END)
	ipmaster_entry.delete(0, END)
	ipglory_entry.delete(0, END)
	balance_entry.delete(0, END)
	sca_entry.delete(0, END)
	cash_entry.delete(0, END)
	eas_entry.delete(0, END)


# Select Record
def select_record(e):
	# Clear entry boxes
	id_entry.delete(0, END)
	num_entry.delete(0, END)
	nom_entry.delete(0, END)
	format_entry.delete(0, END)
	carine_entry.delete(0, END)
	profil_entry.delete(0, END)
	nomposte_entry.delete(0, END)
	terminal_entry.delete(0, END)
	operateur_entry.delete(0, END)
	pwd_entry.delete(0, END)
	ipposte_entry.delete(0, END)	
	masque_entry.delete(0, END)
	passerelle_entry.delete(0, END)
	nommaster_entry.delete(0, END)
	ipmaster_entry.delete(0, END)
	ipglory_entry.delete(0, END)
	balance_entry.delete(0, END)
	sca_entry.delete(0, END)
	cash_entry.delete(0, END)
	eas_entry.delete(0, END)

	# Grab record Number
	selected = my_tree.focus()
	# Grab record values
	values = my_tree.item(selected, 'values')

	# outpus to entry boxes
	id_entry.insert(0, values[0])
	num_entry.insert(0, values[1])
	nom_entry.insert(0, values[2])
	format_entry.insert(0, values[3])
	carine_entry.insert(0, values[4])
	profil_entry.insert(0, values[5])
	nomposte_entry.insert(0, values[6])
	terminal_entry.insert(0, values[7])
	operateur_entry.insert(0, values[8])
	pwd_entry.insert(0, values[9])
	ipposte_entry.insert(0, values[10])	
	masque_entry.insert(0, values[11])
	passerelle_entry.insert(0, values[12])
	nommaster_entry.insert(0, values[13])
	ipmaster_entry.insert(0, values[14])
	ipglory_entry.insert(0, values[15])
	balance_entry.insert(0, values[16])
	sca_entry.insert(0, values[17])
	cash_entry.insert(0, values[18])
	eas_entry.insert(0, values[19])




# Update record
def update_record():
    # Grab the record number
    selected = my_tree.focus()

    # Update record
    my_tree.item(selected, text="", values=(id_entry.get(), num_entry.get(), nom_entry.get(), format_entry.get(), carine_entry.get(), profil_entry.get(), nomposte_entry.get(),terminal_entry.get(),operateur_entry.get(),pwd_entry.get(),ipposte_entry.get(),masque_entry.get(),passerelle_entry.get(),nommaster_entry.get(),ipmaster_entry.get(),ipglory_entry.get(),balance_entry.get(),sca_entry.get(),cash_entry.get(),eas_entry.get()),)

    # Update the database
    # Connect to the database
    conn = mysql.connector.connect(host='localhost',
                                         database='sco_db',
                                         user='root',
                                         password='')

    # Create a cursor instance
    cursor = conn.cursor()

    # Update record in the database
    sql = """UPDATE magasin SET
            ID = %s,
            Numéro = %s,
            Nom = %s,
            Format = %s,
            Code_Carine = %s,
            Profil = %s,
            Nom_poste = %s,
            Terminal = %s,
            Opérateur = %s,
            Pwd = %s,
            IP_poste = %s,
            Masque = %s,
            Passerelle = %s
            Nom_Master = %s,
            IP_Master = %s,
            IP_Glory = %s,
            Balance = %s,
            Type_SCA = %s,
            Cash = %s,
            Eas = %s,
            WHERE id = %s"""

    values = (
		id_entry.get(), 
		num_entry.get(), 
		nom_entry.get(), 
		format_entry.get(), 
		carine_entry.get(), 
		profil_entry.get(), 
		nomposte_entry.get(),
		terminal_entry.get(),
		operateur_entry.get(),
		pwd_entry.get(),
		ipposte_entry.get(),
		masque_entry.get(),
		passerelle_entry.get(),
		nommaster_entry.get(),
		ipmaster_entry.get(),
		ipglory_entry.get(),
		balance_entry.get(),
		sca_entry.get(),
		cash_entry.get(),
		eas_entry.get(),
       
    )

    cursor.execute(sql, values)

    # Commit changes
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Clear entry boxes
    id_entry.delete(0, END)
    num_entry.delete(0, END)
    nom_entry.delete(0, END)
    format_entry.delete(0, END)
    carine_entry.delete(0, END)
    profil_entry.delete(0, END)
    nomposte_entry.delete(0, END)
    terminal_entry.delete(0, END)
    operateur_entry.delete(0, END)
    pwd_entry.delete(0, END)
    ipposte_entry.delete(0, END)	
    masque_entry.delete(0, END)
    passerelle_entry.delete(0, END)
    nommaster_entry.delete(0, END)
    ipmaster_entry.delete(0, END)
    ipglory_entry.delete(0, END)
    balance_entry.delete(0, END)
    sca_entry.delete(0, END)
    cash_entry.delete(0, END)
    eas_entry.delete(0, END)


# add new record to database
def add_record():
	# Update the database
	# Connect to MySQL database
	conn = mysql.connector.connect(host='localhost',
                                         database='sco_db',
                                         user='root',
                                         password='')
	# Create a cursor instance
	c = conn.cursor()

	# Add New Record
	c.execute("INSERT INTO magasin (ID, Numéro, Nom, format, Code_CARINE, Profil, Nom_poste, Terminal, Opérateur, Pwd, IP_poste, Masque, Passerelle, Nom_Master, IP_Master, IP_Glory, Balance, Type_SCA, Cash, EAS) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
		(id_entry.get(), num_entry.get(), nom_entry.get(), format_entry.get(), carine_entry.get(), profil_entry.get(), nomposte_entry.get(),terminal_entry.get(),operateur_entry.get(),pwd_entry.get(),ipposte_entry.get(),masque_entry.get(),passerelle_entry.get(),nommaster_entry.get(),ipmaster_entry.get(),ipglory_entry.get(),balance_entry.get(),sca_entry.get(),cash_entry.get(),eas_entry.get(),))

	# Commit changes
	conn.commit()

	# Close our connection
	conn.close()

	# Clear entry boxes
	id_entry.delete(0, END)
	num_entry.delete(0, END)
	nom_entry.delete(0, END)
	format_entry.delete(0, END)
	carine_entry.delete(0, END)
	profil_entry.delete(0, END)
	nomposte_entry.delete(0, END)
	terminal_entry.delete(0, END)
	operateur_entry.delete(0, END)
	pwd_entry.delete(0, END)
	ipposte_entry.delete(0, END)	
	masque_entry.delete(0, END)
	passerelle_entry.delete(0, END)
	nommaster_entry.delete(0, END)
	ipmaster_entry.delete(0, END)
	ipglory_entry.delete(0, END)
	balance_entry.delete(0, END)
	sca_entry.delete(0, END)
	cash_entry.delete(0, END)
	eas_entry.delete(0, END)

	# Clear The Treeview Table
	my_tree.delete(*my_tree.get_children())

	# Run to pull data from database on start
	query_database()

######################################

import subprocess

# fonction pour prend l'add ip selectioné 
# def get_ip():
# 	# Grab record Number
# 	selected = my_tree.focus()
# 	# Grab record values
# 	values = my_tree.item(selected, 'values')
# 	ip_add=values[10]
# 	# print(ip_add)
# 	return ip_add


import pyautogui
import time
import subprocess
# Fonction à exécuter lorsque le bouton est cliqué
# def connect_ultravnc():
#     # ipadd=get_ip()
# 	selected = my_tree.focus()
# # 	# Grab record values
# 	values = my_tree.item(selected, 'values')
# 	ip_add=values[10]
# 	print(ip_add)
#     # subprocess.call(["python", "C:/Users/safouane.elharrak/Documents/Sujet PFE/ultravnc.py"])
# 	# Attendre quelques secondes pour laisser le temps de basculer vers la fenêtre UltraVNC 
# 	time.sleep(1)
# 	# Coordonnées initiales du curseur
# 	# initial_position = pyautogui.position()
# 	# Réserver le curseur en maintenant le bouton de la souris enfoncé
# 	# pyautogui.mouseDown()
# 	# Chemin d'accès à l'exécutable UltraVNC (à adapter selon votre installation)
# 	ultravnc_path = "C:/Users/safouane.elharrak/Documents/ULTRAVNC/ULTRAVNC/vncviewer.exe"

# 	# Lancer UltraVNC
# 	subprocess.Popen(ultravnc_path)
# 	# Attendre quelques secondes pour laisser le temps de basculer vers la fenêtre UltraVNC
# 	time.sleep(2)
# 	# Coordonnées des boutons et champs de saisie dans l'interface UltraVNC (à adapter selon votre configuration)
# 	host_input = (970, 275)  # Coordonnées du champ de saisie pour l'adresse IP ou le nom d'hôte
# 	connect_button = (1159, 363)  # Coordonnées du bouton "Connect" ou "Connexion"
# 	# plugin_button = (720, 617)  # Coordonnées du bouton "DSMplugin"
# 	username_input = (1010, 480)  # Coordonnées du champ de saisie pour le nom d'utilisateur
# 	password_input = (1004, 520)  # Coordonnées du champ de saisie pour le mot de passe

# 	connexion_button = (1005, 567)  # Coordonnées du bouton "Connect" ou "Connexion"


# 	# Entrer l'adresse IP ou le nom d'hôte de la machine distante
# 	pyautogui.click(host_input)

# 	# Effectuer une combinaison de touches pour vider le champ de saisie
# 	pyautogui.hotkey('ctrl', 'a')  # Sélectionner tout le texte
# 	pyautogui.press('delete')  # Supprimer le texte sélectionné
# 	pyautogui.typewrite(ip_add)  # Remplacez par l'adresse IP ou le nom d'hôte réel

# 	# # Cliquer sur le bouton "DSMplugin" 
# 	# pyautogui.click(plugin_button)

# 	# Attendre quelques secondes pour laisser le temps de basculer 
# 	time.sleep(2)

# 	# Cliquer sur le bouton "Connect" ou "Connexion"
# 	pyautogui.click(connect_button)

# 	# Attendre quelques secondes pour laisser le temps de basculer 
# 	time.sleep(3)

# 	# Entrer le nom d'utilisateur
# 	pyautogui.click(username_input)
# 	pyautogui.typewrite('administrator')  

# 	# Entrer le mot de passe
# 	pyautogui.click(password_input)
# 	pyautogui.typewrite('Wind0ws10')  

# 	# Attendre quelques secondes pour laisser le temps de basculer 
# 	time.sleep(1)

# 	# Cliquer sur le bouton "Connexion"
# 	pyautogui.click(connexion_button)

# 	# # Relâcher le bouton de la souris pour libérer le curseur
# 	pyautogui.mouseUp()
	
# 	# try:
# 	# 	while True:
# 	# 		x, y = pyautogui.position()
# 	# 		position_str = f"X: {x}, Y: {y}"
# 	# 		print(position_str, end="\r")
# 	# except KeyboardInterrupt:
# 	# 	print("\nEnregistrement des coordonnées terminé.")

def connect_ultravnc():
    # ipadd=get_ip()
	selected = my_tree.focus()
# 	# Grab record values
	values = my_tree.item(selected, 'values')
	ip_add=values[10]
	chemin_vers_ultravnc = "C:/Users/safouane.elharrak/Documents/ULTRAVNC/ULTRAVNC/vncviewer.exe"
	subprocess.Popen([chemin_vers_ultravnc, ip_add])
# Attendez un certain temps pour permettre la fenêtre UltraVNC de s'afficher
	# Nom d'utilisateur pour la connexion à distance
	utilisateur = "administrator"
	# Mot de passe pour la connexion à distance       
	mot_de_passe = "Wind0ws10"
	time.sleep(2)
    # Entrer le nom d'utilisateur et le mot de passe
	pyautogui.typewrite(utilisateur)
	pyautogui.press('tab')
	pyautogui.typewrite(mot_de_passe)
	pyautogui.press('enter')


from ping3 import ping
def test_ping():
    # Designate selections
    x = my_tree.selection()
        # Create List of ID's
    ids_to_ping = []
    ids_reussi = []
    ids_echoué = []
        
        # Add selections to ids_to_delete list
    for b in x:
        ids_to_ping.append(my_tree.item(b, 'values')[10])

        # Delete From Treeview
    for a in ids_to_ping:
        # print(a)
        response_time=ping(a)
        if response_time is not None:
            ids_reussi.append(f"Le ping vers {a} a réussi. Temps de réponse : {response_time} ms ""\n")
            # messagebox.showinfo("ping test!", f"Le ping vers {a} a réussi. Temps de réponse : {response_time} ms")
            # print(f"Le ping vers {a} a réussi. Temps de réponse : {response_time} ms")
        else:
            ids_echoué.append(f"Le ping vers {a} a échoué." "\n")
            # messagebox.showinfo("ping test!", f"Le ping vers {a} a échoué.")
            # print(f"Le ping vers {a} a échoué.")
    message_réussi = "\n".join(ids_reussi)
    messagebox.showinfo("Test réussi!", message_réussi)
    message_échoué = "\n".join(ids_echoué)
    messagebox.showinfo("Test échoué!", message_échoué)

import time
from time import sleep

def redemarrer():
	selected = my_tree.focus()
	# Grab record values
	values = my_tree.item(selected, 'values')
	ip_add=values[10]
	print(ip_add)
	# Ouvrir Bureau à distance
	pyautogui.hotkey('win', 'r')
	pyautogui.typewrite('mstsc')
	pyautogui.press('enter')
	time.sleep(2)
		# Entrer l'adresse IP
	pyautogui.typewrite(ip_add)
	pyautogui.press('enter')
	time.sleep(5)

	sleep(1)
	x,y = pyautogui.locateCenterOnScreen("autre_choix.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.click()

	sleep(1)
	x,y = pyautogui.locateCenterOnScreen("autre_compte.PNG",confidence=0.9)
	pyautogui.moveTo(x, y, 1)
	pyautogui.click()

	time.sleep(2)
		# Entrer le nom d'utilisateur et le mot de passe
	utilisateur = "administrator"
	pyautogui.typewrite(utilisateur)
	pyautogui.press('tab')
	mot_de_passe = "Wind0ws10"
	pyautogui.typewrite(mot_de_passe)
	pyautogui.press('enter')
	time.sleep(2)
		# Envoyer la combinaison de touches Flèche gauche + Entrée pour effectuer une action dans UltraVNC
	pyautogui.hotkey('left', 'enter')

	sleep(10)
	# Recherche du choix
	choice = pyautogui.locateCenterOnScreen("bureau.PNG", confidence=0.9)
	# Si le choix est trouvé, effectuer l'action
	if choice is not None:
		x, y = choice
		pyautogui.moveTo(x, y, duration=1)
		pyautogui.click()
		pyautogui.click()
	else:
		# Action "skip" lorsque le choix n'est pas trouvé
		print("Le choix n'a pas été trouvé. Skip...")

	time.sleep(6)
	# Recherche du premier choix
	first_choice = pyautogui.locateCenterOnScreen("oui_but.PNG", confidence=0.7)

	# Si le premier choix est trouvé, le sélectionner
	if first_choice is not None:
		x, y = first_choice
		pyautogui.moveTo(x, y, duration=1)
		pyautogui.click()
	else:
		# Recherche du deuxième choix
		second_choice = pyautogui.locateCenterOnScreen("oui_but2.PNG", confidence=0.7)
		
		# Si le deuxième choix est trouvé, le sélectionner
		if second_choice is not None:
			x, y = second_choice
			pyautogui.moveTo(x, y, duration=1)
			pyautogui.click()
		else:
			# Action "skip" lorsque aucun des choix n'est trouvé
			print("Aucun des choix n'a été trouvé. Skip...")

	time.sleep(10)
	    # Redémarrer la caisse
	pyautogui.hotkey('win', 'r')
	sleep(2)
	pyautogui.typewrite('shutdown')
	pyautogui.press('capslock')
	pyautogui.typewrite(' /r /t 0')
	pyautogui.press('capslock')

	sleep(1)
	pyautogui.press('enter')
	time.sleep(2)    

def connect_bureau():
	selected = my_tree.focus()
	# Grab record values
	values = my_tree.item(selected, 'values')
	ip_add=values[10]
	print(ip_add)
	# Ouvrir Bureau à distance
	pyautogui.hotkey('win', 'r')
	pyautogui.typewrite('mstsc')
	pyautogui.press('enter')
	time.sleep(2)
		# Entrer l'adresse IP
	pyautogui.typewrite(ip_add)
	pyautogui.press('enter')
	time.sleep(5)

	sleep(1)
	x,y = pyautogui.locateCenterOnScreen("autre_choix.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.click()

	sleep(1)
	x,y = pyautogui.locateCenterOnScreen("autre_compte.PNG",confidence=0.9)
	pyautogui.moveTo(x, y, 1)
	pyautogui.click()

	time.sleep(2)
		# Entrer le nom d'utilisateur et le mot de passe
	utilisateur = "administrator"
	pyautogui.typewrite(utilisateur)
	pyautogui.press('tab')
	mot_de_passe = "Wind0ws10"
	pyautogui.typewrite(mot_de_passe)
	pyautogui.press('enter')
	time.sleep(2)
		# Envoyer la combinaison de touches Flèche gauche + Entrée pour effectuer une action dans UltraVNC
	pyautogui.hotkey('left', 'enter')

	sleep(10)
	# Recherche du choix
	choice = pyautogui.locateCenterOnScreen("bureau.PNG", confidence=0.9)
	# Si le choix est trouvé, effectuer l'action
	if choice is not None:
		x, y = choice
		pyautogui.moveTo(x, y, duration=1)
		pyautogui.click()
		pyautogui.click()
	else:
		# Action "skip" lorsque le choix n'est pas trouvé
		print("Le choix n'a pas été trouvé. Skip...")

	time.sleep(6)
	# Recherche du premier choix
	first_choice = pyautogui.locateCenterOnScreen("oui_but.PNG", confidence=0.7)

	# Si le premier choix est trouvé, le sélectionner
	if first_choice is not None:
		x, y = first_choice
		pyautogui.moveTo(x, y, duration=1)
		pyautogui.click()
	else:
		# Recherche du deuxième choix
		second_choice = pyautogui.locateCenterOnScreen("oui_but2.PNG", confidence=0.7)
		
		# Si le deuxième choix est trouvé, le sélectionner
		if second_choice is not None:
			x, y = second_choice
			pyautogui.moveTo(x, y, duration=1)
			pyautogui.click()
		else:
			# Action "skip" lorsque aucun des choix n'est trouvé
			print("Aucun des choix n'a été trouvé. Skip...")

import clipboard

def DNS_comparison():
	selected = my_tree.focus()
	# Grab record values
	values = my_tree.item(selected, 'values')
	ip_add=values[10]
	print(ip_add)
	# Ouvrir Bureau à distance
	pyautogui.hotkey('win', 'r')
	pyautogui.typewrite('mstsc')
	pyautogui.press('enter')
	time.sleep(2)
		# Entrer l'adresse IP
	pyautogui.typewrite(ip_add)
	pyautogui.press('enter')
	time.sleep(5)

	sleep(1)
	x,y = pyautogui.locateCenterOnScreen("autre_choix.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.click()

	sleep(1)
	x,y = pyautogui.locateCenterOnScreen("autre_compte.PNG",confidence=0.9)
	pyautogui.moveTo(x, y, 1)
	pyautogui.click()

	time.sleep(2)
		# Entrer le nom d'utilisateur et le mot de passe
	utilisateur = "administrator"
	pyautogui.typewrite(utilisateur)
	pyautogui.press('tab')
	mot_de_passe = "Wind0ws10"
	pyautogui.typewrite(mot_de_passe)
	pyautogui.press('enter')
	time.sleep(2)
		# Envoyer la combinaison de touches Flèche gauche + Entrée pour effectuer une action dans UltraVNC
	pyautogui.hotkey('left', 'enter')

	sleep(10)
	# Recherche du choix
	choice = pyautogui.locateCenterOnScreen("bureau.PNG", confidence=0.9)
	# Si le choix est trouvé, effectuer l'action
	if choice is not None:
		x, y = choice
		pyautogui.moveTo(x, y, duration=1)
		pyautogui.click()
		pyautogui.click()
	else:
		# Action "skip" lorsque le choix n'est pas trouvé
		print("Le choix n'a pas été trouvé. Skip...")

	time.sleep(6)
	# Recherche du premier choix
	first_choice = pyautogui.locateCenterOnScreen("oui_but.PNG", confidence=0.7)

	# Si le premier choix est trouvé, le sélectionner
	if first_choice is not None:
		x, y = first_choice
		pyautogui.moveTo(x, y, duration=1)
		pyautogui.click()
	else:
		# Recherche du deuxième choix
		second_choice = pyautogui.locateCenterOnScreen("oui_but2.PNG", confidence=0.7)
		
		# Si le deuxième choix est trouvé, le sélectionner
		if second_choice is not None:
			x, y = second_choice
			pyautogui.moveTo(x, y, duration=1)
			pyautogui.click()
		else:
			# Action "skip" lorsque aucun des choix n'est trouvé
			print("Aucun des choix n'a été trouvé. Skip...")

	# Attendre que la connexion soit établie et les paramètres DNS s'affichent
	time.sleep(10)
	# Récupérer les paramètres DNS
	pyautogui.hotkey('win', 'r')
	pyautogui.typewrite('cmd')
	pyautogui.press('enter')
	time.sleep(2)
	pyautogui.typewrite('ipconfig')
	pyautogui.press('capslock')
	pyautogui.typewrite('/all')
	pyautogui.press('capslock')

	sleep(3)
	pyautogui.press('enter')
	time.sleep(3)

	# Copier la sortie de la commande ipconfig
	pyautogui.hotkey('ctrl', 'a')
	pyautogui.hotkey('ctrl', 'c')
	sleep(3)
	# Fermer la fenêtre de commande
	pyautogui.hotkey('alt', 'f4')

	# Comparer les paramètres DNS
	msg_box=[]
	dns_output = clipboard.paste()
	dns_lines = dns_output.split('\n')
	for line in dns_lines:
		if "Serveurs DNS" in line:
			dns_servers = line.split(':')[1].strip()
			if dns_servers == "Serveurs DNS attendus ": #Expected DNS Servers
				# print("Les paramètres DNS sont corrects.")
				msg_box.append("Les paramètres DNS sont corrects.")

			else:
				# print("Les paramètres DNS ne correspondent pas.")
				msg_box.append("Les paramètres DNS ne correspondent pas.")

	msg_box2 = []
	dns_servers=[]
	found_dns_servers = False
	next_lines_count = 3
	lines = dns_output.split('\n')
	print(lines)
	try:
		for line in lines:
			if 'Serveurs DNS' in line:
				found_dns_servers = True
				dns_servers.extend(line.split(':')[1].strip().split())

			elif found_dns_servers and next_lines_count > 0:
				dns_servers.append(line.strip())
				next_lines_count -= 1
				dns_servers_line = line.split(':')
				if len(dns_servers_line) > 1:
					servers = dns_servers_line[1].strip().split(' ')
					dns_servers.extend(servers)
					print(dns_servers)
	except FileNotFoundError:
		# print("Impossible de récupérer les paramètres DNS.")
		msg_box2.append("Impossible de récupérer les paramètres DNS.")



	if len(dns_servers) < 2:
		# print("Il n'y a pas suffisamment de serveurs DNS pour comparer.")
		msg_box2.append("Il n'y a pas suffisamment de serveurs DNS pour comparer.")

	# Vérifie si tous les serveurs DNS sont identiques
	if all(server == dns_servers[0] for server in dns_servers):
		# print("Tous les serveurs DNS sont identiques :", dns_servers[0])
		msg_box2.append(f"Tous les serveurs DNS sont identiques :{dns_servers[0]}""\n")

	else:
		print("Les serveurs DNS sont différents :", dns_servers)
		msg_box2.append(f"Les serveurs DNS sont différents :{dns_servers}""\n")

	message_réussi = "\n".join(msg_box)
	messagebox.showinfo("DNS Result", message_réussi)
	message_échoué = "\n".join(msg_box2)
	messagebox.showinfo("DNS Result", message_échoué)
	# Fermer la session Bureau à distance
	# pyautogui.hotkey('alt', 'f4')
	# pyautogui.hotkey('alt', 'f4')s


def system_events():
	selected = my_tree.focus()
	# Grab record values
	values = my_tree.item(selected, 'values')
	ip_add=values[10]
	# Ouvrir Bureau à distance
	pyautogui.hotkey('win', 'r')
	pyautogui.typewrite('mstsc')
	pyautogui.press('enter')
	time.sleep(2)
		# Entrer l'adresse IP
	pyautogui.typewrite(ip_add)
	pyautogui.press('enter')
	time.sleep(5)

	sleep(1)
	x,y = pyautogui.locateCenterOnScreen("autre_choix.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.click()

	sleep(1)
	x,y = pyautogui.locateCenterOnScreen("autre_compte.PNG",confidence=0.9)
	pyautogui.moveTo(x, y, 1)
	pyautogui.click()

	time.sleep(2)
		# Entrer le nom d'utilisateur et le mot de passe
	utilisateur = "administrator"
	pyautogui.typewrite(utilisateur)
	pyautogui.press('tab')
	mot_de_passe = "Wind0ws10"
	pyautogui.typewrite(mot_de_passe)
	pyautogui.press('enter')
	time.sleep(2)
		# Envoyer la combinaison de touches Flèche gauche + Entrée pour effectuer une action dans UltraVNC
	pyautogui.hotkey('left', 'enter')

	sleep(10)
	# Recherche du choix
	choice = pyautogui.locateCenterOnScreen("bureau.PNG", confidence=0.9)
	# Si le choix est trouvé, effectuer l'action
	if choice is not None:
		x, y = choice
		pyautogui.moveTo(x, y, duration=1)
		pyautogui.click()
		pyautogui.click()
	else:
		# Action "skip" lorsque le choix n'est pas trouvé
		print("Le choix n'a pas été trouvé. Skip...")

	time.sleep(6)
	# Recherche du premier choix
	first_choice = pyautogui.locateCenterOnScreen("oui_but.PNG", confidence=0.7)

	# Si le premier choix est trouvé, le sélectionner
	if first_choice is not None:
		x, y = first_choice
		pyautogui.moveTo(x, y, duration=1)
		pyautogui.click()
	else:
		# Recherche du deuxième choix
		second_choice = pyautogui.locateCenterOnScreen("oui_but2.PNG", confidence=0.7)
		
		# Si le deuxième choix est trouvé, le sélectionner
		if second_choice is not None:
			x, y = second_choice
			pyautogui.moveTo(x, y, duration=1)
			pyautogui.click()
		else:
			# Action "skip" lorsque aucun des choix n'est trouvé
			print("Aucun des choix n'a été trouvé. Skip...")
	
	sleep(30)
	pyautogui.hotkey('win', 'r')
	pyautogui.typewrite('cmd')
	pyautogui.press('enter')
	sleep(2)
	deb_anomalie = '2023-05-23T10:00:00'
	fin_anomalie = '2023-05-23T10:10:00'
	command = f'wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>=\'{deb_anomalie}\'] and TimeCreated[@SystemTime<=\'{fin_anomalie}\']]]" > "Documents/output.xml"'
	pyperclip.copy(command)
	pyautogui.hotkey('ctrl', 'v')
	pyautogui.press('enter')
	# Attendre que la connexion soit établie et les paramètres DNS s'affichent
	
	sleep(5)
	pyautogui.hotkey('win', 'r')
	time.sleep(1)
	pyautogui.typewrite('Documents')
	time.sleep(1)
	pyautogui.press('enter')
	time.sleep(1)

	# Sélectionner le fichier à couper
	sleep(5)
	x,y = pyautogui.locateCenterOnScreen("outputimg.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.click()
	time.sleep(1)

	# Couper le fichier
	pyautogui.hotkey('ctrl', 'x')
	pyautogui.hotkey('ctrl', 'x')
	time.sleep(1)

	sleep(1)
	x,y = pyautogui.locateCenterOnScreen("reduire.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.click()

	sleep(2)
	cmd ='Documents\Sujet PFE'
	# Ouvrir le dossier de destination
	pyautogui.hotkey('win', 'r')
	time.sleep(1)
	pyperclip.copy(cmd)
	pyautogui.hotkey('ctrl', 'v')
	pyautogui.press('enter')

	# sleep(2)
	# x,y = pyautogui.locateCenterOnScreen("doc3.PNG",confidence=0.8)
	# pyautogui.moveTo(x, y, 1)
	# pyautogui.click()

	# Coller le fichier
	sleep(1)
	pyautogui.hotkey('ctrl', 'v')
	time.sleep(1)

	sleep(1)
	x,y = pyautogui.locateCenterOnScreen("bureau.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.click()

	sleep(1)
	x,y = pyautogui.locateCenterOnScreen("sortir2.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.click()

	sleep(1)
	x,y = pyautogui.locateCenterOnScreen("ok.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.click()

	sleep(5)
	# Exemple d'utilisation
	nom_fichier = 'output.xml'
	motP = '<Events>'
	motD = '</Events>'
    # Lecture du fichier XML
	with open(nom_fichier, 'r') as fichier:
		lignes = fichier.readlines()
	# Ajout du mot à la première et à la dernière ligne
	lignes[0] = motP + '' + lignes[0].strip() + '\n'
	lignes[-1] = lignes[-1].strip() + ' ' + motD + '\n'
    # Écriture du fichier modifié
	with open(nom_fichier, 'w') as fichier:
		fichier.writelines(lignes)
	
	evenements =[]
	with open(nom_fichier, 'r') as f:
		data = f.read()

	# Parser le XML avec BeautifulSoup
	soup = BeautifulSoup(data, 'xml')
	events = soup.find_all('Event')
	# print(events)
	for event in events:
		try:
			if event is not None:
				system = event.find('System')
				provider_name = system.find('Provider')['Name']
				event_id = system.find('EventID').text
				time_created = system.find('TimeCreated')['SystemTime']
				event_record_id = system.find('EventRecordID').text
				data_typ = event.find('Data', {'Name': 'Type'})
				if data_typ is not None:
					data_type =data_typ.text
				else:
					print('Skip ...')
				error_stat = event.find('Data', {'Name': 'ErrorState'})
				if error_stat is not None:
					error_state=error_stat.text
				else:
					print('Skip ...')
			else:
				print("Le choix n'a pas été trouvé. Skip...")

			evenements.append(f"Provider Name : {provider_name} ""\n")
			# print('Provider Name:', provider_name)
			evenements.append(f"Event ID : {event_id} ""\n")
			# print('Event ID:', event_id)
			evenements.append(f"Time Created : {time_created} ""\n")			
			# print('Time Created:', time_created)
			evenements.append(f"Event Record ID: {event_record_id} ""\n")
			# print('Event Record ID:', event_record_id)
			evenements.append(f"Data Type: {data_type} ""\n")
			# print('Data Type:', data_type)
			evenements.append(f"Error State: {error_state} ""\n")
			# print('Error State:', error_state)
			evenements.append(f"----- ""\n")
			print('---')

		except KeyboardInterrupt:
			print("\nEnregistrement des coordonnées terminé.")
		message_evenements = "\n".join(evenements)
		messagebox.showinfo("Les événements systeme windows!", message_evenements)	





def fichier_param():
	selected = my_tree.focus()
	# Grab record values
	values = my_tree.item(selected, 'values')
	ip_add=values[10]
	chemin_vers_ultravnc = "C:/Users/safouane.elharrak/Documents/ULTRAVNC/ULTRAVNC/vncviewer.exe"
	subprocess.Popen([chemin_vers_ultravnc, ip_add])
	# Attendez un certain temps pour permettre la fenêtre UltraVNC de s'afficher
	sleep(1)
	# Nom d'utilisateur pour la connexion à distance
	utilisateur = "administrator"
	# Mot de passe pour la connexion à distance       
	mot_de_passe = "Wind0ws10"
	time.sleep(2)
	# Entrer le nom d'utilisateur et le mot de passe
	pyautogui.typewrite(utilisateur)
	pyautogui.press('tab')
	pyautogui.typewrite(mot_de_passe)
	pyautogui.press('enter')

	sleep(5)
	x,y = pyautogui.locateCenterOnScreen("fichier.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.click()

	sleep(2)
	x,y = pyautogui.locateCenterOnScreen("my_doc.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.doubleClick()

	sleep(25)
	x,y = pyautogui.locateCenterOnScreen("disk_C.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.doubleClick()

	sleep(5)
	x,y = pyautogui.locateCenterOnScreen("scot.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.doubleClick()

	sleep(3)
	x,y = pyautogui.locateCenterOnScreen("install.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.doubleClick()

	sleep(3)
	x,y = pyautogui.locateCenterOnScreen("size.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.click()
	sleep(1)
	pyautogui.click()

	sleep(1)
	x,y = pyautogui.locateCenterOnScreen("scoconfig.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.click()

	sleep(2)
	x,y = pyautogui.locateCenterOnScreen("recevoir.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.click()

	sleep(5)
	x,y = pyautogui.locateCenterOnScreen("sortir.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.click()

	sleep(2)
	x,y = pyautogui.locateCenterOnScreen("sortir2.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.click()	
	messagebox.showinfo("Recupérrer!", "tu vas trouver le fichier diag sur votre document!")


def fichier_logs():
	selected = my_tree.focus()
	# Grab record values
	values = my_tree.item(selected, 'values')
	ip_add=values[10]
	chemin_vers_ultravnc = "C:/Users/safouane.elharrak/Documents/ULTRAVNC/ULTRAVNC/vncviewer.exe"
	subprocess.Popen([chemin_vers_ultravnc, ip_add])
	# Attendez un certain temps pour permettre la fenêtre UltraVNC de s'afficher
	sleep(1)
	# Nom d'utilisateur pour la connexion à distance
	utilisateur = "administrator"
	# Mot de passe pour la connexion à distance       
	mot_de_passe = "Wind0ws10"
	time.sleep(2)
	# Entrer le nom d'utilisateur et le mot de passe
	pyautogui.typewrite(utilisateur)
	pyautogui.press('tab')
	pyautogui.typewrite(mot_de_passe)
	pyautogui.press('enter')

	sleep(5)
	x,y = pyautogui.locateCenterOnScreen("fichier.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.click()

	sleep(2)
	x,y = pyautogui.locateCenterOnScreen("my_doc.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.doubleClick()

	sleep(25)
	x,y = pyautogui.locateCenterOnScreen("disk_C.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.doubleClick()

	sleep(5)
	x,y = pyautogui.locateCenterOnScreen("temp.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.doubleClick()

	sleep(3)
	pyautogui.moveTo(1528, 147, 1)   # Coordonnées du champ de saisie pour l'adresse IP ou le nom d'hôte
	pyautogui.click()

	sleep(2)
	x,y = pyautogui.locateCenterOnScreen("FRHY2.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.click()

	sleep(2)
	x,y = pyautogui.locateCenterOnScreen("recevoir.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.click()

	sleep(30)
	x,y = pyautogui.locateCenterOnScreen("sortir.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.click()

	sleep(2)
	x,y = pyautogui.locateCenterOnScreen("sortir2.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.click()
	messagebox.showinfo("Recupérrer!", "tu vas trouver le fichier log sur votre document!")

def version_qvs():
	selected = my_tree.focus()
	# Grab record values
	values = my_tree.item(selected, 'values')
	ip_add=values[10]
	chemin_vers_ultravnc = "C:/Users/safouane.elharrak/Documents/ULTRAVNC/ULTRAVNC/vncviewer.exe"
	subprocess.Popen([chemin_vers_ultravnc, ip_add])
	# Attendez un certain temps pour permettre la fenêtre UltraVNC de s'afficher
	sleep(1)
	# Nom d'utilisateur pour la connexion à distance
	utilisateur = "administrator"
	# Mot de passe pour la connexion à distance       
	mot_de_passe = "Wind0ws10"
	time.sleep(2)
	# Entrer le nom d'utilisateur et le mot de passe
	pyautogui.typewrite(utilisateur)
	pyautogui.press('tab')
	pyautogui.typewrite(mot_de_passe)
	pyautogui.press('enter')

	sleep(5)
	x,y = pyautogui.locateCenterOnScreen("fichier.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.click()

	sleep(2)
	x,y = pyautogui.locateCenterOnScreen("my_doc.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.doubleClick()

	sleep(25)
	x,y = pyautogui.locateCenterOnScreen("disk_C.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.doubleClick()

	sleep(3)
	x,y = pyautogui.locateCenterOnScreen("install.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.doubleClick()

	time.sleep(2)
	msg_v1=[]
	msg_v2=[]
	msg_v3=[]

	# Recherche du premier choix
	qvs_v1 = pyautogui.locateCenterOnScreen("qvsv1.PNG", confidence=0.7)
	# Si le premier choix est trouvé, le sélectionner
	if qvs_v1 is not None:
		x, y = qvs_v1
		pyautogui.moveTo(x, y, duration=1)
		# pyautogui.click()
		msg_v1.append("QVS version est : 8.10.11.0")
	else:
		# Recherche du deuxième choix
		qvs_v2 = pyautogui.locateCenterOnScreen("qvsv2.PNG", confidence=0.7)
		# Si le deuxième choix est trouvé, le sélectionner
		if qvs_v2 is not None:
			x, y = qvs_v2
			pyautogui.moveTo(x, y, duration=1)
			# pyautogui.click()
			msg_v2.append("QVS version est : 7.7.12.0")

		else:
			# Action "skip" lorsque aucun des choix n'est trouvé
			msg_v3.append("Probleme de trouvé la version")

	sleep(2)
	x,y = pyautogui.locateCenterOnScreen("sortir.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.click()

	sleep(2)
	x,y = pyautogui.locateCenterOnScreen("sortir2.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.click()
	message_evenements = msg_v1 + msg_v2 + msg_v3
	messagebox.showinfo('QVS',message_evenements)	


def version_fastlane():
	selected = my_tree.focus()
	# Grab record values
	values = my_tree.item(selected, 'values')
	ip_add=values[10]
	chemin_vers_ultravnc = "C:/Users/safouane.elharrak/Documents/ULTRAVNC/ULTRAVNC/vncviewer.exe"
	subprocess.Popen([chemin_vers_ultravnc, ip_add])
	# Attendez un certain temps pour permettre la fenêtre UltraVNC de s'afficher
	sleep(1)
	# Nom d'utilisateur pour la connexion à distance
	utilisateur = "administrator"
	# Mot de passe pour la connexion à distance       
	mot_de_passe = "Wind0ws10"
	time.sleep(2)
	# Entrer le nom d'utilisateur et le mot de passe
	pyautogui.typewrite(utilisateur)
	pyautogui.press('tab')
	pyautogui.typewrite(mot_de_passe)
	pyautogui.press('enter')

	sleep(5)
	x,y = pyautogui.locateCenterOnScreen("fichier.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.click()

	sleep(2)
	x,y = pyautogui.locateCenterOnScreen("my_doc.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.doubleClick()

	sleep(25)
	x,y = pyautogui.locateCenterOnScreen("disk_C.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.doubleClick()

	sleep(2)
	x,y = pyautogui.locateCenterOnScreen("install.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.doubleClick()

	sleep(3)
	# Coordonnées du modifié le
	pyautogui.moveTo(1528, 147, 1)
	pyautogui.click()

	sleep(2)
	x,y = pyautogui.locateCenterOnScreen("grandir.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.click()
	msg_v1 =[]
	msg_v2 =[]
	msg_v3 =[]
	msg_v4 =[]

	time.sleep(2)
	# Recherche du premier choix
	fastlane_v1 = pyautogui.locateCenterOnScreen("fastlane_v1.PNG", confidence=0.7)
	# Si le premier choix est trouvé, le sélectionner
	if fastlane_v1 is not None:
		x, y = fastlane_v1
		pyautogui.moveTo(x, y, duration=1)
		# pyautogui.click()
		msg_v1.append("la version du fastlane est : 2.2.0.167.2")
	else:
		# Recherche du deuxième choix
		fastlane_v2 = pyautogui.locateCenterOnScreen("fastlane_v2.PNG", confidence=0.7)
		# Si le deuxième choix est trouvé, le sélectionner
		if fastlane_v2 is not None:
			x, y = fastlane_v2
			pyautogui.moveTo(x, y, duration=1)
			# pyautogui.click()
			msg_v2.append("la version du fastlane est : 2.2.0.166.7")

		fastlane_v3 = pyautogui.locateCenterOnScreen("fastlane_v3.PNG", confidence=0.7)
		if fastlane_v3 is not None:
			x, y = fastlane_v3
			pyautogui.moveTo(x, y, duration=1)
			# pyautogui.click()
			msg_v3.append("la version du fastlane est : 2.2.0.166.3")

		else:
			# Action "skip" lorsque aucun des choix n'est trouvé
			msg_v4.append("Probleme de trouvé la version")

	sleep(2)
	x,y = pyautogui.locateCenterOnScreen("sortir3.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.click()

	sleep(2)
	x,y = pyautogui.locateCenterOnScreen("sortir2.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.click()
	message_evenements = msg_v1 + msg_v2 + msg_v3 + msg_v4
	messagebox.showinfo('QVS',message_evenements)	


import mysql.connector

def create_table_again():
    # Create a database connection
    conn = mysql.connector.connect(host='localhost',
                                         database='sco_db',
                                         user='root',
                                         password='')

    # Create a cursor instance
    c = conn.cursor()

    # Create table if it doesn't exist
    c.execute("""CREATE TABLE if not exists magasin(
    ID int,
	Numéro int,
	Nom varchar(22),
	format varchar(5),
	Code_CARINE int,
	Profil varchar(7),
	Nom_poste varchar(14),
	Terminal int,
	Opérateur int,
	Pwd int,
	IP_poste_varchar(13),
	Masque varchar varchar(13),
	Passerelle varchar(13),
	Nom_Master varchar(14),
	IP_Master varchar(13),
	IP_Glory varchar(13),
	Balance varchar(3),
	Type_SCA varchar(8),
	Cash varchar(9),
	EAS varchar(3)
	)""")

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()

# Add Buttons
button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

update_button = Button(button_frame, text="Update Record", command=update_record)
update_button.grid(row=0, column=0, padx=10, pady=10)

add_button = Button(button_frame, text="Add Record", command=add_record)
add_button.grid(row=0, column=1, padx=10, pady=10)

remove_all_button = Button(button_frame, text="Remove All Records", command=remove_all)
remove_all_button.grid(row=0, column=2, padx=10, pady=10)

remove_one_button = Button(button_frame, text="Remove One Selected", command=remove_one)
remove_one_button.grid(row=0, column=3, padx=10, pady=10)

remove_many_button = Button(button_frame, text="Remove Many Selected", command=remove_many)
remove_many_button.grid(row=0, column=4, padx=10, pady=10)

move_up_button = Button(button_frame, text="Move Up", command=up)
move_up_button.grid(row=0, column=5, padx=10, pady=10)

move_down_button = Button(button_frame, text="Move Down", command=down)
move_down_button.grid(row=0, column=6, padx=10, pady=10)

select_record_button = Button(button_frame, text="Clear Entry Boxes", command=clear_entries)
select_record_button.grid(row=0, column=7, padx=10, pady=10)


ultravnc_button = Button(button_frame, text="ULTRAVNC", command=connect_ultravnc)
ultravnc_button.grid(row=1, column=0, padx=10, pady=10)

ping_button = Button(button_frame, text="PING", command=test_ping)
ping_button.grid(row=1, column=1, padx=10, pady=10)

redemarrer_button = Button(button_frame, text="REDEMARRER", command=redemarrer)
redemarrer_button.grid(row=1, column=2, padx=10, pady=10)

bureau_button = Button(button_frame, text="Bureau à distance", command=connect_bureau)
bureau_button.grid(row=1, column=2, padx=10, pady=10)

dns_button = Button(button_frame, text="Serveurs DNS", command=DNS_comparison)
dns_button.grid(row=1, column=3, padx=10, pady=10)

fichLog_button = Button(button_frame, text="Fichier Log", command=fichier_logs)
fichLog_button.grid(row=1, column=4, padx=10, pady=10)

fichConfig_button = Button(button_frame, text="Fichier Config", command=fichier_param)
fichConfig_button.grid(row=1, column=5, padx=10, pady=10)

qvs_button = Button(button_frame, text="QVS Version", command=version_qvs)
qvs_button.grid(row=1, column=6, padx=10, pady=10)

fastlane_button = Button(button_frame, text="Fastlane Version", command=version_fastlane)
fastlane_button.grid(row=1, column=7, padx=10, pady=10)

system_button = Button(button_frame, text="System Events", command=system_events)
system_button.grid(row=1, column=8, padx=10, pady=10)

# Bind the treeview
my_tree.bind("<ButtonRelease-1>", select_record)

# Run to pull data from database on start
query_database()

root.mainloop()