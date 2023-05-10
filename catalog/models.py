from django.db import models

# Create your models here.
class Category(models.Model):
    # Properties:
    name = models.CharField(max_length=100, unique=True, verbose_name='Назва категорії')

    # Presentation:
    def __str__(self) -> str:
        return str(self.name)


class Producer(models.Model):
    # Properties:
    name = models.CharField(max_length=100, unique=True, verbose_name='Назва виробника')

    # Presentation:
    def __str__(self) -> str:
        return str(self.name)


class Product(models.Model):
    # Properties:
    name = models.CharField(max_length=100, unique=True, verbose_name='Назва товару')
    about = models.TextField(max_length=500, unique=True, verbose_name='Про товар')

    # Foreign keys:
    # 2ий параметр - каскадний ефект - чи видаляти атрибут, при видалені обєкту
    # CASCADE - если удаляем Категорию, то автоматически удаляются все товари єтой категории
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)

    photo = models.FileField(upload_to='products/', verbose_name='Фото товару')
    price = models.FloatField(verbose_name='Ціна товару')

    # Presentation:
    def __str__(self) -> str:
        return str(self.name)