import uuid
from django.http import HttpResponse
from rest_framework.response import Response
from datetime import datetime


def generate_unique_id():
    unique_id = str(uuid.uuid4().int)
    formatted_id = f"{unique_id[0]}-{unique_id[1:5]}-{unique_id[5:13]}-{unique_id[13]}"
    return formatted_id


def save_object(self):
    if self.confirm or self.reject or self.cancel:
        self.consideration = False
    if self.confirm:
        if not self.issue_date:
            self.issue_date = datetime.today().date()


def get_certificate(request, queryset, certificate_gen, pk):
    user = request.user
    certificate = queryset.objects.filter(pk=pk).first()
    if certificate:
        result = all(not getattr(certificate, field) for field in ["confirm", "reject", "consideration", "cancel"])
        if certificate.confirm or user.is_staff or result:
            pdf_path = certificate_gen(certificate)
            with open(pdf_path, 'rb') as pdf_file:
                pdf_content = pdf_file.read()

            response = HttpResponse(pdf_content, content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="your_file.pdf"'
            return response
    return Response('У вас нет сертификата или он ещё не подтвержден')

