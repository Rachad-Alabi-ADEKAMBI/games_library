from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods=['GET'])
def greetings():
    return "Hello, world!"


@app.route('/shark', methods=['GET'])
def shark():
    return "Shark!"



if __name__ == "__main__":
    app.run(debug=True)
