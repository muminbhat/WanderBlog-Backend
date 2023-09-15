from rest_framework import serializers
from .models import Blog, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class BlogSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Blog 
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = instance.image.url

        return representation
