from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['spine', 'movie', 'director', 'media_type', 'country', 'year', 'runtime', 'isColor', 'aspect_ratio', 'language', 'isBluRay_available', 'isDVD_available', 'BluRay_price', 'DVD_price', 'poster_url', 'page_url', 'thumb_url']
