# Generated by Django 4.2.3 on 2023-08-18 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goodscategory',
            options={'verbose_name': '商品类型'},
        ),
        migrations.AlterModelTable(
            name='goods',
            table='',
        ),
        migrations.AlterModelTable(
            name='goodscategory',
            table='goodscategory',
        ),
    ]