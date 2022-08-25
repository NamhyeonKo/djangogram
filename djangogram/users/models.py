from platform import python_version_tuple
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    #얘 처럼 저장 가능할줄 몰랐음 ㄷㄷ
    GENDER_CHOICES = [
        ('M','Male'),
        ('F','Female'),
    ]

    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    user_name = models.CharField(blank=True, max_length=255)
    profile_photo = models.ImageField(blank=True)   #? imagefield는 뭘 까?
    website = models.URLField(blank=True)   #? urlfield로 저장하면 일반 charfield와 뭐가 다를까?
    bio = models.TextField(blank=True)
    email = models.CharField(blank=True, max_length=255)
    phone_number = models.CharField(blank=True, max_length=255)
    gender = models.CharField(blank=True, choices=GENDER_CHOICES, max_length=255)
    follower = models.ManyToManyField("self")   #! manytomanyfield 이용하면 다대다 db 이용 가능
    following = models.ManyToManyField("self")

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
