from flask import Flask, request, Response
from database.db import initialize_db
from database.models import Movie

application = Flask(__name__)


application.config['MONGODB_SETTINGS'] = {'host': 'mongodb+srv://dbuser:sa170687@db-1-ybzcs.mongodb.net/movie-db?retryWrites=true&w=majority'}
    #{'host': 'mongodb://localhost/movie-bag2'}
    #
initialize_db(application)


@application.route('/movies', methods=['GET'])
def get():
    movies = Movie.objects().to_json()
    return {'movies': movies}


@application.route('/movies', methods=['POST'])
def add():
    body = request.get_json()
    movie = Movie(**body).save()
    #id = movie.id
    return {"message": 'movie saved'}


@application.route('/movies/<int:index>', methods=['PUT'])
def update(index):
    body = request.get_json()
    Movie.objects.get(id=id).update(**body)
    return {'message': 'movie updated'}


@application.route('/movies/<int:index>', methods=['DELETE'])
def delete(index):
    Movie.objects.get(id=id).delete()
    return {'message': 'movie deleted'}


if __name__ == "__main__":
    application.run(debug=True)
