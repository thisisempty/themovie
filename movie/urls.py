from django.urls import path
from movie.views import MovieView, ActorView


urlpatterns = [
    path('', ActorView.as_view()),
    path('movies/', MovieView.as_view())
]
