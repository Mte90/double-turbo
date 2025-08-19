import uuid

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import (UserDetailsSerializer)
from django.conf import settings
from django.db.models import Q
from rest_framework import serializers

from api.forms import PasswordResetForm
from api.models import User


class UserSerializer(UserDetailsSerializer):
    telephone = serializers.CharField(required=True)

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'telephone',
        )

    def update(self, instance, validated_data):
        instance.telephone = validated_data.get('telephone', instance.telephone)

        instance.save()

        return instance


class RegisterSerializer(RegisterSerializer):
    username = serializers.CharField(required=False)
    first_name = serializers.CharField(max_length=20, required=True)
    last_name = serializers.CharField(max_length=20, required=True)
    telephone = serializers.CharField(max_length=30, required=True)

    def _has_phone_field(self):
        return None

    def get_cleaned_data(self):
        return {
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'telephone': self.validated_data.get('telephone', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()

        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.telephone = self.cleaned_data.get('telephone')
        user.is_active = False
        user.save()

        setup_user_email(request, user, [])
        adapter.save_user(request, user, self)
        return user
