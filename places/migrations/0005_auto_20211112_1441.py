# Generated by Django 3.2.9 on 2021-11-12 14:41

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_alter_place_description_long'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='number',
            field=models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Порядковый номер'),
        ),
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(upload_to='', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Длинное описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(blank=True, verbose_name='Короткое описание'),
        ),
    ]
