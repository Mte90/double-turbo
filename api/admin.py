from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from unfold.admin import ModelAdmin
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialToken, SocialApp, SocialAccount
from django.contrib.sites.models import Site
from rest_framework.authtoken.models import TokenProxy
from hijack.contrib.admin import HijackUserAdminMixin

from .models import User

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(HijackUserAdminMixin, BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


# Disable from admin useless models
admin.site.unregister(EmailAddress)
admin.site.unregister(TokenProxy)
admin.site.unregister(SocialApp)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialToken)
admin.site.unregister(Site)


def no_log(*args, **kwargs):
    pass


admin.ModelAdmin.log_addition = no_log
admin.ModelAdmin.log_change = no_log
admin.ModelAdmin.log_deletion = no_log
