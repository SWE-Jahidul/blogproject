# Generated by Django 2.2 on 2019-04-24 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20190424_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postlike',
            name='totalLike',
            field=models.IntegerField(default=0),
        ),
    ]
