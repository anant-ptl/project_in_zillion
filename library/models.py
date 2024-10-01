from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_librarian = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    total_copies = models.IntegerField()
    available_copies = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class BookRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    requested_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    renewal_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} requested {self.book.title}"