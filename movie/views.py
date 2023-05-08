from rest_framework import viewsets, permissions, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import MovieSerializer
from .models import Movie
from rest_framework.pagination import PageNumberPagination


class MoviePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100



class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MoviePagination
    
    @action(detail=False, methods=['get'])
    def list_by_country(self, request):
        if country := request.query_params.get('country', None):
            movies = self.queryset.filter(country=country)
            page = self.paginate_queryset(movies)
            serializer = self.get_serializer(movies, many=True)
            return Response(serializer.data)
        return Response([])
        
    @action(detail=False, methods=['get'])
    def list_by_language(self, request):
        if language := request.query_params.get('language', None):
            movies = self.queryset.filter(language=language)
            serializer = self.get_serializer(movies, many=True)
            return Response(serializer.data)
        return Response([])
    
    @action(detail=False, methods=['get'])
    def list_by_blu_ray_available(self, request):
        movies = self.queryset.filter(isBluRay_available=True)
        serializer = self.get_serializer(movies, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def list_by_dvd_available(self, request):
        movies = self.queryset.filter(isDVD_available=True)
        serializer = self.get_serializer(movies, many=True)
        return Response(serializer.data)