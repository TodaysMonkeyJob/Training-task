from tkinter import messagebox, ttk
from tkinter import *
import mysql.connector
import csv

root = Tk()
mainmenu = Menu(root)
root.config(menu=mainmenu)
root.title("Testing DataBase Project")
root.geometry("1600x600")

# Connect to MySQL
MyDB = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "sony1601",
        database = "mortem",
    )
# Check to see if connection to MySQL was created
#print(MyDB)

# Create a cursor and initialize it
DB_cursor = MyDB.cursor()

# Create DataBase just once create
#DB_cursor.execute("CREATE DATABASE mortem")

# Test if DataBase was created
'''
DB_cursor.execute("SHOW DATABASES")
for DB in DB_cursor:
    print(DB)
'''

# Drop Table
#DB_cursor.execute("DROP TABLE Storage")

# Create a table
DB_cursor.execute("CREATE TABLE IF NOT EXISTS Storage (\
    user_id INT AUTO_INCREMENT PRIMARY KEY, \
    Items_category VARCHAR(255), \
    Items_name VARCHAR(255), \
    Items_manufacturer VARCHAR(255), \
    Items_count INT(200), \
    Items_price DECIMAL(10,2))")

# Create alter Table just once
'''
DB_cursor.execute("ALTER TABLE Storage ADD (\
    Year_of_manufacture VARCHAR(255),\
    Expiration_date INT(240), \
    Provider VARCHAR(255), \
    Weight VARCHAR(255), \
    Quality_rate INT(10))")
'''
# Show Table
'''
DB_cursor.execute("SELECT * FROM Storage")
for thing in DB_cursor.description:
    print(thing)
'''
# Clear text Fields
def clear_fields():
    Items_category_box.delete(0, END)
    Items_name_box.delete(0, END)
    Items_manufacturer_box.delete(0, END)
    Items_count_box.delete(0, END)
    Items_price_box.delete(0, END)
    Year_of_manufacture_box.delete(0, END)
    Expiration_date_box.delete(0, END)
    Provider_box.delete(0, END)
    Weight_box.delete(0, END)
    Quality_rate_box.delete(0, END)

# Add Item to DataBase
def Add_Item():
    sql_command = "INSERT INTO Storage (Items_category, Items_name, \
    Items_manufacturer, Items_price, Items_count, Year_of_manufacture, \
    Expiration_date, Provider, Weight, Quality_rate) \
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    values = (Items_category_box.get(), Items_name_box.get(), Items_manufacturer_box.get(), Items_price_box.get(), Items_count_box.get(), Year_of_manufacture_box.get(), Expiration_date_box.get(), Provider_box.get(), Weight_box.get(), Quality_rate_box.get())
    DB_cursor.execute(sql_command, values)
    # Commit the changes to the database
    MyDB.commit()
    # Clear the Fields
    clear_fields()

# Show Item List
def refresh_data():
    Refresh_tittle = Label(root, text = "Storage DataBase INFO", font = ("Helvetica", 16))
    Refresh_tittle.grid(row = 3, column = 4, columnspan = 2, sticky = W, padx = 35)

    DB_cursor.execute("SELECT * FROM Storage")
    information = DB_cursor.fetchall()
    for index, x in enumerate(information):
        count_row = 0
        index += 2
        for column in x:
            lookup_label = Label(root, text = column)
            lookup_label.grid(row = index + 5, column = count_row)
            count_row += 1

# Write_To_CSV Excel Function
def write_to_csv(information):
    with open("Storage.csv", "w", newline = "") as file:
        write = csv.writer(file, dialect = "excel")
        for record in information:
            write.writerow(record)

# Create Saving for cascade menu
def cascade_save():
    # Query the Storage DataBase
    DB_cursor.execute("SELECT * FROM Storage")
    information = DB_cursor.fetchall()
    for index, x in enumerate(information):
        count_row = 0
        for column in x:
           lookup_label = Label(root, text = column)
           lookup_label.grid(row = index + 5, column = count_row)
           count_row += 1
    write_to_csv(information)

# Search element by name
def search_item():
    item_search_list = Tk()
    item_search_list.title(" Search in ALL Item ")
    item_search_list.geometry("1150x600")

    def update():
        sql_command = """UPDATE Storage SET Items_category = %s, Items_name = %s, \
            Items_manufacturer = %s, Items_price = %s, Items_count = %s, Year_of_manufacture = %s, \
            Expiration_date = %s, Provider = %s, Weight = %s, Quality_rate = %s WHERE user_id = %s"""

        Items_category = Items_category_box2.get()
        Items_name = Items_name_box2.get()
        Items_manufacturer = Items_manufacturer_box2.get()
        Items_price = Items_price_box2.get()
        Items_count = Items_count_box2.get()
        Year_of_manufacture = Year_of_manufacture_box2.get()
        Expiration_date = Expiration_date_box2.get()
        Provider = Provider_box2.get()
        Weight = Weight_box2.get()
        Quality_rate = Quality_rate_box2.get()

        id_value = id_box2.get()
        inputs = (Items_category, Items_name, Items_manufacturer, Items_price, Items_count, Year_of_manufacture, Expiration_date, Provider, Weight, Quality_rate, id_value)

        DB_cursor.execute(sql_command, inputs)
        item_search_list.destroy()

    def edit_item(id_reference, index):
        sql2 = "SELECT * FROM Storage WHERE user_id = %s"
        name2 = (id_reference, )
        result2 = DB_cursor.execute(sql2, name2)
        result2 = DB_cursor.fetchall()

        index += 2
        id_label = Label(item_search_list, text = "ID", width = 10).grid(row = 1 + index, column = 0,  sticky = W, padx =15)
        Items_category_label = Label(item_search_list, text = "Category Name").grid(row = 1 + index, column = 1, sticky = W, padx = 5)
        Items_name_label = Label(item_search_list, text = "Item Name").grid(row = 1  + index, column = 2, sticky = W, padx = 5)
        Items_manufacturer = Label(item_search_list, text = "Manufacture", width = 15).grid(row = 1  + index, column = 3, sticky = W, padx = 5)
        Items_price_label = Label(item_search_list, text = "Price", width = 10).grid(row = 1 + index, column = 4, sticky = W, padx = 5)
        Items_count_label = Label(item_search_list, text = "Count", width = 10).grid(row = 1 + index, column = 5, sticky = W, padx = 5)
        Year_of_manufacture_label = Label(item_search_list, text = "Year Manufacture").grid(row = 1 + index, column = 6, sticky = W, padx = 5)
        Expiration_date_label = Label(item_search_list, text = "Expiration date").grid(row = 1 + index, column = 7, sticky = W, padx = 5)
        Provider_label = Label(item_search_list, text = "Provider").grid(row = 1 + index, column = 8, sticky = W, padx = 5)
        Weight_label = Label(item_search_list, text = "Weight").grid(row = 1 + index, column = 9, sticky = W, padx = 5)
        Quality_rate_label = Label(item_search_list, text = "Quality Rate").grid(row = 1 + index, column = 10, sticky = W, padx = 5)

        # Create Entry Boxes
        global id_box2
        id_box2 = Entry(item_search_list, width = 12)
        id_box2.grid(row = 2 + index, column=0, padx = 3, pady = 10)
        id_box2.insert(0, result2[0][0])

        global Items_category_box2
        Items_category_box2 = ttk.Combobox(item_search_list, value = ["", "Dairy", "Bakery", "Candy", "Nature", "Fish", "Meat", "Fruits", "Vegetables"], width = 12)
        Items_category_box2.current(0)
        Items_category_box2.grid(row = 2 + index, column = 1, padx = 3, pady = 10)
        Items_category_box2.insert(0, result2[0][1])

        global Items_name_box2
        Items_name_box2 = Entry(item_search_list, width = 12)
        Items_name_box2.grid(row = 2 + index, column = 2, padx = 3, pady = 10)
        Items_name_box2.insert(0, result2[0][2])

        global Items_manufacturer_box2
        Items_manufacturer_box2 = Entry(item_search_list, width = 12)
        Items_manufacturer_box2.grid(row = 2 + index, column = 3, padx = 3, pady = 10)
        Items_manufacturer_box2.insert(0, result2[0][3])

        global Items_price_box2
        Items_price_box2 = Entry(item_search_list, width = 12)
        Items_price_box2.grid(row = 2 + index, column = 4, padx = 3, pady = 10)
        Items_price_box2.insert(0, result2[0][5])

        global Items_count_box2
        Items_count_box2 = Entry(item_search_list, width = 12)
        Items_count_box2.grid(row = 2 + index, column = 5, padx = 3, pady = 10)
        Items_count_box2.insert(0, result2[0][4])

        global Year_of_manufacture_box2
        Year_of_manufacture_box2 = ttk.Combobox(item_search_list, value = ["", "2014", "2015", "2016", "2017", "2018", "2019", "2020"], width = 12)
        Year_of_manufacture_box2.current(0)
        Year_of_manufacture_box2.grid(row = 2 + index, column = 6, padx = 3, pady = 10)
        Year_of_manufacture_box2.insert(0, result2[0][6])

        global Expiration_date_box2
        Expiration_date_box2 = ttk.Combobox(item_search_list, value = ["", "15", "30", "120", "180", "365"], width = 12)
        Expiration_date_box2.current(0)
        Expiration_date_box2.grid(row = 2 + index, column = 7, padx = 3, pady = 10)
        Expiration_date_box2.insert(0, result2[0][7])

        global Provider_box2
        Provider_box2 = ttk.Combobox(item_search_list, value = ["", "CowINC", "NewPost", "Roshen", "GreenForest"], width = 12)
        Provider_box2.current(0)
        Provider_box2.grid(row = 2 + index, column = 8, padx = 3, pady = 10)
        Provider_box2.insert(0, result2[0][8])

        global Weight_box2
        Weight_box2 = Entry(item_search_list, width = 12)
        Weight_box2.grid(row = 2 + index, column = 9, padx = 3, pady = 10)
        Weight_box2.insert(0, result2[0][9])

        global Quality_rate_box2
        Quality_rate_box2 = ttk.Combobox(item_search_list, value = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], width = 12)
        Quality_rate_box2.current(0)
        Quality_rate_box2.grid(row = 2 + index, column = 10, padx = 3, pady = 10)
        Quality_rate_box2.insert(0, result2[0][10])

        save_record = Button(item_search_list, text = "Update record", command = update)
        save_record.grid(row = 0, column = 5, padx = 5)

    def search_now():
        selected = drop.get()
        sql = ""
        if selected == "Search by...":
            inform_label = Label(item_search_list, text = "You forgot to pick a drop box")
            inform_label.grid( row = 1, column = 1, columnspan = 2, padx = 10)
        if selected == "Category":
            sql = "SELECT * FROM Storage WHERE Items_category = %s"
        if selected == "Name":
            sql = "SELECT * FROM Storage WHERE Items_name = %s"
        if selected == "Provider":
            sql = "SELECT * FROM Storage WHERE Provider = %s"

        searching = search_box.get()
        name = (searching, )
        result = DB_cursor.execute(sql, name)
        result = DB_cursor.fetchall()

        if not result:
            result = messagebox.showwarning(parent = item_search_list, title = "Warning", message = "Record Not Found...")
        else:
            for index, x in enumerate(result):
                count_row = 0
                index += 2
                id_reference = str(x[0])
                edit_button = Button(item_search_list, text = "Edit" + id_reference, command = lambda: edit_item(id_reference, index), width = 10,  bg = "#C3CCD7")
                edit_button.grid(row = index, column = 11)
                print(id_reference)
                for column in x:
                    searching_label = Label(item_search_list, text = column, width = 8)
                    searching_label.grid(row = index, column = count_row, pady = 5)
                    count_row += 1

    # Entry box to search item
    search_box = Entry(item_search_list)
    search_box.grid(row = 0, column = 1, columnspan = 2, padx = 10, pady = 10)
    # Entry box Label search for item
    search_box_label = Label(item_search_list, text = "Searching INFO by")
    search_box_label.grid(row = 0, column = 0, padx = 5, pady = 10)
    # Entry box Button for item
    search_button = Button(item_search_list, text = " Search Item", command = search_now)
    search_button.grid(row = 0, column = 4, padx = 5)
    # Drop Down Box
    drop = ttk.Combobox(item_search_list, value = ["Search by...", "Category", "Name", "Provider"], width = 15)
    drop.current(0)
    drop.grid(row = 0, column = 3)

# Create label
Title_label = Label(root, text = "  Market storage DataBase", font = ("Helvetica", 16))
Title_label.grid(row = 0, column = 4, columnspan = 2, pady = "10")

# Create Main Form to Enter Storage Data
Items_category_label = Label(root, text = "Category Name").grid(row = 1, column = 0, sticky = W, padx = 30)
Items_name_label = Label(root, text = "Item Name").grid(row = 1, column = 1, sticky = W, padx = 35)
Items_manufacturer = Label(root, text = "Manufacture").grid(row = 1, column = 2, sticky = W, padx = 35)
Items_price_label = Label(root, text = "Price").grid(row = 1, column = 3, sticky = W, padx = 50)
Items_count_label = Label(root, text = "Count").grid(row = 1, column = 4, sticky = W, padx = 50)
Year_of_manufacture_label = Label(root, text = "Year Manufacture").grid(row = 1, column = 5, sticky = W, padx = 30)
Expiration_date_label = Label(root, text = "Expiration date").grid(row = 1, column = 6, sticky = W, padx = 30)
Provider_label = Label(root, text = "Provider").grid(row = 1, column = 7, sticky = W, padx = 43)
Weight_label = Label(root, text = "Weight").grid(row = 1, column = 8, sticky = W, padx = 47)
Quality_rate_label = Label(root, text = "Quality Rate").grid(row = 1, column = 9, sticky = W, padx = 35)

# Create Entry Boxes
global Items_category_box
Items_category_box = ttk.Combobox(root, value = ["Items Category...", "Dairy", "Bakery", "Candy", "Nature", "Fish", "Meat", "Fruits", "Vegetables"])
Items_category_box.current(0)
Items_category_box.grid(row = 2, column = 0)


global Items_name_box
Items_name_box = Entry(root)
Items_name_box.grid(row = 2, column = 1, pady = 10, padx = 5)

global Items_manufacturer_box
Items_manufacturer_box = Entry(root)
Items_manufacturer_box.grid(row = 2, column = 2, pady = 10, padx = 5)

global Items_price_box
Items_price_box = Entry(root)
Items_price_box.grid(row = 2, column = 3, pady = 10, padx = 5)

global Items_count_box
Items_count_box = Entry(root)
Items_count_box.grid(row = 2, column = 4, pady = 10, padx = 3)

global Year_of_manufacture_box
Year_of_manufacture_box = ttk.Combobox(root, value = ["Manufactured in...", "2014", "2015", "2016", "2017", "2018", "2019", "2020"])
Year_of_manufacture_box.current(0)
Year_of_manufacture_box.grid(row = 2, column = 5, pady = 10)

global Expiration_date_box
Expiration_date_box = ttk.Combobox(root, value = ["Expiration time...", "15", "30", "120", "180", "365"])
Expiration_date_box.current(0)
Expiration_date_box.grid(row = 2, column = 6, pady = 10)

global Provider_box
Provider_box = ttk.Combobox(root, value = ["Delivered by...", "CowINC", "NewPost", "Roshen", "GreenForest"])
Provider_box.current(0)
Provider_box.grid(row = 2, column = 7, padx = 5, pady = 10)

global Weight_box
Weight_box = Entry(root)
Weight_box.grid(row = 2, column = 8, pady = 10, padx = 5)

global Quality_rate_box
Quality_rate_box = ttk.Combobox(root, value = ["Rate by...", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
Quality_rate_box.current(0)
Quality_rate_box.grid(row = 2, column = 9, pady = 10)

# Add Item to Storage Buttons
global Add_Storage_button
Add_Storage_button = Button(root, text = "Add Item", height = 2, width = 10, bg = "#C3CCD7", command = Add_Item)
Add_Storage_button.grid(row = 2, column = 10, pady = 10, padx = 10)

# Clear Field Button
Clear_fields_button = Button(root, text = "Clear Fields", bg = "#C3CCD7", command = clear_fields)
Clear_fields_button.grid(row = 3, column = 10)

# Show Storage DataBase
Show_Storage_Button = Button(root, text = "Show Data", width = 17, bg = "#C3CCD7", command = refresh_data)
Show_Storage_Button.grid(row = 3, column = 0, sticky = W, padx = 10)

# Cascade Menu
filemenu = Menu(mainmenu, tearoff = 0)
filemenu.add_command(label = "Save as Excel", command = cascade_save)
filemenu.add_command(label = "Search Item", command = search_item)
mainmenu.add_cascade(label="File", menu = filemenu)

root.mainloop()