from rest_framework import serializers
from datetime import datetime

def certificate_validation(self, attrs):
    user = self.context.get('request').user
    attrs['student'] = user
    if 'confirm' and 'reject' in attrs:
        confirm = attrs['confirm']
        reject = attrs['reject']
        if not user.is_staff and confirm or reject:
            raise serializers.ValidationError(
                'Подтверждать или отклонять справки может только администратор'
            )
        if confirm and reject:
            raise serializers.ValidationError(
                'Может быть выбрано только одно значение!'
            )
    return attrs


def date_chek(created_date):
    current_date = datetime.now().date()

    if created_date.month > 8:
        expiry_date = created_date.replace(year=created_date.year + 1, month=9, day=1)
    else:
        expiry_date = created_date.replace(month=9, day=1)

    if current_date < created_date:
        raise serializers.ValidationError(
            'Дата создания справки не может превышать текущую дату'
        )

    if current_date > expiry_date:
        return False
    else:
        return True
    

def creation_validation(validated_data, certificate_type):
    student=validated_data['student']
    certificate = certificate_type.objects.filter(student=student, consideration=True)
    if certificate.exists():
        raise serializers.ValidationError(
            'Ваш запрос уже подан и находится в рассмотрении'
        )
    created_date = certificate_type.objects.filter(student=student, confirm=True).order_by('-issue_date').first()
    if created_date:
        is_valid = date_chek(created_date.issue_date)
        if is_valid:
            raise serializers.ValidationError(
                'У вас уже имеется активная справка'
            )
        else:
            created_date.confirm = False
            created_date.save()
    validated_data['consideration'] = True
    return validated_data


def update_validation(instance, validated_data):
    result = all(not getattr(instance, field) for field in ["confirm", "reject", "consideration", "cancel"])
    if instance.cancel or result:
        raise serializers.ValidationError(
            'Обновить данные уже невозможно'
        )
    if validated_data['cancel']:
        if instance.student != validated_data['student']:
            raise serializers.ValidationError(
                'Отменить запрос может только сам студент'
            )
  
