from django.db import models

class Movie(models.Model):
    spine = models.IntegerField(primary_key=True)
    movie = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    media_type = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    
    # -1 means not available
    year = models.IntegerField(null=True)
    
    # -1 means not available
    runtime = models.IntegerField(null=True)
    isColor = models.CharField(max_length=50)
    
    # -1 means not available
    aspect_ratio = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    isBluRay_available = models.BooleanField()
    isDVD_available = models.BooleanField()
    
    # 0 means price not available
    # -1 means out of print
    BluRay_price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    DVD_price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    
    poster_url = models.URLField()
    page_url = models.URLField()
    thumb_url = models.URLField()
