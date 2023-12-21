from django.contrib import admin


from .models import FirstCertificate, SecondCertificate, ThirdCertificate

admin.site.register(FirstCertificate)
admin.site.register(SecondCertificate)
admin.site.register(ThirdCertificate)

# Register your models here.
