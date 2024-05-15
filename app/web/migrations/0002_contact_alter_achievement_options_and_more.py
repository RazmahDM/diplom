# Generated by Django 5.0.6 on 2024-05-15 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('middle_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField(max_length=1000)),
                ('type', models.CharField(max_length=200)),
                ('kindbusiness', models.TextField(max_length=2000)),
                ('kindservice', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Заявка',
            },
        ),
        migrations.AlterModelOptions(
            name='achievement',
            options={'verbose_name': 'Достижение'},
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'verbose_name': 'Документ'},
        ),
        migrations.AlterModelOptions(
            name='example',
            options={'verbose_name': 'Пример работы'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Проект'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Услуга'},
        ),
    ]