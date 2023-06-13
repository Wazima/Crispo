from flask import Flask
from flask import render_template
from flask import request,jsonify
import pymysql

app = Flask(__name__)

# MySQL configuration
host = 'localhost'
user = 'root'
password = ''
database = 'crispo'

@app.route('/')
@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()

    # Extracting data from the request
    username = data['username']
    email = data['email']
    password = data['password']

    # Connect to MySQL
    conn = pymysql.connect(host=host, user=user, password=password, database=database)
    
    # Create a cursor object
    cursor = conn.cursor()
    # Validating the input data
    if not username or not email or not password:
        return jsonify({'message': 'Please provide all the required fields'}), 400

    # Storing the data to the MySQL database
    try:
        cursor.execute(
            "Select username from  user " )
        # mysql.connection.commit()
        cursor.close()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        return jsonify({'message': 'Error occurred while creating the user', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run()

# def index():
#     # Connect to MySQL
#     conn = pymysql.connect(host=host, user=user, password=password, database=database)
    
#     # Create a cursor object
#     cursor = conn.cursor()
    
#     # Execute a sample query
#     cursor.execute("SELECT * FROM user")
    
#     # Fetch all rows from the result
#     rows = cursor.fetchall()
    
#     # Close the cursor and connection
#     cursor.close()
#     conn.close()
    
#     return render_template('index.html', rows=rows)

# if __name__ == '__main__':
#     app.run()