from django.db import models

# Create your models here.


class Slide(models.Model):
    img = models.ImageField('Картинка')
    

class Example(models.Model):
    img = models.ImageField('Картинка')
    text = models.CharField('Текст', max_length=255)
    
    class Meta:
        verbose_name = "Пример работы"

class Achievement(models.Model):
    img = models.ImageField('Картинка')
    text = models.TextField('Текст')
    class Meta:
        verbose_name = "Достижение"

class Document(models.Model):
    file = models.FileField('Файл')
    data = models.DateField('Дата')
    heading = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Текст')
    class Meta:
        verbose_name = "Документ"


class Service(models.Model):
    img = models.ImageField('Картинка')
    heading = models.CharField('Заголовок', max_length=255)
    subheading = models.CharField('Подзаголовок', max_length=255)
    text = models.TextField('Текст')
    class Meta:
        verbose_name = "Услуга"


class Project(models.Model):
    img = models.ImageField('Картинка')
    heading = models.CharField('Заголовок', max_length=255)
    subheading = models.CharField('Подзаголовок', max_length=255)
    text = models.TextField('Текст')
    class Meta:
        verbose_name = "Проект"


class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=1000)
    type = models.CharField(max_length=200)
    kindbusiness = models.TextField(max_length=2000)
    kindservice = models.CharField(max_length=200)

    def __str__(self):
        # Будет отображаться следующее поле в панели администрирования
        return self.email
    
    class Meta:
        verbose_name = "Заявка"