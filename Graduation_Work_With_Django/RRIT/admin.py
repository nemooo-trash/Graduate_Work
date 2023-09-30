from django.contrib import admin
from collections import OrderedDict

from django.contrib import admin
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group
from users.models import User
from users.admin import UserChangeForm, UserCreationForm


class CustomUserAdmin(admin.ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm,
    fieldsets = [
        (
            None,
            {
                "fields": ["email", "password"],
            },
        ),
        (
            'Личные данные',
            {
                "fields": ["name", "surname", "lastname"],
            },
        ),
        (
            'Права доступа',
            {
                "fields": ['groups',],
            },
        ),
    ]
    list_display = ('id', 'name', 'surname', 'lastname', )
    list_display_links = ('id', 'name')
    search_fields = ('email', 'surname', 'lastname')
    ordering = ('email','name', 'surname')
    filter_horizontal = ('groups', 'user_permissions',)
    #list_editable = []
admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)
