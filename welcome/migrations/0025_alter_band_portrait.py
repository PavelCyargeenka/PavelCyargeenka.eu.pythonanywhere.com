# Generated by Django 4.1.2 on 2022-12-02 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0024_alter_band_portrait'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='portrait',
            field=models.ImageField(default='', upload_to='portraits'),
        ),
    ]
