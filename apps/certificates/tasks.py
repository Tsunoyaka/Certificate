from django.core.mail import send_mail
from django.conf import settings
from config.celery import app
from decouple import config
from .models import FirstCertificate, SecondCertificate, ThirdCertificate

@app.task
def send_report_form(name, phone, route, date, time, auto, place_departure, price, contract_price):
    message_1 = f'Имя: {name}\nТелефон: {phone}\nНаправление: {route}\nМашина: {auto}\nЦена машины от: {price} сом\nДата: {date}\nВремя: {time}\nMecто выезда: {place_departure}'
    message_2 = f'Имя: {name}\nТелефон: {phone}\nНаправление: {route}\nМашина: {auto}\nЦена: Договорная\nДата: {date}\nВремя: {time}\nMecто выезда: {place_departure}'
    if contract_price is False:
        send_mail(
            subject='У вас заказали трансфер!',
            message=message_1,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[config('EMAIL')],
            fail_silently=False
        )
    else:
        send_mail(
            subject='У вас заказали трансфер!',
            message=message_2,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[config('EMAIL')],
            fail_silently=False
        )


def date_chek():
    first_certificate = FirstCertificate.objects.all()
    second_cetificate = SecondCertificate.objects.all()
    third_certificate = ThirdCertificate.objects.all()
    all_certificate = first_certificate + second_cetificate + third_certificate
    