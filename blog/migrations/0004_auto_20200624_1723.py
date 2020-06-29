# Generated by Django 3.0.7 on 2020-06-24 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_blogcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='post',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
