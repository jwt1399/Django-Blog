# Generated by Django 3.0.5 on 2020-04-29 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20200429_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='site_name',
            field=models.CharField(default='简简', max_length=30, verbose_name='网站名字'),
        ),
    ]