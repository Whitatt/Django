# Generated by Django 2.1.5 on 2021-09-09 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210908_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('drinks', 'drinks'), ('appetizers', 'appetizers'), ('entrees', 'entrees'), ('treats', 'treats')], max_length=60),
        ),
    ]
