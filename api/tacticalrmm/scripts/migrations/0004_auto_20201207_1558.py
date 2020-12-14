# Generated by Django 3.1.3 on 2020-12-07 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scripts', '0003_auto_20200922_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='script',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='script',
            name='favorite',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='script',
            name='script_base64',
            field=models.TextField(blank=True, null=True),
        ),
    ]
