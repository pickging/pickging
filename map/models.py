from random import choices
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Path(models.Model):
    class PathLength(models.IntegerChoices):
        km1 = 1    # 1km (pk)
        km3 = 3    # 3km (pk)
        km5 = 5    # 5km (pk)

    path_coordinate = ArrayField(models.CharField(max_length=30), null=True, blank=True, help_text="경로 위경도 배열") # ['127.0 35.0', '127.1 35.1']
    path_length = models.IntegerField(choices=PathLength.choices, primary_key=True, help_text="경로 길이(1:1km, 3:3km, 5:5km)")
    mission = models.CharField(max_length=200, null=True, blank=True, help_text="미션")

    def __str__(self):
        return str(self.path_length) + "km 경로"

class Spot(models.Model):
    class SpotType(models.IntegerChoices):
        SOL_SPOT = 0    # 솔방울 정산소
        PICK_SPOT = 1   # 픽스팟

    spot_coordinate = ArrayField(models.FloatField(), null=True, blank=True, help_text="스팟 위경도") # [127.1, 35.0]
    spot_type = models.IntegerField(choices=SpotType.choices, help_text="스팟 종류(0:솔방울정산소, 1:픽스팟)")