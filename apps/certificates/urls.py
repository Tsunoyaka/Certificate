from django.urls import path
from rest_framework.routers import DefaultRouter


from .views import MyCertificatesView, FirstCertificateView, SecondCertificateView, ThirdCertificateView


router = DefaultRouter()
router.register('first-certificate', FirstCertificateView)
router.register('second-certificate', SecondCertificateView)
router.register('third-certificate', ThirdCertificateView)

urlpatterns = [
    path('my-certificates/', MyCertificatesView.as_view()),
]


urlpatterns += router.urls


