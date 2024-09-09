from django.db import models


class Travel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='travel')
    price = models.IntegerField()
    text = models.TextField()

    def __str__(self):
        return self.title


class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    tour = models.CharField(max_length=100)

    def __str__(self):
        return self.name
