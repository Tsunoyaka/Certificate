from django.db import models
from django.contrib.auth import get_user_model
from .utils import save_object, generate_unique_id

User = get_user_model()


class FirstCertificate(models.Model):
    student = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='first_certificate'
    )
    direction_number = models.CharField('Номер справки', max_length=255, blank=True)
    issue_date = models.DateField('Дата создания', blank=True, null=True)
    certificate_num = models.CharField('Номер сертификата', max_length=17, blank=True)
    confirm = models.BooleanField('Принять', default=False)
    reject = models.BooleanField('Отклонить', default=False)
    consideration = models.BooleanField('В рассмотрении', default=True)
    cancel = models.BooleanField('Отменить', default=False)

    def save(self,*args, **kwargs):
        if not self.certificate_num:
            self.certificate_num = generate_unique_id()
        save_object(self=self)
        super().save(*args, **kwargs)
        

class SecondCertificate(models.Model):
    student = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='second_certificate')
    embassy = models.CharField('Для посольства', max_length=255)
    certificate_num = models.CharField('Номер сертификата', max_length=255, blank=True)
    issue_date = models.DateField('Дата создания', blank=True, null=True)
    executor_name = models.CharField('Имя исполнителя', max_length=255, blank=True)
    project_authority_name = models.CharField('Имя проектора', max_length=255, blank=True)
    project_authority_role = models.CharField('Должность проектора', max_length=255, blank=True)
    confirm = models.BooleanField('Принять', default=False)
    reject = models.BooleanField('Отклонить', default=False)
    consideration = models.BooleanField('В рассмотрении', default=True)
    cancel = models.BooleanField('Отменить', default=False)

    def save(self,*args, **kwargs):
        if not self.certificate_num:
            self.certificate_num = generate_unique_id()
        save_object(self=self)
        super().save(*args, **kwargs)


class ThirdCertificate(models.Model):
    student = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='third_certificate')
    issue_date = models.DateField('Дата создания', blank=True, null=True)
    district=models.CharField('Район военкомата', max_length=255)
    confirm = models.BooleanField('Принять', default=False)
    reject = models.BooleanField('Отклонить', default=False)
    consideration = models.BooleanField('В рассмотрении', default=True)
    cancel = models.BooleanField('Отменить', default=False)

    def save(self,*args, **kwargs):
        save_object(self=self)
        super().save(*args, **kwargs)