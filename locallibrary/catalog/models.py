from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class MyModelName(models.Model):
    my_field_name = models.CharField(max_length=20, help_text="Enter field documentation")

    class Meta:
        ordering = ["-my_field_name"]

    def get_absolute_url(self):
        return  reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.field_name

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a book genry (e.g. Science Fiction, French Poety etc.)")

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="enter a breif description of the book")
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>)
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )