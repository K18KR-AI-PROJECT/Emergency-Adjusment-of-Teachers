# Generated by Django 3.0.4 on 2020-03-28 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Day', models.CharField(max_length=100)),
                ('Teacher_id', models.IntegerField()),
                ('Time', models.DateTimeField()),
            ],
        ),
    ]
