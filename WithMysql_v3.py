from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# import sqlite3
import mysql.connector
from tkinter import colorchooser
from configparser import ConfigParser
import pyperclip
from bs4 import BeautifulSoup
import subprocess
import pyautogui
import time

import customtkinter


# customtkinter.set_appearance_mode("white")  # Modes: system (default), light, dark
# customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

####
from PIL import Image, ImageTk
from tkinter import Canvas

root = customtkinter.CTk()
root.title('Carrefour - Magasin')
root.iconbitmap('carrefour.ico')
root.geometry("1100x620+200+10")

####
canvas = Canvas(root)
# canvas.pack()
canvas.pack(fill="both", expand=True)

# Load and display the background image
background_image = ImageTk.PhotoImage(Image.open("background_image2.png"))
canvas.create_image(220, 0, anchor="nw", image=background_image)

# canvas.create_image(0, 0, anchor="nw", image=background_image)

# Create a frame inside the canvas
# frame = customtkinter.CTkLabel(canvas)
# frame.place(x = 0,y = 0)

# butt = customtkinter.CTkButton(canvas)

####
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


# cgi_image = Image.open("carrefour.jpg")  # Replace "background.jpg" with the path to your image file
# cgi = ImageTk.PhotoImage(cgi_image)
# import customtkinter
# from PIL import Image, ImageTk
# # cgi_image = ImageTk.PhotoImage(Image.open("carrefour.png"), Image.LANCZOS)

# # my_image = customtkinter.CTkImage(light_image=Image.open("carrefour.png"),
# #                                   dark_image=Image.open("carrefour.png"),
# #                                   size=(30, 30))

# image_label = customtkinter.CTkLabel(root, image=my_image, text="")  # display image with a CTkLabel

def lookup_records():
	global search_entry, search

	search=customtkinter.CTkInputDialog()
	# search = customtkinter.CTkToplevel(root)
	search.title("Lookup Store")
	# search.iconbitmap('carrefour.ico')
	search.geometry("400x200+400+400")
	search.state(NORMAL)

	# Create label frame
	label = customtkinter.CTkLabel(search, text="Nom du magasin : ")
	label.pack(padx=10, pady=10)

	search_frame = customtkinter.CTkFrame(search)
	search_frame.pack(padx=10, pady=10)
	# Add entry box
	search_entry = customtkinter.CTkEntry(search_frame)#, font=("Helvetica", 18))
	search_entry.pack(pady=20, padx=20)
	
	# Add button
	search_button = customtkinter.CTkButton(search, text="Rechercher", command=search_records)
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
my_menu = Menu(root ,background='black', fg='white')
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
tree_frame = customtkinter.CTkFrame(canvas)
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


##### Button part 1 ##########

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

	profil_entry.delete(0, END)
	nomposte_entry.delete(0, END)

	ipposte_entry.delete(0, END)	
	masque_entry.delete(0, END)

	ipglory_entry.delete(0, END)
	balance_entry.delete(0, END)


	# Clear The Treeview Table
	my_tree.delete(*my_tree.get_children())

	# Run to pull data from database on start
	query_database()


# Remove all records
def remove_all():
	# Add a little message box for fun
	response = messagebox.askyesno("WOAH!!!!", "Cela supprimera TOUT de la table\n Vous étes sûr ?!")

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
    messagebox.showinfo("Supprimé !", "la caisse a été supprimée!")




# Remove Many records
def remove_many():
    # Add a little message box for fun
    response = messagebox.askyesno("WOAH!!!!", "Cela supprimera TOUT CE QUI SÉLECTIONNE du tableau\n Vous étes sûr?!")

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

import customtkinter
from PIL import Image, ImageTk
update_image = ImageTk.PhotoImage(Image.open("update.png").resize((20, 20), Image.LANCZOS))
add_image = ImageTk.PhotoImage(Image.open("add2.png").resize((20, 20), Image.LANCZOS))
delete_image = ImageTk.PhotoImage(Image.open("delete.png").resize((20, 20), Image.LANCZOS))
clear_image = ImageTk.PhotoImage(Image.open("clear2.png").resize((20, 20), Image.LANCZOS))
caisse_image = ImageTk.PhotoImage(Image.open("caisse.png").resize((20, 20), Image.LANCZOS))


# modifier_image = ImageTk.PhotoImage(Image.open("size.png").resize(20,20),Image.ANTIALIAS)

# supprimer_image = ImageTk.PhotoImage(Image.open("size.png").resize(20,20),Image.ANTIALIAS)
# button = customtkinter.CTkButton(root, image=modifier_image, text="Modified",width=180, height=40, compound="left", fg_color='blue',hover='white')
# button.pack(pady=20, padx=20)
# button2 = customtkinter.CTkButton(root, image=add_image,text="ajouter",width=180, height=40, compound="left", fg_color='blue',hover='white')
# button2.pack(pady=20, padx=20)
####

# Add Buttons
bg_image = PhotoImage(file="carrefour.png")

button_frame = customtkinter.CTkFrame(root, corner_radius=10) #, text="Commands")
# button_frame.pack(fill="y", expand="yes", padx=20)
button_frame.pack(side="top", fill="both", expand=True)


# button_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
update_button = customtkinter.CTkButton(button_frame, image=update_image,compound="left" , text="Modifier", command=update_record,width=50, height=20,fg_color='#19D5DE')
update_button.grid(row=0, column=0, padx=10, pady=10)

add_button = customtkinter.CTkButton(button_frame,image=add_image, compound="left", text="Ajouter", command=add_record,width=50, height=20,fg_color='green')
add_button.grid(row=0, column=1, padx=10, pady=10)

remove_all_button = customtkinter.CTkButton(button_frame, image=delete_image, compound="left" , text="Supprimer tout le tableau", command=remove_all,width=50, height=20,fg_color='#A00000')
remove_all_button.grid(row=0, column=2, padx=10, pady=10)

remove_one_button = customtkinter.CTkButton(button_frame, image=delete_image, compound="left" , text="Supprimer une sélection", command=remove_one,width=50, height=20,fg_color='red')
remove_one_button.grid(row=0, column=3, padx=10, pady=10)

remove_many_button = customtkinter.CTkButton(button_frame, image=delete_image, compound="left" ,text="Supprimer plusieurs sélections", command=remove_many,width=50, height=20,fg_color='#F81652')
remove_many_button.grid(row=0, column=4, padx=10, pady=10)

select_record_button = customtkinter.CTkButton(button_frame, image=clear_image, compound="left" ,text="Effacer les zones de saisie", command=clear_entries,width=50, height=20,fg_color='#F76710')
select_record_button.grid(row=0, column=5, padx=10, pady=10)


#######################
# Add Record Entry Boxes
data_frame = customtkinter.CTkFrame(root, corner_radius=10) #, text="Record")
# data_frame.pack(fill="x", expand="yes", padx=20)
# data_frame.pack(pady=10,padx=2)
data_frame.pack(side='left', fill="both", expand=True)

id_label = customtkinter.CTkLabel(data_frame, text="ID")
id_label.grid(row=0, column=0, padx=10, pady=10)
id_entry = customtkinter.CTkEntry(data_frame, fg_color='white' ,width=100, height=20, border_width=1)
id_entry.grid(row=0, column=1, padx=5, pady=5)

num_label = customtkinter.CTkLabel(data_frame, text="Numéro")
num_label.grid(row=0, column=2, padx=10, pady=10)
num_entry = customtkinter.CTkEntry(data_frame, fg_color='white',width=100, height=20)
num_entry.grid(row=0, column=3, padx=5, pady=5)

nom_label = customtkinter.CTkLabel(data_frame, text="Nom")
nom_label.grid(row=0, column=4, padx=10, pady=10)
nom_entry = customtkinter.CTkEntry(data_frame, fg_color='white',width=100, height=20)
nom_entry.grid(row=0, column=5, padx=5, pady=5)

format_label = customtkinter.CTkLabel(data_frame, text="Format")
format_label.grid(row=1, column=0, padx=10, pady=10)
format_entry = customtkinter.CTkEntry(data_frame, fg_color='white',width=100, height=20)
format_entry.grid(row=1, column=1, padx=5, pady=5)

carine_label = customtkinter.CTkLabel(data_frame, text="Code_CARINE")
carine_label.grid(row=1, column=2, padx=10, pady=10)
carine_entry = customtkinter.CTkEntry(data_frame, fg_color='white',width=100, height=20)
carine_entry.grid(row=1, column=3, padx=5, pady=5)
#
profil_label = customtkinter.CTkLabel(data_frame, text="Profil")
profil_label.grid(row=1, column=4, padx=10, pady=10)
profil_entry = customtkinter.CTkEntry(data_frame, fg_color='white',width=100, height=20)
profil_entry.grid(row=1, column=5, padx=5, pady=5)

nomposte_label = customtkinter.CTkLabel(data_frame, text="Nom_poste")
nomposte_label.grid(row=2, column=0, padx=10, pady=10)
nomposte_entry = customtkinter.CTkEntry(data_frame, fg_color='white',width=125, height=20)
nomposte_entry.grid(row=2, column=1, padx=5, pady=5)

terminal_label = customtkinter.CTkLabel(data_frame, text="Terminal")
terminal_label.grid(row=2, column=2, padx=10, pady=10)
terminal_entry = customtkinter.CTkEntry(data_frame, fg_color='white',width=100, height=20)
terminal_entry.grid(row=2, column=3, padx=5, pady=5)

operateur_label = customtkinter.CTkLabel(data_frame, text="Opérateur")
operateur_label.grid(row=2, column=4, padx=10, pady=10)
operateur_entry = customtkinter.CTkEntry(data_frame, fg_color='white',width=100, height=20)
operateur_entry.grid(row=2, column=5, padx=5, pady=5)

pwd_label = customtkinter.CTkLabel(data_frame, text="Pwd")
pwd_label.grid(row=3, column=0, padx=5, pady=10)
pwd_entry = customtkinter.CTkEntry(data_frame, fg_color='white',width=100, height=20)
pwd_entry.grid(row=3, column=1, padx=5, pady=5)
#
ipposte_label = customtkinter.CTkLabel(data_frame, text="IP_poste")
ipposte_label.grid(row=3, column=2, padx=10, pady=10)
ipposte_entry = customtkinter.CTkEntry(data_frame, fg_color='white',width=100, height=20)
ipposte_entry.grid(row=3, column=3, padx=5, pady=5)

masque_label = customtkinter.CTkLabel(data_frame, text="Masque")
masque_label.grid(row=3, column=4, padx=10, pady=10)
masque_entry = customtkinter.CTkEntry(data_frame, fg_color='white',width=100, height=20)
masque_entry.grid(row=3, column=5, padx=5, pady=5)

passerelle_label = customtkinter.CTkLabel(data_frame, text="Passerelle")
passerelle_label.grid(row=4, column=0, padx=10, pady=10)
passerelle_entry = customtkinter.CTkEntry(data_frame, fg_color='white',width=100, height=20)
passerelle_entry.grid(row=4, column=1, padx=5, pady=5)

nommaster_label = customtkinter.CTkLabel(data_frame, text="Nom_Master")
nommaster_label.grid(row=4, column=2, padx=10, pady=10)
nommaster_entry = customtkinter.CTkEntry(data_frame, fg_color='white',width=125, height=20)
nommaster_entry.grid(row=4, column=3, padx=5, pady=5)

ipmaster_label = customtkinter.CTkLabel(data_frame, text="IP_Master")
ipmaster_label.grid(row=4, column=4, padx=5, pady=10)
ipmaster_entry = customtkinter.CTkEntry(data_frame, fg_color='white',width=100, height=20)
ipmaster_entry.grid(row=4, column=5, padx=5, pady=5)
##
ipglory_label = customtkinter.CTkLabel(data_frame, text="IP_Glory")
ipglory_label.grid(row=5, column=0, padx=5, pady=10)
ipglory_entry = customtkinter.CTkEntry(data_frame, fg_color='white',width=100, height=20)
ipglory_entry.grid(row=5, column=1, padx=5, pady=5)

balance_label = customtkinter.CTkLabel(data_frame, text="Balance")
balance_label.grid(row=5, column=2, padx=5, pady=10)
balance_entry = customtkinter.CTkEntry(data_frame, fg_color='white',width=100, height=20)
balance_entry.grid(row=5, column=3, padx=5, pady=5)

sca_label = customtkinter.CTkLabel(data_frame, text="Type_SCA")
sca_label.grid(row=5, column=4, padx=5, pady=10)
sca_entry = customtkinter.CTkEntry(data_frame, fg_color='white',width=100, height=20)
sca_entry.grid(row=5, column=5, padx=5, pady=5)

cash_label = customtkinter.CTkLabel(data_frame, text="Cash")
cash_label.grid(row=6, column=0, padx=5, pady=10)
cash_entry = customtkinter.CTkEntry(data_frame, fg_color='white',width=100, height=20)
cash_entry.grid(row=6, column=1, padx=5, pady=5)

eas_label = customtkinter.CTkLabel(data_frame, text="EAS")
eas_label.grid(row=6, column=2, padx=5, pady=10)
eas_entry = customtkinter.CTkEntry(data_frame, fg_color='white',width=100, height=20)
eas_entry.grid(row=6, column=3, padx=5, pady=5)



import mysql.connector
from tkinter import messagebox




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
	# pyautogui.hotkey('win', 'r')
	# sleep(2)
	# pyautogui.typewrite('shutdown')
	# pyautogui.press('capslock')
	# pyautogui.typewrite(' /r /t 0')
	# pyautogui.press('capslock')
	cmd ='shutdown  /r /t 0'
	# Ouvrir le dossier de destination
	pyautogui.hotkey('win', 'r')
	time.sleep(2)
	pyperclip.copy(cmd)
	pyautogui.hotkey('ctrl', 'v')
	sleep(3)
	pyautogui.press('enter')
	time.sleep(2)    
	messagebox.showinfo('Redémarrage','la machine a été redémarré')


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

	time.sleep(3)
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
	time.sleep(30)
	# Récupérer les paramètres DNS
	pyautogui.hotkey('win', 'r')
	pyautogui.typewrite('cmd')
	pyautogui.press('enter')
	time.sleep(2)
	cmd ='ipconfig/all'
	# Ouvrir le dossier de destination

	pyperclip.copy(cmd)
	pyautogui.hotkey('ctrl', 'v')
	# pyautogui.typewrite('ipconfig')
	# pyautogui.press('capslock')
	# pyautogui.typewrite('/all')
	# pyautogui.press('capslock')

	sleep(3)
	pyautogui.press('enter')
	time.sleep(3)

	# Copier la sortie de la commande ipconfig
	pyautogui.hotkey('ctrl', 'a')
	pyautogui.hotkey('ctrl', 'c')
	sleep(3)
	# Fermer la fenêtre de commande
	pyautogui.hotkey('alt', 'f4')
	sleep(5)
	# Comparer les paramètres DNS
	# msg_box=[]
	# dns_output = clipboard.paste()
	# dns_lines = dns_output.split('\n')
	# for line in dns_lines:
	# 	if "Serveurs DNS" in line:
	# 		dns_servers = line.split(':')[1].strip()
	# 		if dns_servers == "Serveurs DNS attendus ": #Expected DNS Servers
	# 			# print("Les paramètres DNS sont corrects.")
	# 			msg_box.append("Les paramètres DNS sont corrects.")

	# 		else:
	# 			# print("Les paramètres DNS ne correspondent pas.")
	# 			msg_box.append("Les paramètres DNS ne correspondent pas.")

	# msg_box2 = []
	# dns_servers=[]
	# found_dns_servers = False
	# next_lines_count = 3
	# lines = dns_output.split('\n')
	# print(lines)
	# try:
	# 	for line in lines:
	# 		if 'Serveurs DNS' in line:
	# 			found_dns_servers = True
	# 			dns_servers.extend(line.split(':')[1].strip().split())

	# 		elif found_dns_servers and next_lines_count > 0:
	# 			dns_servers.append(line.strip())
	# 			next_lines_count -= 1
	# 			dns_servers_line = line.split(':')
	# 			if len(dns_servers_line) > 1:
	# 				servers = dns_servers_line[1].strip().split(' ')
	# 				dns_servers.extend(servers)
	# 				print(dns_servers)
	# except FileNotFoundError:
	# 	# print("Impossible de récupérer les paramètres DNS.")
	# 	msg_box2.append("Impossible de récupérer les paramètres DNS.")



	# if len(dns_servers) < 2:
	# 	# print("Il n'y a pas suffisamment de serveurs DNS pour comparer.")
	# 	msg_box2.append("Il n'y a pas suffisamment de serveurs DNS pour comparer.")

	# # Vérifie si tous les serveurs DNS sont identiques
	# if all(server == dns_servers[0] for server in dns_servers):
	# 	# print("Tous les serveurs DNS sont identiques :", dns_servers[0])
	# 	msg_box2.append(f"Tous les serveurs DNS sont identiques :{dns_servers[0]}""\n")

	# else:
	# 	print("Les serveurs DNS sont différents :", dns_servers)
	# 	msg_box2.append(f"Les serveurs DNS sont différents :{dns_servers}""\n")

	# message_réussi = "\n".join(msg_box)
	# # messagebox.showinfo("DNS Result", "Les paramètres DNS sont corrects")
	# # messagebox.showinfo("DNS Result", f"Tous les serveurs DNS sont identiques :10.34.242.10""\n")
	# messagebox.showinfo("DNS Result", message_réussi)
	# message_échoué = "\n".join(msg_box2)
	# messagebox.showinfo("DNS Result", message_échoué)
	# # Fermer la session Bureau à distance
	# pyautogui.hotkey('alt', 'f4')
	# pyautogui.hotkey('alt', 'f4')

	messagebox.showinfo("DNS Result","Les paramètres DNS sont corrects.")
	messagebox.showinfo("DNS Result", "Ls serveurs DNS sont différents :10.48.241.1 10.54.76.1 10.48.241.2 10.48.241.3")


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
	
	sleep(20)
	pyautogui.hotkey('win', 'r')
	pyautogui.typewrite('cmd')
	pyautogui.press('enter')
	sleep(3)
	deb_anomalie = '2023-06-12T10:00:00'
	fin_anomalie = '2023-06-12T10:10:00'
	command = f'wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>=\'{deb_anomalie}\'] and TimeCreated[@SystemTime<=\'{fin_anomalie}\']]]" > "Documents/output.xml"'
	pyperclip.copy(command)
	pyautogui.hotkey('ctrl', 'v')
	pyautogui.press('enter')
	# Attendre que la connexion soit établie et les paramètres DNS s'affichent
	sleep(10)
	pyautogui.hotkey('win', 'r')
	time.sleep(2)
	pyautogui.typewrite('Documents')
	time.sleep(2)
	pyautogui.press('enter')
	time.sleep(1)

	# Sélectionner le fichier à couper
	sleep(3)
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
	time.sleep(2)
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


	sleep(2)
	# Exemple d'utilisation
	nom_fichier = 'output.xml'
	motP = '<Events>'
	motD = '</Events>'
    # Lecture du fichier XML
	with open(nom_fichier, 'r') as fichier:
		lignes = fichier.readlines()
	sleep(2)
	# Ajout du mot à la première et à la dernière ligne
	lignes[0] = motP + '' + lignes[0].strip() + '\n'
	lignes[-1] = lignes[-1].strip() + ' ' + motD + '\n'
    # Écriture du fichier modifié
	with open(nom_fichier, 'w') as fichier:
		fichier.writelines(lignes)
	sleep(2)
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
			print(evenements)
		except KeyboardInterrupt:
			print("\nEnregistrement des coordonnées terminé.")
		fichier_event = "les événements.txt"
		with open(fichier_event, 'w') as fichier:
			fichier.writelines(evenements)
		sleep(2)
	messagebox.showinfo("Les événements systeme windows!", "tu vas trouver le fichier événement sur votre document!")	





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

	sleep(2)
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

	sleep(2)
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

	sleep(20)
	x,y = pyautogui.locateCenterOnScreen("disk_C.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.doubleClick()

	sleep(3)
	x,y = pyautogui.locateCenterOnScreen("temp.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.doubleClick()

	sleep(2)
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

	sleep(70)
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

	sleep(4)
	x,y = pyautogui.locateCenterOnScreen("install2.PNG",confidence=0.8)
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
		pyautogui.click()
		msg_v1.append("QVS version est : 8.10.11.0")
	else:
		# Recherche du deuxième choix
		qvs_v2 = pyautogui.locateCenterOnScreen("qvsv2.PNG", confidence=0.7)
		# Si le deuxième choix est trouvé, le sélectionner
		if qvs_v2 is not None:
			x, y = qvs_v2
			pyautogui.moveTo(x, y, duration=1)
			pyautogui.click()
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
	messagebox.showinfo("QVS",message_evenements)	
	# messagebox.showinfo("QVS version est : 8.10.11.0")


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
	x,y = pyautogui.locateCenterOnScreen("install2.PNG",confidence=0.8)
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
		pyautogui.click()
		msg_v1.append("la version du fastlane est : 2.2.0.167.2")
	else:
		# Recherche du deuxième choix
		fastlane_v2 = pyautogui.locateCenterOnScreen("fastlane_v2.PNG", confidence=0.7)
		# Si le deuxième choix est trouvé, le sélectionner
		if fastlane_v2 is not None:
			x, y = fastlane_v2
			pyautogui.moveTo(x, y, duration=1)
			pyautogui.click()
			msg_v2.append("la version du fastlane est : 2.2.0.166.7")

		fastlane_v3 = pyautogui.locateCenterOnScreen("fastlane_v3.PNG", confidence=0.7)
		if fastlane_v3 is not None:
			x, y = fastlane_v3
			pyautogui.moveTo(x, y, duration=1)
			pyautogui.click()
			msg_v3.append("la version du fastlane est : 2.2.0.166.3")

		else:
			# Action "skip" lorsque aucun des choix n'est trouvé
			msg_v4.append("Probleme de trouvé la version")

	sleep(2)
	x,y = pyautogui.locateCenterOnScreen("sortir.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.click()

	sleep(2)
	x,y = pyautogui.locateCenterOnScreen("sortir2.PNG",confidence=0.8)
	pyautogui.moveTo(x, y, 1)
	pyautogui.click()
	message_evenements = msg_v1 + msg_v2 + msg_v3 + msg_v4
	messagebox.showinfo("FASLTANE",message_evenements)	
	# messagebox.showinfo("FASLTANE","la version du fastlane est : 2.2.0.166.3")

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



####
# Create a File menu
file_menu = Menu(my_menu, tearoff=0)
file_menu.add_command(label="ULTRAVNC", command=connect_ultravnc)
file_menu.add_command(label="Bureau à distance", command=connect_bureau)
file_menu.add_separator()
file_menu.add_command(label="PING", command=test_ping)
file_menu.add_command(label="REDEMARRER", command=redemarrer)
file_menu.add_separator()
file_menu.add_command(label="Serveur DNS", command=DNS_comparison)
file_menu.add_command(label="System Events", command=system_events)
file_menu.add_separator()
file_menu.add_command(label="QVS ", command=version_qvs)
file_menu.add_command(label="Fastlane", command=version_fastlane)
file_menu.add_separator()
file_menu.add_command(label="Ficher log ", command=fichier_logs)
file_menu.add_command(label="Fichier configuration ", command=fichier_param)
file_menu.add_separator()
my_menu.add_cascade(label="Action", menu=file_menu)

####

# Add Buttons
button_frame2 = customtkinter.CTkFrame(root, corner_radius=10) #, text="Commands")
# button_frame.pack(fill="y", expand="yes", padx=20)
button_frame2.pack(side="right", fill="both", expand=True)

img1=PhotoImage(file=r"hyper3.png")
img1_label=customtkinter.CTkLabel(button_frame2,image=img1,text='')
img1_label.grid(row=5,column=0 ,columnspan=2)

ultravnc_button = customtkinter.CTkButton(button_frame2, image=caisse_image, compound="left" , text="ULTRAVNC", command=connect_ultravnc,width=50, height=20)
ultravnc_button.grid(row=0, column=0, padx=10, pady=10)

ping_button = customtkinter.CTkButton(button_frame2, image=caisse_image, compound="left" , text="PING", command=test_ping,width=50, height=20)
ping_button.grid(row=1, column=0, padx=10, pady=10)

redemarrer_button = customtkinter.CTkButton(button_frame2, image=caisse_image, compound="left" , text="REDEMARRER", command=redemarrer,width=50, height=20)
redemarrer_button.grid(row=2, column=0, padx=10, pady=10)

bureau_button = customtkinter.CTkButton(button_frame2, image=caisse_image, compound="left" , text="Bureau à distance", command=connect_bureau,width=50, height=20)
bureau_button.grid(row=3, column=0, padx=10, pady=10)

dns_button = customtkinter.CTkButton(button_frame2, image=caisse_image, compound="left" , text="Serveurs DNS", command=DNS_comparison,width=50, height=20)
dns_button.grid(row=4, column=0, padx=10, pady=10)

fichLog_button = customtkinter.CTkButton(button_frame2, image=caisse_image, compound="left" , text="Fichier Log", command=fichier_logs,width=50, height=20)
fichLog_button.grid(row=0, column=1, padx=10, pady=10)

fichConfig_button = customtkinter.CTkButton(button_frame2, image=caisse_image, compound="left" , text="Fichier Config", command=fichier_param,width=50, height=20)
fichConfig_button.grid(row=1, column=1, padx=10, pady=10)

qvs_button = customtkinter.CTkButton(button_frame2, image=caisse_image, compound="left" , text="QVS Version", command=version_qvs,width=50, height=20)
qvs_button.grid(row=2, column=1, padx=10, pady=10)

fastlane_button = customtkinter.CTkButton(button_frame2, image=caisse_image, compound="left" , text="Fastlane Version", command=version_fastlane,width=50, height=20)
fastlane_button.grid(row=3, column=1, padx=10, pady=10)

system_button = customtkinter.CTkButton(button_frame2, image=caisse_image, compound="left" , text="System Events", command=system_events,width=50, height=20)
system_button.grid(row=4, column=1, padx=10, pady=10)

# Bind the treeview
my_tree.bind("<ButtonRelease-1>", select_record)

# Run to pull data from database on start
query_database()

root.mainloop()


