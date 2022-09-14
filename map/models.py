from random import choices
from django.db import models
# from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Path(models.Model):
    class PathLength(models.IntegerChoices):
        km2 = 2    # 2km
        km3 = 3    # 3km
        km5 = 5    # 5km

    length_category = models.IntegerField(choices=PathLength.choices, help_text="경로 거리 범주")
    # path_coordinate = ArrayField(models.CharField(max_length=30), null=True, blank=True, help_text="경로 위경도 좌표 배열") # ['127.0 35.0', '127.1 35.1']
    path_geojson = models.TextField(null=True, blank=True, help_text="경로 geojson (문자열)")
    path_length = models.FloatField(default=0, help_text="실제 경로 거리")
    maybe_time = models.IntegerField(default=0, help_text="예상 소요시간(분)")
    mission = models.CharField(max_length=200, null=True, blank=True, help_text="미션")

    def __str__(self):
        return str(self.length_category) + "km 경로"

class Spot(models.Model):
    class SpotType(models.IntegerChoices):
        SOL_SPOT = 0    # 솔방울 정산소
        PICK_SPOT = 1   # 픽스팟

    # spot_coordinate = ArrayField(models.FloatField(), null=True, blank=True, help_text="스팟 위경도") # [127.1, 35.0]
    spot_geojson = models.TextField(null=True, blank=True, help_text="스팟 geojson (문자열)")
    spot_type = models.IntegerField(choices=SpotType.choices, help_text="스팟 종류(0:솔방울정산소, 1:픽스팟)")