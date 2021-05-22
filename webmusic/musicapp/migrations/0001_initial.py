# Generated by Django 3.2.2 on 2021-05-11 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('song_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('singer', models.CharField(max_length=50)),
                ('tags', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='docs')),
                ('song', models.FileField(upload_to='docs')),
            ],
        ),
    ]