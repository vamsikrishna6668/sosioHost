# Generated by Django 2.1.1 on 2018-11-06 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sc1', '0002_auto_20181106_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='sosio',
            name='res',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
