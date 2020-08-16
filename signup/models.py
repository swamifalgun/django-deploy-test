import os
import base64
import string
import random
import signup
from django.db import models
from django.contrib.auth.models import User


class AugustUser(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = email = models.EmailField(null=False, blank=False)
    referral_code = models.CharField(max_length=255, null=True, blank=True)
    referral_code_used = models.CharField(max_length=255)
    phone = models.CharField(null=True, blank=True, max_length=64)
    auth_provider = models.CharField(max_length=255, null=True, blank=True)
    #references = models.ManyToManyField("self", blank=True, through='Referral', symmetrical=False, related_name='related_referrals+')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def generate_referral(self, *args, **kwargs):
        initials = "AUG"
        token_len = 8
        chars= string.ascii_uppercase + string.digits
        token= ''.join(random.choice(chars) for _ in range(token_len)) #make 8 character long unique key
        return initials + str(token)

    def clean(self, *args, **kwargs):
        if self.referral_code:
            self.referral_code
        else:
            self.referral_code = self.generate_referral()

    def __str__(self):
        return self.email


class Referral(models.Model):
    code = models.CharField(max_length=255, null=True, blank=True)
    user = models.ManyToManyField(AugustUser, blank=True)

    def __str__(self):
        return self.user.email