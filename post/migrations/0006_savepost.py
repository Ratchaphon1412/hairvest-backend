# Generated by Django 4.1.3 on 2022-11-21 09:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0005_rename_post_image_imagepost_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postID', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='save_post', to='post.post')),
                ('userID', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
