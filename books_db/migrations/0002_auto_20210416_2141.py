# Generated by Django 3.2 on 2021-04-16 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_db', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='average_rating',
            new_name='averageRating',
        ),
        migrations.RenameField(
            model_name='books',
            old_name='published_date',
            new_name='publishedDate',
        ),
        migrations.RenameField(
            model_name='books',
            old_name='rating_count',
            new_name='ratingCount',
        ),
    ]
