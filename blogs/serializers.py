from rest_framework import serializers
from .models import Blog, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class BlogSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Include the CategorySerializer for the 'category' field

    class Meta:
        model = Blog 
        fields = '__all__'
