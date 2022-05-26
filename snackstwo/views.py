from rest_framework import generics
from .models import Snack
from .serializers import SnacksSerializer

# Create your views here.

# class SnackList(generics.ListAPIView):
#   queryset= Snack.objects.all()
#   serializer_class= SnacksSerializer  

class SnackList(generics.ListCreateAPIView):
  queryset= Snack.objects.all()
  serializer_class= SnacksSerializer  

class SnackDetail(generics.RetrieveAPIView):
  queryset= Snack.objects.all()
  serializer_class= SnacksSerializer  

