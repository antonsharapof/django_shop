# Generated by Django 3.1.3 on 2020-11-24 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
