from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from django.shortcuts import get_object_or_404

from .models import FirstCertificate, SecondCertificate, ThirdCertificate
from .serializers import FirstCertificateSerializer, SecondCertificateSerializer, ThirdCertificateSerializer
from .permission import IsOwnerOrReadOnly
from .gen_certificate import first_certificate, second_certificate, third_certificate
from .utils import get_certificate
from rest_framework import filters  

import django_filters

class FirstCertificateFilter(django_filters.FilterSet):
    confirm = django_filters.BooleanFilter(field_name='confirm')
    reject = django_filters.BooleanFilter(field_name='reject')
    cancel = django_filters.BooleanFilter(field_name='cancel')
    consideration = django_filters.BooleanFilter(field_name='consideration')

    class Meta:
        model = FirstCertificate
        fields = ['confirm', 'reject', 'cancel', 'consideration']



class FirstCertificateView(ModelViewSet):
    queryset = FirstCertificate.objects.all()
    serializer_class = FirstCertificateSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        if self.action in ['create']:
            self.permission_classes = [IsAuthenticated]
        if self.action in ['destroy', 'update', 'partial_update']:
            self.permission_classes = [AllowAny]
        return super().get_permissions()

    def retrieve(self, request, *args, **kwargs):
        return get_certificate(request=request, queryset=FirstCertificate, certificate_gen=first_certificate, pk=kwargs['pk'])
    
    def list(self, request, *args, **kwargs):
        certificate = FirstCertificate.objects.filter(student=request.user)
        serializer = FirstCertificateSerializer(instance=certificate, many=True)
        return Response(serializer.data)
    

class GetAllFirstCertificate(ListAPIView):
    queryset = FirstCertificate.objects.all()
    serializer_class = FirstCertificateSerializer
    filter_class = FirstCertificateFilter
    filter_backends = [filters.OrderingFilter]  
    ordering_fields = ['issue_date'] 

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
 

class MyCertificatesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        first_certificate = FirstCertificate.objects.filter(student=request.user)
        first_serializer = FirstCertificateSerializer(instance=first_certificate, many=True)
        second_certificate = SecondCertificate.objects.filter(student=request.user)
        second_serializer = SecondCertificateSerializer(instance=second_certificate, many=True)
        third_certificate = ThirdCertificate.objects.filter(student=request.user)
        third_serializer = ThirdCertificateSerializer(instance=third_certificate, many=True)
        combined_data = {
            'first_certificate': first_serializer.data,
            'second_certificate': second_serializer.data,
            'second_certificate': third_serializer.data,
        }
        if not first_certificate and not second_certificate:
            return Response('У вас ещё нет сертификата', status=status.HTTP_404_NOT_FOUND)
        return Response(combined_data, status=status.HTTP_200_OK)
   

class SecondCertificateView(ModelViewSet):
    queryset = SecondCertificate.objects.all()
    serializer_class = SecondCertificateSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        if self.action in ['create']:
            self.permission_classes = [IsAuthenticated]
        if self.action in ['destroy', 'update', 'partial_update']:
            self.permission_classes = [IsOwnerOrReadOnly]
        return super().get_permissions()
    
    def retrieve(self, request, *args, **kwargs):
        return get_certificate(request=request, queryset=SecondCertificate, certificate_gen=second_certificate, pk=kwargs['pk'])
    

    def list(self, request, *args, **kwargs):
        certificate = SecondCertificate.objects.filter(student=request.user)
        serializer = SecondCertificateSerializer(instance=certificate, many=True)
        return Response(serializer.data)


class ThirdCertificateView(ModelViewSet):
    queryset = ThirdCertificate.objects.all()
    serializer_class = ThirdCertificateSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        if self.action in ['create']:
            self.permission_classes = [IsAuthenticated]
        if self.action in ['destroy', 'update', 'partial_update']:
            self.permission_classes = [IsOwnerOrReadOnly]
        return super().get_permissions()
    
    def retrieve(self, request, *args, **kwargs):
        return get_certificate(request=request, queryset=ThirdCertificate, certificate_gen=third_certificate, pk=kwargs['pk'])

    def list(self, request, *args, **kwargs):
        certificate = ThirdCertificate.objects.filter(student=request.user)
        serializer = ThirdCertificateSerializer(instance=certificate, many=True)
        return Response(serializer.data)