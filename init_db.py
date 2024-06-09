import os
import psycopg2

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="mydatabase",
    user="user",
    password="password"
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute commands to create a user table
cur.execute('DROP TABLE IF EXISTS users;')
cur.execute('''CREATE TABLE users (
                id serial PRIMARY KEY,
                name varchar(100) NOT NULL,
                email varchar(100) NOT NULL UNIQUE,
                date_registered date DEFAULT CURRENT_TIMESTAMP
            );''')

# Insert data into the user table
cur.execute('''INSERT INTO users (name, email)
               VALUES (%s, %s);''',
            ('John Doe', 'john@example.com'))

cur.execute('''INSERT INTO users (name, email)
               VALUES (%s, %s);''',
            ('Jane Smith', 'jane@example.com'))

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
