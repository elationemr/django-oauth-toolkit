# Generated by Django 1.11.1 on 2017-05-14 11:41
import django.db.models.deletion
from django.db import migrations, models

from oauth2_provider.settings import oauth2_settings


class Migration(migrations.Migration):

    dependencies = [
        ("oauth2_provider", "0005_auto_20170514_1141"),
    ]

    operations = [
        migrations.AddField(
            model_name="accesstoken",
            name="source_refresh_token",
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=oauth2_settings.REFRESH_TOKEN_MODEL, related_name="refreshed_access_token"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="refreshtoken",
            name="revoked",
           field=models.DateTimeField(null=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="refreshtoken",
            name="token",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="refreshtoken",
            name="access_token",
            field=models.OneToOneField(blank=True, null=True, related_name="refresh_token", to=oauth2_settings.ACCESS_TOKEN_MODEL, on_delete=models.SET_NULL),
        ),
        migrations.AlterUniqueTogether(
            name="refreshtoken",
            unique_together=set([("token", "revoked")]),
        ),
    ]
