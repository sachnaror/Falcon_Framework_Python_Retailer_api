import random
import string

import pymysql
from faker import Faker

# Establish connection to the MySQL database
connection = pymysql.connect(
    host="127.0.0.1",  # Update with your MySQL host
    user="root",       # Update with your MySQL username
    #   password="sachin",  # Update with your MySQL password
    database="falcon_db"  # Update with your MySQL database name
)
cursor = connection.cursor()

fake = Faker()

# Loop to insert 100 rows of random data into the 'retailer' table
for i in range(1, 101):
    id = i
    GSTIN = ''.join(random.choice(string.ascii_uppercase +
                    string.ascii_lowercase + string.digits) for _ in range(15))
    Business_name = fake.name()
    Contact_person = fake.name()
    Contact_number = int(''.join(random.choice(string.digits)
                         for _ in range(5)))
    Contact_address = fake.address()
    Contact_emailId = fake.email()
    Status = random.choice(["active", "inactive", "active"])
    Outlet_limit = random.choice(range(1, 11))

    # Execute SQL query to insert data into the 'retailer' table
    cursor.execute("INSERT INTO retailer (id, GSTIN, Business_name, Contact_person, Contact_number, Contact_address, Contact_emailId, Status, Outlet_limit) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (id, GSTIN, Business_name, Contact_person, Contact_number, Contact_address, Contact_emailId, Status, Outlet_limit))

    # Commit the transaction
    connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
