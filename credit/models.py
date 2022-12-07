import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=20)
    citizenship = models.CharField(max_length=20, default='Kyrgyzstan')
    birth_year = models.DateField()
    work_place = models.CharField(max_length=30, null=True, blank=True)
    update_date = models.DateField(auto_now=True)

    class Meta:
        db_table = 'customers'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name


class Account(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='accounts')
    number = models.IntegerField(max_length=16, primary_key=True)
    account_type = models.IntegerField(default=1)

    class Meta:
        db_table = 'accounts'
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'


class Credit(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='credits')
    sum = models.IntegerField()
    date = models.DateField(default=datetime.datetime.now)

    class Meta:
        db_table = 'loans'
        verbose_name = 'Кредит'
        verbose_name_plural = 'Кредиты'
