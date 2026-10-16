from django.contrib import admin
from django.urls import path
from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroyView
from genres.views import GenreCreateListView, GenreRetrieverUpdateDestroyView
from movies.views import MovieListCreateView, MovieRetrieverUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),
        
    path('actors/', ActorCreateListView.as_view(),
         name='actors-create-list'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), 
         name='actor-retrieve-update-destroy-view'),

    path('genres/', GenreCreateListView.as_view(), 
         name='genre-create-list'),
    path('genres/<int:pk>/', GenreRetrieverUpdateDestroyView.as_view(), 
         name='genre-detail-view'),

     path('movies/', MovieListCreateView.as_view(),
          name='movie-list-create-view'),
     path('movies/<int:pk>', MovieRetrieverUpdateDestroyView.as_view(),
          name='movie-retriever-update-destroy-view')
]

