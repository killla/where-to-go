# Generated by Django 3.2.9 on 2021-11-07 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['number']},
        ),
        migrations.AlterField(
            model_name='image',
            name='number',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
