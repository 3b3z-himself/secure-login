import mysql.connector
import json, bcrypt, re, hashlib

def register_account(account_data, connection_params):
    try:
        connection = mysql.connector.connect(**connection_params)
        cursor = connection.cursor()

        # Validate email format
        if not re.match(r'^[\w\.-]+@[\w\.-]+$', account_data['email']):
            print("Invalid email format")
            return "Invalid email format"

        # Hash the password
        raw_password = account_data['password']
        hashed_password = hashlib.sha256(raw_password.encode('utf-8')).hexdigest()
        
        sql = "INSERT INTO accounts (username, password, email) VALUES (%s, %s, %s)"
        values = (account_data['username'], hashed_password, account_data['email'])

        cursor.execute(sql, values)
        connection.commit()  # Commit the transaction
        
        print("Account registered successfully!")
    except mysql.connector.Error as error:
        return f'Error: {error}'

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()



def validate_login(account_data, connection_params):
    try:
        connection = mysql.connector.connect(**connection_params)
        cursor = connection.cursor()

        username = account_data['username']
        entered_password = account_data['password']

        # Retrieve user's hashed password and salt from the database
        sql = "SELECT password FROM accounts WHERE username = %s"
        cursor.execute(sql, (username,))
        result = cursor.fetchone()

        if result:
            hashed_password = result[0]

            # Hash the entered password using the retrieved salt
            hashed_entered_password = hashlib.sha256(entered_password.encode('utf-8')).hexdigest()
            
            # Compare hashed passwords for validation
            if hashed_entered_password == hashed_password:
                print("Login successful!")
                message = "Login successful!"
            else:
                print("Invalid username or password")
                message = "Invalid username or password"
        else:
            print("Invalid username or password")
            message = "Invalid username or password"
        return message

    except mysql.connector.Error as error:
        print('Error:', error)
        message = f'Error: {error}'
        return message

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
