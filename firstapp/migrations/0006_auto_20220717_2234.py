# Generated by Django 3.2.14 on 2022-07-17 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_bookdata_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookdata',
            name='names',
            field=models.CharField(default='Нету', max_length=200),
        ),
        migrations.AlterField(
            model_name='bookdata',
            name='photo',
            field=models.ImageField(default='SOME STRING', upload_to=''),
        ),
    ]