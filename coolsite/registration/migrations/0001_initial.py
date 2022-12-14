# Generated by Django 4.1.4 on 2022-12-09 10:48

from django.db import migrations, models
import django.utils.timezone
import registration.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True, verbose_name='Почта')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('is_active', models.BooleanField(default=True, verbose_name='Заботает')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Супер-пользователь')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Работник')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата присоединения')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='Дата последнего логина')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', registration.models.CustomUserManager()),
            ],
        ),
    ]
