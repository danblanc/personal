# Generated by Django 4.1.1 on 2022-10-28 02:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_types_project_url_project_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('intro', models.TextField()),
                ('url', models.URLField(null=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 10, 28, 2, 22, 4, 844781))),
            ],
        ),
    ]
