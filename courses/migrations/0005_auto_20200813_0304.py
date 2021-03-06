# Generated by Django 2.2.6 on 2020-08-13 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20200813_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='logo_url',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='image_url',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='summary',
            field=models.TextField(),
        ),
    ]
