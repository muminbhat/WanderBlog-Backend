from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.core.exceptions import ValidationError

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True,  allow_unicode=True, blank=True)
    author = models.CharField(max_length=255)
    read_time = models.IntegerField()
    publish_time = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='blogs/', blank=True,)
    info = models.CharField(max_length=1000, null=True)
    content = models.TextField()
    tags = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    
    def clean(self):
        # Query for the number of featured posts
        featured_count = Blog.objects.filter(featured=True).count()

        # Set the maximum number of allowed featured posts
        max_featured_posts = 3

        if self.featured and featured_count >= max_featured_posts:
            raise ValidationError(
                f"Only {max_featured_posts} posts can be featured at a time."
            )

    def save(self, *args, **kwargs):
        self.clean()  # Validate before saving
        super().save(*args, **kwargs)


    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Blog,self).save(*args,**kwargs)
    
    def __str__(self):
        return self.title + ' by ' + self.author