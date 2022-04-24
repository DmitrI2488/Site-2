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


class Comment(models.Model):
    chanel = models.ForeignKey(rating, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    only_user = models.BooleanField(default=False)
    rate = models.TextField(null=False, default=0)
    rate1 = models.TextField(null=False, default=0)
    rate2 = models.TextField(null=False, default=0)
    def __str__(self):
        return f'{self.body}'
