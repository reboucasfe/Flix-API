from django.contrib import admin
from django.urls import path
from actors.views import ActorListCreateView, ActorRetrieveUpdateDestroyView
from genres.views import GenreListCreateView, GenreRetrieverUpdateDestroyView
from movies.views import MovieListCreateView, MovieRetrieverUpdateDestroyView
from reviews.views import ReviewListCreateView, ReviewRetieverUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
        
    path('actors/', ActorListCreateView.as_view(),
         name='actors--list-create'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), 
         name='actor-retrieve-update-destroy-view'),

    path('genres/', GenreListCreateView.as_view(), 
         name='genre-list-create'),
    path('genres/<int:pk>/', GenreRetrieverUpdateDestroyView.as_view(), 
         name='genre-detail-view'),

     path('movies/', MovieListCreateView.as_view(),
          name='movie-list-create-view'),
     path('movies/<int:pk>', MovieRetrieverUpdateDestroyView.as_view(),
          name='movie-retriever-update-destroy-view'),

     path('review/', ReviewListCreateView.as_view(),
          name='review-list-create-view'),
     path('review/<int:pk>', ReviewRetieverUpdateDestroyView.as_view(),
          name='review-retriever,update,destroy-view')
]

