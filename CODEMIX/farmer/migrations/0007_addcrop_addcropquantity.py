# Generated by Django 3.0.4 on 2020-07-04 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0006_auto_20200704_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='addcrop',
            name='addCropQuantity',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
