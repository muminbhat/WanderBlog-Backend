from django.urls import path
from .views import post_create_view
from .views import handle_preflight

urlpatterns = [
    path('post/', post_create_view, name='newsletter-create'),
    path('preflight/', handle_preflight, name='handle-preflight'),  # Use a different path
]