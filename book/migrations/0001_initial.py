# Generated by Django 2.2.6 on 2023-05-05 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booAAddress', models.CharField(max_length=100)),
                ('create_time', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('reserve1', models.CharField(max_length=100)),
                ('reserve2', models.CharField(max_length=100)),
                ('reserve3', models.CharField(max_length=100)),
                ('reserve4', models.CharField(max_length=100)),
                ('reserve5', models.CharField(max_length=100)),
                ('booAtime', models.CharField(max_length=100)),
                ('Column1', models.CharField(max_length=100)),
                ('booFare', models.CharField(max_length=100)),
                ('booNo', models.CharField(max_length=100)),
                ('booNumber', models.CharField(max_length=100)),
                ('booOrderNum', models.CharField(max_length=100)),
                ('booTime', models.CharField(max_length=100)),
                ('boobAddress', models.CharField(max_length=100)),
                ('boobTime', models.CharField(max_length=100)),
                ('comCode', models.CharField(max_length=100)),
                ('cusTelNumber', models.CharField(max_length=100)),
                ('flag', models.CharField(max_length=100)),
                ('flagPay', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Book',
                'db_table': 'book',
            },
        ),
    ]