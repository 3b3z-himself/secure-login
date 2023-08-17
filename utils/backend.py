import mysql.connector
import json

with open('config.json', 'r') as file:
    data = json.load(file)

def get_json_from_database(project_id):
    try:
        connection = mysql.connector.connect(**data)
        cursor = connection.cursor()

        query = "SELECT json_column FROM your_table_name WHERE projectID = %s"
        cursor.execute(query, (project_id,))
        result = cursor.fetchone()

        if result:
            json_value = result[0]
            return json.loads(json_value)

        # Return None if no matching projectID is found in the database
        return None

    except mysql.connector.Error as error:
        print('Error:', error)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
