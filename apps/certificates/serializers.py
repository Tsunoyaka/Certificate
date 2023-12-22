from rest_framework import serializers
from .models import FirstCertificate, SecondCertificate, ThirdCertificate
from .validations import certificate_validation, creation_validation, update_validation


class FirstCertificateSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(
        source='student.username'
    )

    class Meta:
        model = FirstCertificate
        fields = '__all__'

    def validate(self, attrs):
        return certificate_validation(self=self, attrs=attrs)
    

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        result = all(not getattr(instance, field) for field in ["confirm", "reject", "consideration", "cancel"])
        if result:
            representation['ineffective'] = True
        source = f"http://127.0.0.1:8000/certificate/first-certificate/{instance.pk}/"
        representation['source'] = source
        return representation
    
    
    def update(self, instance, validated_data):
        update_validation(instance=instance, validated_data=validated_data)
        validated_data['student'] = instance.student
        return super().update(instance, validated_data)


    def create(self, validated_data):
        return super().create(creation_validation(validated_data=validated_data, 
                                                  certificate_type=FirstCertificate))
        

class SecondCertificateSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(
        source='student.username'
    )

    class Meta:
        model = SecondCertificate
        fields = '__all__'


    def validate(self, attrs):
        user = self.context.get('request').user
        attrs_to_check = ['executor_name', 'project_authority_name', 'project_authority_role']
        for check in attrs_to_check:
            if check in attrs:
                if not user.is_staff:
                    raise serializers.ValidationError(
                        f'Заполнить поля: {attrs_to_check} может лишь администратор'
                    )
        return certificate_validation(self=self, attrs=attrs)


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        result = all(not getattr(instance, field) for field in ["confirm", "reject", "consideration", "cancel"])
        if result:
            representation['ineffective'] = True
        source = f"http://127.0.0.1:8000/certificate/second-certificate/{instance.pk}/"
        representation['source'] = source
        return representation


    def update(self, instance, validated_data):
        update_validation(instance=instance, validated_data=validated_data)
        validated_data['student'] = instance.student
        return super().update(instance, validated_data)


    def create(self, validated_data):
        return super().create(creation_validation(validated_data=validated_data, 
                                                  certificate_type=SecondCertificate))
    

class ThirdCertificateSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(
        source='student.username'
    )

    class Meta:
        model = ThirdCertificate
        fields = '__all__'


    def validate(self, attrs):
        return certificate_validation(self=self, attrs=attrs)
    

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        result = all(not getattr(instance, field) for field in ["confirm", "reject", "consideration", "cancel"])
        if result:
            representation['ineffective'] = True
        source = f"http://127.0.0.1:8000/certificate/third-certificate/{instance.pk}/"
        representation['source'] = source
        return representation
    
    
    def update(self, instance, validated_data):
        update_validation(instance=instance, validated_data=validated_data)
        validated_data['student'] = instance.student
        return super().update(instance, validated_data)


    def create(self, validated_data):
        return super().create(creation_validation(validated_data=validated_data, 
                                                  certificate_type=ThirdCertificate))
        
