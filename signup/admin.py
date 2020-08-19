from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import AugustUser, Referral


class ReferralInline(admin.TabularInline):
    model = Referral
    extra = 1

class AugustUserAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'email', 'phone', 'referral_code', 'referral_code_used',]
    list_display = ['id', 'email', 'phone']

class ReferralAdmin(admin.ModelAdmin):
    fields = ['user',] 

# Register your models here.
admin.site.register(AugustUser, AugustUserAdmin)
admin.site.register(Referral, ReferralAdmin)