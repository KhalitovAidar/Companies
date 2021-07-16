from datetime import date

from django.db import models
from django.urls import reverse


class OwnerCompany(models.Model):
    name = models.CharField('Имя', max_length=100)
    age = models.PositiveSmallIntegerField('Возраст', default=0)
    description = models.TextField('Описание')
    image = models.ImageField('Image', upload_to='owners/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Владелец'


class Stock(models.Model):
    type = models.CharField('Тип акции', max_length=20)
    cost = models.PositiveIntegerField('Стоимость', default=0)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'


class Company(models.Model):
    name = models.CharField('Название', max_length=100)
    year = models.PositiveSmallIntegerField('Год основания', default=2021)
    money = models.PositiveBigIntegerField('Стоимость', default=0)
    tagline = models.CharField('Tagline', max_length=100, default='')
    inn_id = models.CharField('Инн компании', max_length=15, unique=True)
    kpp_id = models.CharField('КПП компании', max_length=10, unique=True)
    stock = models.ManyToManyField(Stock, default=0)
    image = models.ImageField('Image', upload_to='company_image/')
    type_company = models.CharField('Тип компании', max_length=100)
    owner = models.ForeignKey(OwnerCompany, verbose_name='Владелец', on_delete=models.CASCADE)
    address = models.CharField('Адрес организации', max_length=100)
    status = models.CharField('Статус', max_length=20)
    url = models.SlugField(max_length=130, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('companysingle', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField('Name', max_length=100)
    text = models.TextField('Message', max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name='Parent', on_delete=models.SET_NULL, blank=True, null=True
    )
    company = models.ForeignKey(Company, verbose_name='company', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.company}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
