# Generated by Django 3.2.8 on 2021-10-12 05:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dvd',
            fields=[
                ('dvd_id', models.AutoField(primary_key=True, serialize=False)),
                ('genre', models.CharField(blank=True, max_length=60)),
                ('title', models.CharField(blank=True, max_length=60)),
                ('release_year', models.CharField(blank=True, max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='RegUser',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('username', models.CharField(blank=True, max_length=60, unique=True)),
                ('password', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('postPK', models.AutoField(primary_key=True, serialize=False)),
                ('post_id', models.CharField(blank=True, max_length=4)),
                ('post_title', models.CharField(blank=True, max_length=60)),
                ('post_content', models.TextField(blank=True)),
                ('post_status', models.CharField(blank=True, choices=[('PENDING', 'PENDING'), ('APPROVED', 'APPROVED')], default='PENDING', max_length=10)),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]