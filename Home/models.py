from django.db import models


class rating(models.Model):
    name = models.CharField('Название канала', max_length=120)
    photo = models.ImageField(null=True, blank=True, upload_to="images/")
    url = models.URLField('Ссылка на канал')
    text = models.TextField('Текст', null=True, blank=True)
    content = models.TextField('Содержание', null=True, blank=True)
    date = models.DateField('Дата публикации', null=True, blank=True)
    rating = models.IntegerField('Рейтинг', null=True, blank=True)
    passed = models.BooleanField('Прошел ли проверку?')

    def __str__(self):
        return self.name
