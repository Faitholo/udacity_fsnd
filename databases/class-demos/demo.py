import psycopg2
""" script that executes a postgresql script using pscopg2"""

# Establish a connection, begin transaction
connection = psycopg2.connect('dbname=test')

# Set a cursor to begin executing commands
cursor = connection.cursor()

# Drop table if table exists
cursor.execute("DROP TABLE IF EXISTS todos1;")

# Create a new table
cursor.execute('''
    CREATE TABLE todos1 (
    id serial PRIMARY KEY,
    item VARCHAR(255) NOT NULL
    );
''')

# SQL commands to innsert into table method one
cursor.execute('INSERT INTO todos1 (id, item) VALUES (%s, %s);', (1, 'food'))

cursor.execute('INSERT INTO todos1 (id, item) VALUES (%s, %s);', (2, 'clothes'))

# SQL commands to innsert into table method two
SQL = 'INSERT INTO todos1 (id, item) VALUES (%(id)s, %(item)s);'

data = {
    'id': 3, 
    'item': 'shoes'
}
cursor.execute(SQL, data)

# Fetch the executed data
cursor.execute('SELECT * FROM todos1;')

for i in data:
    result = cursor.fetchone()
    print(result)

# commit the transaction
connection.commit()

# close cursor
cursor.close()

# close connection
connection.close()
