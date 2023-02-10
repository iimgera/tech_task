from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=False, verbose_name='Название')
    description = models.CharField(max_length=255, blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, verbose_name='Цена')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return self.name
    


