from django.shortcuts import render

import json
from django.http import JsonResponse
from django.views import View
from movie.models import Actor, Movie


class MovieView(View):

    def post(self, request):
        data = json.loads(request.body)
        Movie.objects.create(
            title=data['title'],
            release_date=data['release_date'],
            running_time=data['running_time']
        )
        return JsonResponse({'MESSAGE': 'SUCCESS'}, status=201)

    def get(self, requset):
        movies = Movie.objects.all()
        results = []

        for movie in movies:
            actors = movie.actor_set.all()
            results.append({
                "title": movie.title,
                "actor_list": [actor.first_name for actor in actors]
            })
        return JsonResponse({'result': results}, status=200)


class ActorView(View):
    def post(self, request):
        data = json.loads(request.body)
        Actor.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            date_of_birth=data['date_of_birth']
        )
        return JsonResponse({'MESSAGE': 'SUCCESS'}, status=201)

    def get(self, request):
        actors = Actor.objects.all()
        results = []

        for actor in actors:
            movies = actor.movies.all()
            movie_list = []

            for movie in movies:
                movie_list.append(movie.title)
            results.append({
                "name": actor.first_name,
                "movie_list": movie_list
            })

        return JsonResponse({'result': results}, status=200)


''' 
{
	"title" : "마약왕",
	"release_date" : "2018-12-19",
	"running_time" : 139
}

{
	"first_name" : "소담",
	"last_name" : "박",
	"date_of_birth" : "1991-09-08"
}
'''
