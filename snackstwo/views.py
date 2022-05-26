from rest_framework import generics
from .serializers import SnacksSerializer
from .models import Snack

# Create your views here.

# class SnackList(generics.ListAPIView):
#   queryset= Snack.objects.all()
#   serializer_class= SnacksSerializer  

class SnackList(generics.ListCreateAPIView):
  queryset = Snack.objects.all()
  serializer_class = SnacksSerializer  

class SnackDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Snack.objects.all()
  serializer_class = SnacksSerializer  

