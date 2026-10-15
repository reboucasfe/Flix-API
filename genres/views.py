from rest_framework import generics
from genres.models import Genre
from genres.serializer import GenreSerializer


class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreRetrieverUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    