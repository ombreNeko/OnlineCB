# Generated by Django 2.2.3 on 2019-07-21 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0004_auto_20190721_0646'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='recommended',
            field=models.BooleanField(default=False),
        ),
    ]
