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


@app.route('/games', methods=['GET'])
def all_games():
    return jsonify({
        'games': GAMES,
        'status': 'success'
    })


def all_games():
    if request.method == 'POST':
        post_data = request.get_json()
        new_game = {
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played', False)  # Default to False if not provided
        }
        GAMES.append(new_game)
        response_object = {'status': 'success', 'message': 'Game Added !'}
    else:  # GET request
        response_object = {'status': 'success', 'games': GAMES}

    return jsonify(response_object)


if __name__ == "__main__":
    app.run(debug=True)
