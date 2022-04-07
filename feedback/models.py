from django.db import models


class feedback(models.Model):
    name = models.CharField(verbose_name='Ваше имя', max_length=50)
    email = models.EmailField(verbose_name='Email', max_length=120)
    theme = models.CharField(verbose_name='Тема', max_length=100)
    message = models.TextField(verbose_name='Сообщение', max_length=1500)

    def __str__(self):
        return self.theme


class review(models.Model):
    name = models.CharField(verbose_name='Ваше имя', max_length=50)
    email = models.EmailField(verbose_name='Email', max_length=120)
    url = models.URLField(verbose_name='Cсылка на аккаунт', max_length=100)
    message = models.TextField(verbose_name='Сообщение', max_length=1500)

    def __str__(self):
        return self.url

