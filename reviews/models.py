from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie



class Review(models.Model):
    movie = models.ForeignKey(Movie, 
        on_delete=models.PROTECT, 
        related_name='reviews'
    )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'The rating cannot be lower than 0 stars.'),
            MaxValueValidator(5, 'The rating cannot be higher than 0 stars.'),
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.movie

