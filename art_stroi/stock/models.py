from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=100, verbose_name='Страна')

    class Meta:
        verbose_name = 'Страны'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.country_name


class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=100, verbose_name='Производитель')
    email = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, verbose_name='Страна производитель')

    class Meta:
        verbose_name = 'Производители'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.manufacturer_name


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Категория товара')

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name


class Branch(models.Model):
    branch_name = models.CharField(max_length=100, verbose_name='Филиал')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    phone = models.CharField(max_length=100, verbose_name='Номер')

    class Meta:
        verbose_name ='Филиалы'
        verbose_name_plural ='Филиалы'

    def __str__(self):
        return self.branch_name


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=100, verbose_name='Поставщик')
    way = models.CharField(max_length=100, verbose_name='Способ доставки')

    class Meta:
        verbose_name = 'Поставщики'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.supplier_name


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотография', blank=True)
    characteristic = models.TextField(blank=True, verbose_name='Характеристика')
    manufacturer = models.ForeignKey(Manufacturer, on_delete = models.PROTECT, verbose_name='Производитель')
    price = models.IntegerField(verbose_name='Цена')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    amount = models.IntegerField(verbose_name='Количество')
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT, verbose_name='Филиал')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'

    def __str__(self):
        return self.title


class Supply(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT, verbose_name='Филиал')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    amount = models.IntegerField(verbose_name='Количество')
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, verbose_name='Поставщик')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Товар')

    class Meta:
        verbose_name = 'Поставка'
        verbose_name_plural = 'Поставка'


class application(models.Model):
    name_of_manager = models.CharField(max_length=100, verbose_name='ФИО')
    title_of_product = models.CharField(max_length=100, verbose_name='Название продукта')
    amount_of_product = models.IntegerField(verbose_name='Количество')
    characteristic_of_product = models.TextField(verbose_name='Характеристика')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказ'

    def __str__(self):
        return self.title_of_product