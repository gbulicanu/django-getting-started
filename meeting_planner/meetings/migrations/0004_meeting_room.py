# Generated by Django 3.0.7 on 2020-06-22 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0003_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='meetings.Room'),
        ),
    ]