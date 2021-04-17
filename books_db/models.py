from django.db import models


class Authors(models.Model):
    """
    A class to represent authors objects in database.

    Attributes
    ________
    name : str
        Author's full name
    """

    name = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.name


class Categories(models.Model):
    """
    A class to represent categories in database.

    Attributes
    ________
    name : str
        Category name
    """

    name = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.name


class Books(models.Model):
    """
    A class to represent books objects in database.

    Attributes
    ________
    id : str
        Book's id based on googleapi id
    title : str
        Book's title
    author : str
        Book's author name which is many to many relationship with Authors class (table in database)
    publishedDate : str
        Book's published date.
    category : str
        Book's category name which is many to many relationship with Categories class (table in database)
    averageRating : float
        Average rating of the book
    ratingsCount : int
        Number of votes for the book
    thumbnail : str
        Url to book's picture.
    """

    id = models.CharField(max_length=80, primary_key=True)
    title = models.CharField(max_length=250, default='Untitled')
    author = models.ManyToManyField(Authors)
    publishedDate = models.CharField(max_length=30, null=True, blank=True)
    category = models.ManyToManyField(Categories)
    averageRating = models.FloatField(default=0)
    ratingsCount = models.IntegerField(default=0)
    thumbnail = models.CharField(max_length=250)

    def __str__(self):
        return self.title


