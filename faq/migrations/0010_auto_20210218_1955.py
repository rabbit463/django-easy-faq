# Generated by Django 3.1.4 on 2021-02-19 00:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('faq', '0009_faqcomment_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faqcomment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]