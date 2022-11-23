# Generated by Django 4.1.3 on 2022-11-23 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_alter_userprofile_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('detials', models.TextField()),
                ('userProfileImage', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_user', to='users.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='SavePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='save_post', to='post.post')),
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='users.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='ImagePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='post')),
                ('post', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_image', to='post.post')),
            ],
        ),
    ]
