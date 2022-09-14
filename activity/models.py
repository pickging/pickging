from django.db import models

# Create your models here.
class Activity(models.Model):
    user = models.ForeignKey("user.User", related_name="user", on_delete=models.CASCADE, null=True, blank=True, help_text="유저")
    path = models.ForeignKey("map.Path", related_name="path", on_delete=models.CASCADE, null=True, blank=True, help_text="경로")
    date = models.DateField(auto_now_add=True, help_text="날짜")
    point = models.IntegerField(default=0, help_text="포인트")
    garbage = models.FloatField(default=0, help_text="쓰레기양")
    heart_rate = models.IntegerField(default=0, help_text="심박수")
    step_count = models.IntegerField(default=0, help_text="걸음수")
    review = models.IntegerField(default=0, help_text="별점")