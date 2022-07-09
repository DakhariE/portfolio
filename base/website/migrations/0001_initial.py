# Generated by Django 4.0.5 on 2022-07-08 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10000)),
                ('photo', models.ImageField(upload_to='')),
                ('description', models.CharField(max_length=1000000)),
                ('tech', models.CharField(max_length=10000)),
                ('gitlink', models.CharField(max_length=10000)),
                ('codelink', models.CharField(max_length=10000)),
            ],
        ),
    ]