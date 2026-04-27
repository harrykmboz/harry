

import sqlite3

conn = sqlite3.connect('hotel.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS MealRate (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        rate TEXT
    )
''')


# SQL query to create the 'customers' table
create_table_query = """
CREATE TABLE IF NOT EXISTS customers (
    ref TEXT PRIMARY KEY,
    name TEXT,
    father TEXT,
    mother TEXT,
    gender TEXT,
    post TEXT,
    mobile TEXT,
    email TEXT,
    nationality TEXT,
    comboidtype TEXT,
    Idnumber TEXT,
    address TEXT
);
"""

# Execute the CREATE TABLE query
cursor.execute(create_table_query)


# Create booking table
create_booking_table = """
CREATE TABLE IF NOT EXISTS booking (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contact TEXT,
    checkInDate TEXT,
    checkOutDate TEXT,
    roomType TEXT,
    availableRoom TEXT,
    meal TEXT,
    noOfDays INTEGER,
    paidTax REAL,
    roomRent REAL,
    mealCost REAL,
    totalCost REAL
);
"""

cursor.execute(create_booking_table)


# Create the 'rooms' table
create_rooms_table = """
CREATE TABLE IF NOT EXISTS rooms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    roomType TEXT,
    roomNumber TEXT UNIQUE,
    roomRent REAL
);
"""

cursor.execute(create_rooms_table)


# Create the tax table
create_tax_table = """
CREATE TABLE IF NOT EXISTS tax (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    taxValue TEXT
);
"""

cursor.execute(create_tax_table)


conn.commit()


