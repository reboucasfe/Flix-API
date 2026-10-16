from django.urls import path
from .import views

urlpatterns = [

     path('actors/', views.ActorListCreateView.as_view(),
          name='actors-list-create-view'),
     path('actors/<int:pk>', views.ActorRetrieveUpdateDestroyView.as_view(),
          name='actors-retriever,update,destroy-view')
]

