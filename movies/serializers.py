from rest_framework import serializers
from movies.models import Movie

class MovieModelSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Movie
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year <1990:
            raise serializers.ValidationError(
                'The date of release didnt to be previous at 1990'
                )
        return value

    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError(
                'The resume must not to be longer then 200 characters'
            )
        return value
        