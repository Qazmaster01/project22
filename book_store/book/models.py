from django.db import models

# Create your models here.



class Language(models.Model):
    language = models.CharField(max_length=30)

    def __str__(self):
        return self.language


class Genre(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Author(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    oldname = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.surname} {self.name} {self.oldname}'


class Book(models.Model):
    title = models.CharField(max_length=30)
    amount_in_warehouse = models.IntegerField()
    book_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='languages', null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='genres', null=True, blank=True)

    def __str__(self):
        return self.title


