# Generated by Django 3.0.5 on 2020-08-25 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_servicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='imagen',
            field=models.ImageField(upload_to='servicios'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]