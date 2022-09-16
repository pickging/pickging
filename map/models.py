from random import choices
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Path(models.Model):
    class PathLength(models.IntegerChoices):
        km2 = 2    # 2km
        km3 = 3    # 3km
        km5 = 5    # 5km

    name = models.CharField(max_length=20, help_text="경로 이름")
    length_category = models.IntegerField(choices=PathLength.choices, help_text="경로 거리 범주")
    geojson = models.TextField(null=True, blank=True, help_text="경로 geojson (문자열)")
    length = models.FloatField(default=0, help_text="실제 경로 거리")
    maybe_time = models.IntegerField(default=0, help_text="예상 소요시간(분)")
    mission = models.CharField(max_length=200, null=True, blank=True, help_text="미션")

    def __str__(self):
        return str(self.name)

class Spot(models.Model):
    class SpotType(models.IntegerChoices):
        SOL_SPOT = 0    # 솔방울 정산소
        PICK_SPOT = 1   # 픽스팟

    name = models.CharField(max_length=20, help_text="스팟 이름")
    coordinate = ArrayField(models.FloatField(), help_text="스팟 위경도")
    type = models.IntegerField(choices=SpotType.choices, help_text="스팟 종류(0:솔방울정산소, 1:픽스팟)")

    def __str__(self):
        return str(self.name)