from django.db import models

# Create your models here.


class Slide(models.Model):
    img = models.ImageField('Картинка')

class Example(models.Model):
    img = models.ImageField('Картинка')
    text = models.CharField('Текст', max_length=255)

class Achievement(models.Model):
    img = models.ImageField('Картинка')
    text = models.TextField('Текст')

class Document(models.Model):
    file = models.FileField('Файл')
    data = models.DateField('Дата')
    heading = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Текст')


class Service(models.Model):
    img = models.ImageField('Картинка')
    heading = models.CharField('Заголовок', max_length=255)
    subheading = models.CharField('Подзаголовок', max_length=255)
    text = models.TextField('Текст')


class Project(models.Model):
    img = models.ImageField('Картинка')
    heading = models.CharField('Заголовок', max_length=255)
    subheading = models.CharField('Подзаголовок', max_length=255)
    text = models.TextField('Текст')