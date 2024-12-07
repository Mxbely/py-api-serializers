from django.urls import path, include
from cinema import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("cinema_halls", views.CinemaHallSet, basename="cinema_halls")
router.register("genres", views.GenreSet, basename="genres")
router.register("actors", views.ActorSet, basename="actors")
router.register("movies", views.MovieSet, basename="movies")
router.register("movie_sessions", views.MovieSessionSet, basename="movie_sessions")
router.register("orders", views.OrderSet, basename="orders")
router.register("tickets", views.TicketSet, basename="tickets")

urlpatterns = [
    path("", include(router.urls)),
]
