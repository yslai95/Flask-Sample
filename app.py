from flask import Flask, request, jsonify
import psycopg2

# Database connection details
DATABASE = {
    'host': 'localhost',
    'database': 'mydatabase',
    'user': 'user',
    'password': 'password'
}

app = Flask(__name__)

def connect_to_database():
    try:
        conn = psycopg2.connect(**DATABASE)
        return conn
    except psycopg2.Error as e:
        print("Unable to connect to the database")
        print(e)

@app.route('/')
def index():
    return 'Welcome to the Python Flask SQL API'

@app.route('/api/users', methods=['GET'])
def get_users():
    try:
        conn = connect_to_database()
       # Open a cursor to perform database operations
        cur = conn.cursor()
        
        # Execute the query to select all users from the users table
        cur.execute("SELECT * FROM users")
        
        # Fetch all rows
        result = cur.fetchall()
        
        # Close the cursor and connection
        cur.close()
        conn.close()

        # Return the user data as JSON
        return jsonify(result)
    except Exception as e:
        print(e)
        return 'Server Error', 500

@app.route('/api/user', methods=['POST'])
def add_user():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    
    try:
        conn = connect_to_database()
        cur = conn.cursor()
        
        # Execute the query to insert a new user into the users table
        cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        
        # Commit the transaction
        conn.commit()
        
        # Close the cursor and connection
        cur.close()
        conn.close()

        # Return a success message
        return jsonify({"message": "User added successfully"}), 201
    except Exception as e:
        print(e)
        return 'Server Error', 500

if __name__ == '__main__':
    app.run(debug=True, port=3000)
