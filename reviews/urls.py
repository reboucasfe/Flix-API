from django.urls import path
from .import views


urlpatterns = [
    path('review/', views.ReviewListCreateView.as_view(), name='review-list-create-view'),
    path('review/<int:pk>', views.ReviewRetieverUpdateDestroyView.as_view(), name='review-retriever,update,destroy-view')
]
