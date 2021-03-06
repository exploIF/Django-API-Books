# Generated by Django 3.2 on 2021-04-16 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('title', models.CharField(default='Untitled', max_length=100)),
                ('published_date', models.CharField(blank=True, max_length=30, null=True)),
                ('average_rating', models.FloatField(default=0)),
                ('rating_count', models.IntegerField(default=0)),
                ('thumbnail', models.CharField(max_length=250)),
                ('author', models.ManyToManyField(to='books_db.Authors')),
                ('category', models.ManyToManyField(to='books_db.Categories')),
            ],
        ),
    ]
