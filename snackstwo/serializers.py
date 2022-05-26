from rest_framework import serializers
from .models import Snack

class SnacksSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ("id", "owner","name", "description", "create_at")
    model = Snack
