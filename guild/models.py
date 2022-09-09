from django.db import models


# Create your models here.
class Guild(models.Model):
    guild_name = models.CharField(max_length=20, unique=True, null=False, blank=False, help_text="길드 이름")
    guild_image = models.ImageField(help_text="길드 이미지")
    guild_description = models.CharField(max_length=50, null=False, blank=False, help_text="길드 설명")
    member_number = models.IntegerField(default=1, null=False, blank=False, help_text="길드 멤버수")
    created_at = models.DateTimeField(auto_now_add=True)