# Generated by Django 4.1.4 on 2022-12-09 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='Название')),
                ('slug', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000, verbose_name='Текст комментария')),
                ('create_date', models.DateTimeField(auto_now=True, verbose_name='Дата комментария')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='URL')),
                ('content', models.TextField(verbose_name='Текст новости')),
                ('image', models.ImageField(upload_to='media/%Y/%m/%d/', verbose_name='Изображение')),
                ('date_publication', models.DateTimeField(auto_now=True, verbose_name='Дата публикации')),
                ('date_update', models.DateTimeField(auto_now_add=True, verbose_name='Дата изменения')),
                ('views', models.IntegerField(default=0, verbose_name='Просмотры')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('categories', models.ManyToManyField(to='news.category', verbose_name='Категории')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
