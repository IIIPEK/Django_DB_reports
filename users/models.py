from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False)
    fullname = models.CharField(max_length=150, blank=True, null=True, verbose_name='ФИО')
    phone = PhoneNumberField(blank=True, null=True, region='EE', verbose_name='Телефон')
    telegram_profile = models.OneToOneField('TelegramProfile', on_delete=models.SET_NULL, blank=True, null=True, related_name='user')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.fullname or self.email or self.username

class TelegramProfile(models.Model):
    chat_id = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    verified_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.username or f"Telegram ID {self.id}"
