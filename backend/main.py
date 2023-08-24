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


#delete
@app.route('/deleteGame', methods=['POST'])
def delete():
    response_object = {'status': 'success'}

    if request.method == 'POST':
        post_data = request.get_json()
        GAMES.append({
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played')
        })
        response_object['message'] = 'Game deleted!'
    else:
        response_object['games'] = GAMES

    return jsonify(response_object)


#update
@app.route('/updateGame', methods=['POST'])
def delete():
    response_object = {'status': 'success'}

    if request.method == 'POST':
        post_data = request.get_json()
        GAMES.append({
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played')
        })
        response_object['message'] = 'Game updated!'
    else:
        response_object['games'] = GAMES

    return jsonify(response_object)

#add
@app.route('/add', methods = ['POST'])
def add():
    if request.method == 'POST':
        new_game = {
             'name' = request.form['name'],
             'genre' = request.form['genre'],
            'played'= request.form['played', False ]  # Default to False if not provided
        }
        GAMES.append(new_game)
        response_object = {'status': 'success', 'message': 'Game Added !'}

    return jsonify(response_object)


if __name__ == "__main__":
    app.run(debug=True)
