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

    # Add this method to customize the representation of the 'image' field
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Modify the representation of the 'image' field to include the Cloudinary URL
        representation['image'] = instance.image.url

        return representation
