# Generated by Django 4.1.4 on 2022-12-07 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_news_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(verbose_name='Текст новости'),
        ),
    ]
