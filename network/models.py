from datetime import datetime

from django.db import models

from users.models import NULLABLE


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='название')
    model = models.CharField(max_length=150, verbose_name='модель', **NULLABLE)
    release_date = models.DateField(verbose_name='дата выхода продукта на рынок', **NULLABLE)

    def __str__(self):
        return f'{self.name}, {self.model}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class MetworkUnit(models.Model):

    TYPE_CHOICES = [
        ('FA', 'Завод'),
        ('RN', 'Розничная сеть'),
        ('IE', 'Индивидуальный предприниматель')
    ]

    LEVEL_CHOICES = [
        ('0', 'Нулевой уровень'),
        ('1', 'Первый уровень'),
        ('2', 'Второй уровень')
    ]

    name = models.CharField(max_length=500, verbose_name='Название')
    type = models.CharField(max_length=30, choices=TYPE_CHOICES, verbose_name='Тип звена сети')
    level = models.CharField(max_length=15, choices=LEVEL_CHOICES, verbose_name='Уровень в иерархии поставок')

    email = models.EmailField(max_length=254, verbose_name='email', null=True, blank=True)
    country = models.CharField(max_length=100, verbose_name='Страна', null=True, blank=True)
    city = models.CharField(max_length=100, verbose_name='Город', null=True, blank=True)
    street = models.CharField(max_length=100, verbose_name='Улица', null=True, blank=True)
    house_number = models.CharField(max_length=15, verbose_name='Номер дома', null=True, blank=True)

    product = models.ManyToManyField('Product', verbose_name='Продукты', related_name='products')
    supplier = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Cсылка на поставщика', null=True, blank=True)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Задолженность перед поставщиком', null=True, blank=True)
    date_create = models.DateTimeField(default=datetime.now, verbose_name='Время создания')

    def __str__(self):
        return f'{self.name} - {self.type}'

    class Meta:
        verbose_name = 'Торговый объект'
        verbose_name_plural = 'Торговые объекты'
