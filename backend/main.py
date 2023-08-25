from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods=['GET'])
def greetings():
    return "Hello, world!"


@app.route('/shark', methods=['GET'])
def shark():
    return "Shark!"


GAMES = [
    {
        'title':'2k21',
        'genre': 'sports',
        'played': 'True',
    },
    {
        'title':'COD',
        'genre': 'FPS',
        'played': 'True',
    },
    {
        'title':'PUBG',
        'genre': 'FPS',
        'played': 'False',
    },
]


#display all
@app.route('/games', methods=['GET', 'POST'])
def all_games():
    response_object = {'status': 'success'}

    if request.method == 'POST':
        post_data = request.get_json()
        GAMES.append({
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played')
        })
        response_object['message'] = 'Game added!'
    else:
        response_object['games'] = GAMES

    return jsonify(response_object)


def insert():
    response_object = {'status': 'success'}

    if request.method == 'POST':
        post_data = request.get_json()
        GAMES.append({
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played')
        })
        response_object['message'] = 'Game added!'
    else:
        response_object['games'] = GAMES

    return jsonify(response_object)


if __name__ == "__main__":
    app.run(debug=True)
