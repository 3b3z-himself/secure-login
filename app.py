from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        return "Under Maintenance.."

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "GET":
        return render_template('register.html')
    else:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        
        print(username, password, email)
        
        # Create a dictionary to hold the data and return it as JSON response
        response_data = {
            'username': username,
            'password': password,
            'email': email
        }
        
        return jsonify(response_data)

if __name__ == "__main__":
    app.run(debug=True, port="5000")