from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.

class Federation(models.Model):
    
    class Level(models.TextChoices):
        REG = "REG", _("Региональный")
        CEN = "CEN", _("Центральный")
        
    name = models.CharField("Наименование", max_length=300, db_index=True)
    email = models.EmailField("Электронная почта")
    phone = models.CharField("Телефон", max_length=20, blank=True, null=True)
    address = models.CharField("Адрес", max_length=300, blank=True, null=True)
    agent = models.ForeignKey(User, verbose_name="Представитель", db_index=True, null=True, on_delete=models.SET_NULL)
    level = models.CharField("Уровень", max_length=3, choices=Level, default=Level.REG)