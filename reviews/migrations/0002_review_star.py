# Generated by Django 3.2.13 on 2022-10-07 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='star',
            field=models.CharField(default='⭐⭐⭐', max_length=20),
        ),
    ]
