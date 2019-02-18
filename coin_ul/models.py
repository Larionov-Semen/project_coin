import datetime
from django.db import models
from django.utils import timezone


class Money(models.Model):
    STATUS = (
        ('ЕСТЬ', 'есть в наличие'),
        ('НЕТ', 'нет в наличие'),
        ('ОТМЕНА', 'отменён'),
    )
    Type_money = (
        ('note', 'банкнота'),
        ('coin', 'монета'),
        ('medal', 'медали'),
        ('', ''),
    )
    # название
    name = models.CharField(max_length=50)
    # год
    year = models.IntegerField(default=2000)
    # описание
    description = models.TextField(blank=True)
    # картинка
    picture = models.ImageField(blank=True, default=None)
    url = models.CharField(max_length=50, blank=True)
    # дата публикации
    pub_date = models.DateTimeField('date start', default=datetime.datetime.now(), )
    # статус
    status = models.CharField(max_length=7, default='Открыт', choices=STATUS)
    type_money = models.CharField(max_length=7, default='coin', choices=Type_money)
    # кол-во
    num = models.IntegerField(default=0)
    # цена
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    # название лота
    lot = models.ForeignKey(Money, on_delete=models.CASCADE, related_name='choice_1')
    # пользователь
    user = models.CharField(max_length=30)
    # email
    email = models.EmailField(default="none")
    # сумма
    choice_sum = models.FloatField(default=0)
    # кол-во
    num = models.IntegerField(default=0)
    # время ставки
    time = models.DateTimeField(default=timezone.now, blank=True)
    # описание
    description = models.TextField(blank=True)

    def __str__(self):
        return self.user

