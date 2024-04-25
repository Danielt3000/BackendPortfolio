from rest_framework import generics, filters
from .serializers import CatSerializer
from .models import Cat
from django_filters.rest_framework import DjangoFilterBackend

class CatList(generics.ListAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    

