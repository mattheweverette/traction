# Generated by Django 3.1.3 on 2020-12-08 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traction_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='hash',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
