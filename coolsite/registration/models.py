from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone


class CustomUserManager(UserManager):
    """Менеджер создания пользователя"""
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Неверный адрес электроннй почты.')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """Класс пользователя (замена встроенного)"""
    email = models.EmailField(verbose_name='Почта',unique=True, db_index=True)
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')

    is_active = models.BooleanField(default=True, verbose_name='Активный')
    is_superuser = models.BooleanField(default=False, verbose_name='Супер-пользователь')
    is_staff = models.BooleanField(default=False, verbose_name='Работник')

    date_joined = models.DateTimeField(default=timezone.now, verbose_name='Дата присоединения')
    last_login = models.DateTimeField(blank=True, null=True, verbose_name='Дата последнего логина')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
