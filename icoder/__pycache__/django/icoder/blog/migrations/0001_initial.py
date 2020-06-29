# Generated by Django 3.0.7 on 2020-06-16 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=20)),
                ('slug', models.CharField(max_length=130)),
                ('timestamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
