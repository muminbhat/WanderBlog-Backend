# Generated by Django 4.2.5 on 2023-09-13 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_alter_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]