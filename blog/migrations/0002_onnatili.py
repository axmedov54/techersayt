# Generated by Django 5.1.1 on 2024-09-21 17:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Onnatili',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
    ]
