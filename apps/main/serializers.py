from rest_framework import serializers
from .models import Main

# Для APIView
class MainAPIViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = ['title', 'description', 'banner_image']

# Для ViewSet
class MainViewSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = ['title', 'price', 'image']
    