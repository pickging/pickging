# Generated by Django 4.1.1 on 2022-09-11 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_guild'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='point',
            field=models.IntegerField(default=0, help_text='잔여포인트'),
        ),
        migrations.AddField(
            model_name='user',
            name='region',
            field=models.CharField(blank=True, help_text='지역', max_length=10, null=True),
        ),
    ]
