# Generated by Django 3.2.14 on 2022-07-17 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_auto_20220717_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookdata',
            name='avtor',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='bookdata',
            name='janr',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='bookdata',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='bookdata',
            name='place',
            field=models.CharField(max_length=200),
        ),
    ]
