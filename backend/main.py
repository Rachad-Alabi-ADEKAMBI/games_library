from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_mysqldb import MySQL

app = Flask(__name__)

# Enable CORS for all routes
CORS(app, resources={r"/*": {"origins": "*"}})

# Database connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'games_library'

# Initialize MySQL
mysql = MySQL(app)

@app.route('/', methods=['GET'])
def greetings():
    return "Hello, world!"

@app.route('/shark', methods=['GET'])
def shark():
    return "Shark!"

# Display all games from the MySQL database
@app.route('/games', methods=['GET'])
def all_games():
    response_object = {'status': 'success'}
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM games ORDER BY id DESC")
    data = cur.fetchall()
    cur.close()
    response_object['games'] = data
    return jsonify(response_object)


@app.route('/games', methods=['GET'])
def insert():
    response_object = {'status': 'success'}
    cur = mysql.connection.cursor()
    cur.execute("INSERT IN games")
    data = cur.fetchall()
    cur.close()
    response_object['games'] = data
    return jsonify(response_object)


if __name__ == '__main__':
    app.run(debug=True)
