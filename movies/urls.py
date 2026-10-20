from django.urls import path
from .import views

urlpatterns = [

     path('movies/', views.MovieListCreateView.as_view(),
          name='movie-list-create-view'),
     path('movies/<int:pk>', views.MovieRetrieverUpdateDestroyView.as_view(),
          name='movie-retriever-update-destroy-view'),
     path('movies/stats',  views.MovieStatsView.as_view(),
          name='movies-stats-view'),

]

