# Generated by Django 3.2.2 on 2022-01-31 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=250)),
                ('first_name', models.CharField(default='', max_length=250)),
                ('last_name', models.CharField(default='', max_length=250)),
                ('password', models.CharField(default='', max_length=250)),
            ],
        ),
    ]
