# Generated by Django 3.2.14 on 2022-07-17 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('avtor', models.CharField(max_length=20)),
                ('janr', models.CharField(max_length=20)),
                ('star', models.IntegerField()),
                ('place', models.CharField(max_length=20)),
                ('aboutbook', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
