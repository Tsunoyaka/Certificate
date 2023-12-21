from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils.crypto import get_random_string


class UserManager(BaseUserManager):
    def _create(self, username, login, password, **extra_fields):
        if not username:
            raise ValueError('User must have username')
        if not login:
            raise ValueError('User must have login')
        user = self.model(
            username=username,
            login=login,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, login, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', False)
        return self._create(username, login, password, **extra_fields)

    def create_superuser(self, username, login, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        return self._create(username, login, password, **extra_fields)


class User(AbstractBaseUser):
    STUDY_FORM_CHOICES = (
        ('Очное', 'Очное'),
        ('Заочное', 'Заочное'),
        ('Вечернее', 'Вечернее')
    )
    STUDY_DEGREE_CHOICES = (
        ('Бакалавр', 'Бакалавр'),
        ('Магистр', 'Магистр')
    )
    username = models.CharField('ФИО', max_length=50)
    login = models.CharField('Логин', max_length=255, primary_key=True)
    email = models.CharField('email', max_length=255, null=True, blank=True)
    group_name = models.CharField('Группа', max_length=255)
    study_degree = models.CharField('Степень', max_length=8, choices=STUDY_DEGREE_CHOICES)
    study_form = models.CharField('Обучение', max_length=9, choices=STUDY_FORM_CHOICES)
    faculty_name = models.CharField('Факультет', max_length=255)
    date_of_birth = models.DateField('Дата рождения', null=True)
    course_num = models.PositiveSmallIntegerField('Курс', null=True)
    period_start = models.DateField('Период обучения с', null=True)
    period_end = models.DateField('Период обучения по', null=True)
    normative_duration = models.PositiveSmallIntegerField('Нормативный срок освоения', null=True)
    direction_name = models.CharField('Название бакалавриата', max_length=255)
    university_name = models.CharField('Университет', max_length=255)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return self.username

    def has_module_perms(self, app_label):
        return self.is_staff

    def has_perm(self, obj=None):
        return self.is_staff

    def create_activation_code(self):
        code = get_random_string(length=8)
        if User.objects.filter(activation_code=code).exists():
            self.create_activation_code()
        self.activation_code = code
        self.save()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'