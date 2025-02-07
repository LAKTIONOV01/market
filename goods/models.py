from django.db import models
from django.urls import reverse

# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Categories'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'



class Product(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    price = models.DecimalField(default=0,max_digits=7, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True)
    discount = models.DecimalField(default=0, max_digits=4, decimal_places=2, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(blank=True, null=True,verbose_name='Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('catalog:product', kwargs={'product_slug': self.slug})

    def display_id(self):
        return f'{self.id:05}'

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100)
        return self.price

    class Meta:
        db_table = 'Product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
