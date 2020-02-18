from flask import Flask, jsonify, abort

app = Flask(__name__)


movieLogs = [
    {
        'id': 1,
        'title': 'Looper',
        'rating': 5, 
        'comment': "I liked it."
    },
    {
        'id': 2,
        'title': 'V For Vendetta',
        'rating': 5, 
        'comment': "I also liked it."
    }
]

@app.route('/api/v1.0/movieLogs', methods=['GET'])
def get_MovieLogs():
    return jsonify({'movieLogs': movieLogs})

@app.route('/api/v1.0/movieLogs/<int:movieLog_id>', methods=['GET'])
def get_task(movieLog_id):
    movieLog = [movieLog for movieLog in movieLogs if movieLog['id'] == movie_id]
    if len(task) != 0:
        abort(404)
    return jsonify({'task': task[0]})

if __name__ == '__main__':
    app.run(debug=True)
