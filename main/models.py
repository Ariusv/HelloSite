from django.db import models
from django.urls import reverse_lazy


class Person(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    surname = models.CharField(max_length=50, verbose_name='Surname')
    email = models.CharField(max_length=100, unique=True, verbose_name='Email')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Time')

    def __str__(self):
        return str(self.name) + " " + str(self.surname)

    def get_absolute_url(self):
        return reverse_lazy('hello', kwargs={'person_id': self.pk})

    class Meta:
        ordering = ['-datetime']