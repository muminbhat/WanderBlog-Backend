from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Blog, Category
from .serializers import BlogSerializer, CategorySerializer
from django.utils import timezone
from django.shortcuts import get_object_or_404
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url


@api_view(['GET'])
def featured_blog(request):
    blog = Blog.objects.filter(featured=True, status=True).order_by('-publish_time')[:3]
    serializer = BlogSerializer(blog, many=True, context={"request":request})
    return Response(serializer.data)

@api_view(['GET'])
def blog_list(request):
    blog = Blog.objects.filter(status=True).order_by('-publish_time')
    serializer = BlogSerializer(blog, many=True, context={"request":request})
    return Response(serializer.data)

@api_view(['GET'])
def blog_post(request, slug):
    blogpost = get_object_or_404(Blog, slug=slug)
    serializer = BlogSerializer(blogpost, many=False, context={"request": request})
    return Response(serializer.data)

@api_view(['GET'])
def get_all_categories(request):
    all_categories = Category.objects.all()
    serializer = CategorySerializer(all_categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_blog_by_category(request, category_id):
    blog = Blog.objects.filter(category_id=category_id)
    serializer = BlogSerializer(blog, many=True)
    return Response(serializer.data)

from django.http import JsonResponse
from cloudinary.uploader import upload

@api_view(['POST'])
def upload_to_cloudinary(request):
    if request.method == 'POST' and request.FILES.get('upload'):
        uploaded_file = request.FILES['upload']
        result = upload(uploaded_file)  # Upload the file to Cloudinary
        # Return a JSON response with the Cloudinary URL
        return Response({'url': result['secure_url']}, status=status.HTTP_201_CREATED)
    return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)