from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    image = models.ImageField(upload_to="catalog/image", blank=True, null=True)
    category = models.CharField(max_length=100, verbose_name="Категория")
    price = models.IntegerField(verbose_name="Цена")
    created_at = models.DateField(verbose_name="дата создания")
    updated_at = models.DateField(verbose_name="дата последнего изменения")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name"]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name
